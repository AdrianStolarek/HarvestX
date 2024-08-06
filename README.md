# HarvestX
This project is a comprehensive web scraping and data analysis tool developed in Python, consisting of two main components:

Twitter (X) Web Scraper:

A web scraper designed to extract tweets from specified Twitter (X) user profiles using Selenium and BeautifulSoup. Technologies Used: Selenium (4.0.0), BeautifulSoup (4.10.0), Pandas (1.3.3), WebDriverManager (3.5.2), ChromeDriver (latest version compatible with your Chrome browser). Collect tweets based on user profiles. Extract relevant information such as username, tweet content, creation date, retweet count, and favorite count. Save the scraped tweets in JSON format. Analyze the tweets by extracting keywords and generating summaries using a Language Model Module (LLM API). Save the analyzed tweets in a JSON file. Scientific Papers and Website Articles Scraper.

A separate module for scraping data from scientific papers and website articles. BeautifulSoup (4.10.0), Requests (2.26.0). Extract text and metadata from scientific papers and articles. Process and clean the data for further analysis. Key Features: Uses Selenium to dynamically interact with web pages and scrape content. Stores scraped data in structured JSON files. Utilizes a Language Model Module (LLM API) to extract keywords and generate summaries for each tweet. (Future Work) Will include functionality to visualize parsed data in a graphical format. Text Analysis with LLM: The text analysis is performed using a local language model, specifically: Model Used: apple/OpenELM-270M-Instruct. Technologies Used: Transformers library from Hugging Face. Analyze Text: Uses the pipeline function from the Transformers library to generate text based on input. Extract Keywords and Summary: The function extract_keywords_and_summary takes tweet text as input, generates a summary using the local LLM, and extracts keywords from the summary.
```
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
```
How to Use
Set Up:

Ensure you have Python installed.
Install the required libraries using pip:
sh
```
pip install selenium beautifulsoup4 pandas webdriver_manager requests transformers
```
Configuration:

Update the ChromeDriver path in the script if necessary.
Ensure you have the latest version of ChromeDriver compatible with your Chrome browser.
Running the Scraper:

Use the provided collect_tweets function to scrape tweets from specified user profiles.
The script will save the scraped tweets to a JSON file and then analyze the tweets, saving the results to another JSON file.
Analyzing Data:

Utilize the LLM API to extract keywords and generate summaries from the tweets.
Future Work
Graphical Representation: Implement functionality to visualize the parsed data in a graph format.
Enhanced Scraping Capabilities: Extend scraping capabilities to other social media platforms and content types.
Contribution
Feel free to contribute to this project by forking the repository and submitting pull requests. Any suggestions or improvements are welcome.

License
This project is licensed under the MIT License.
