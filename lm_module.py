from transformers import pipeline
from transformers import AutoModelForCausalLM, AutoTokenizer

#model_name = "apple/OpenELM-270M-Instruct"
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name)
nlp = pipeline("text-generation", model=model, tokenizer=tokenizer, trust_remote_code=True)

def analyze_text_with_local_llm(text):
    response = nlp(text, max_new_tokens=150, num_return_sequences=1)
    return response[0]['generated_text']

def extract_keywords_and_summary(tweet_text):
    summary = analyze_text_with_local_llm(tweet_text)
    keywords = summary.split()
    #Space for pushing data into df
    return keywords, summary