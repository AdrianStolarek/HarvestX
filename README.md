# HarvestX

A web scraper designed to extract tweets from specified Twitter (X) user profiles using Selenium and BeautifulSoup. Technologies Used: Selenium (4.0.0), BeautifulSoup (4.10.0), Pandas (1.3.3), Requests (2.26.0), WebDriverManager (3.5.2), ChromeDriver (latest version compatible with your Chrome browser). Collect tweets based on user profiles. Extract relevant information such as username, tweet content, creation date, retweet count, and favorite count. Save the scraped tweets in JSON format. Analyze the tweets by extracting keywords and generating summaries using a Language Model Module (LLM API). Save the analyzed tweets in a JSON file.

# How to Use

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
