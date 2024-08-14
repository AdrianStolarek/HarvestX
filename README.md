# HarvestX

A web scraper designed to extract tweets from specified Twitter (X) user profiles using Selenium and BeautifulSoup. Technologies Used: Selenium (4.0.0), BeautifulSoup (4.10.0), Pandas (1.3.3), Requests (2.26.0), WebDriverManager (3.5.2), ChromeDriver (latest version compatible with your Chrome browser). Collect tweets based on user profiles. Extract relevant information such as username, tweet content, creation date, retweet count, and favorite count. Save the scraped tweets in JSON format. Analyze the tweets by extracting keywords and generating summaries using a Language Model Module (LLM API). Save the analyzed tweets in a JSON file.

# How to Use

Ensure you have Python installed.
Install the required libraries using pip:
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

Current model is just a simple exemplary one. It is sugested to use more sophisticated LLM such as:
```
inceptionai/jais-family-30b-8k-chat
```
Simply change model_name and add imports from below:

```
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
```
Also model and tokenizer have to be set to:

```
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True)
```
In this case, 'summarization' keyword has to be changed to 'generated_text'. Same for response[0]['summary_text'] (response[0]['generated_text']).

Graphical Representation: 

Implementation of a functionality to visualize the parsed data in a graph format.


Feel free to contribute to this project by forking the repository and submitting pull requests. Any suggestions or improvements are welcome.
