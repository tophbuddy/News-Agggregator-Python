import requests
from datetime import datetime
from .scraper import NewsScraper

class NewsFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/everything"
        # Initialize scraper with base_url of website to scrape
        self.scraper = NewsScraper(base_url='http://example.com')
    
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
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()

        # Get articles from API
        api_articles = response.json("articles")

        # Scrape articles if category provided
        scraped_articles = []
        if category:
            scraped_articles = self.scraper.fetch_articles(category)
        
        # Combine articles from API and scraped article
        return api_articles + scraped_articles
    
    