from transformers import pipeline
from transformers import AutoTokenizer, LongT5ForConditionalGeneration

model_name = "Stancld/longt5-tglobal-large-16384-pubmed-3k_steps"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = LongT5ForConditionalGeneration.from_pretrained(model_name)
nlp = pipeline("summarization", model=model, tokenizer=tokenizer, trust_remote_code=True)

def analyze_text_with_local_llm(text):
    input_text = "Summarize: " + text
    response = nlp(input_text, max_length=10, min_length=10, num_return_sequences=1)
    return response[0]['summary_text']

def extract_keywords_and_summary(tweet_text):
    summary = analyze_text_with_local_llm(tweet_text)
    keywords = summary.split()
    #Space for pushing data into df
    return keywords, summary