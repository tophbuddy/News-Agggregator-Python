import requests
import logging
from bs4 import BeautifulSoup
from datetime import datetime

logging.basicConfig(
    filename='scraper.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

class NewsScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        logging.info("NewsScraper initialized")
    
    def fetch_articles(self, category):
        """
        Fetch news articles from a specific category
        
        :param category: The category of news articles to scrape
        :return: A list of news articles
        """
        logging.info(f"Scraping articles from category: {category}")

        # Make request to the news page
        try:
            url = f"{self.base_url}/category/{category}"
            response = requests.get(url)
            # Raise exception if the request was unsuccessful
            response.raise_for_status()
        except requests.HTTPError as e:
            logging.error(f"An HTTP error occured: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return []

        # Parse page content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find articles on page
        # Note: Will need to update selectors and extraction logic based onsite HTML structure
        articles = soup.find_all('article')

        # Extract details from each article
        extracted_articles = []
        for article in articles:
            headline = article.find('h2').text
            summary = article.find('p').text
            link = article.find('a')['href']
            date_string = article.find('time').text
            date = datetime.strptime(date_string, '%Y-%m-%d').isoformat()

            # Append article list
            articles.append({
                "headline": headline,
                "summary": summary,
                "link": link,
                "date": date
            })
        
        # Return list of articles
        return articles