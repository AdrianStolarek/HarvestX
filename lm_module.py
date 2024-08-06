from transformers import pipeline
from transformers import LlamaForCausalLM, LlamaTokenizer

model_name = "apple/OpenELM-270M-Instruct"
nlp = pipeline("text-generation", model=model_name, trust_remote_code=True)

def analyze_text_with_local_llm(text):
    response = nlp(text, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']

def extract_keywords_and_summary(tweet_text):
    summary = analyze_text_with_local_llm(tweet_text)
    keywords = summary.split()
    return keywords, summary