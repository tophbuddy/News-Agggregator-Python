import requests
import logging
from datetime import datetime
from .scraper import NewsScraper

# Logging Config
logging.basicConfig(
    filename='news_fetcher.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

class NewsFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/everything"
        # Initialize scraper with base_url of website to scrape
        self.scraper = NewsScraper(base_url='http://example.com')
        logging.info("NewsFetcher initialized")
    
    def fetch_news(self, query, category=None, from_date=None, to_date=None, sort_by="publishedAt", page=1):
        """
        Fetch news articles using the News API and scraping
        
        :param query: Keywords or phrases to search for
        :param category: Category to scrape news articles from
        :param from_date: A datetime object representing the start date
        :param to_date: A datetime object representing the end date
        :param sort_by: The ordering of the articles, can be 'relevancy', 'popularity', or 'publishedAt'
        :param page: The page number to return
        :return: A list of news articles
        """ 
        logging.info(f"Fetching news with query: {query}")

        # Construct parameters for API request
        params = {
            "q" : query,
            "sortBy" : sort_by,
            "page" : page,
            "apiKey" : self.api_key
        }

        if from_date:
            params["from"] = from_date.strftime("%Y-%m-%dT%H:%M:%S")
        
        if to_date:
            params["to"] = to_date.strftime("%Y-%m-%dT%H:%M:%S")

        # Request to News API
        api_articles = []
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            # Get Articles from API
            api_articles = response.json()["articles"]
            logging.info(f"Fetched {len(api_articles)} articles from News API")
        except requests.HTTPError as e:
            logging.error(f"An HTTP error occured: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

        # Scrape articles if category provided
        scraped_articles = []
        try:
            if category:
                scraped_articles = self.scraper.fetch_articles(category)
                logging.info(f"Scraped {len(scraped_articles)} articles from {category} category")
        except Exception as e:
            logging.error(f"Error scraping articles: {e}")

        # Normalize API articles
        normalized_api_articles = [
            {
                "title": article["title"],
                "description": article["description"],
                "url": article["url"],
                "source": article["source"]["name"],
                "published_at": article["publishedAt"]
            }
        ]
        
        # Combine articles from API and scraped article
        return api_articles + scraped_articles

if __name__ == "__main__":
    news_fetcher = NewsFetcher(api_key='fad17fd7972541d3ab0658ea44ad5c3c')    
    