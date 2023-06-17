import requests
from bs4 import BeautifulSoup
from datetime import datetime

class NewsScraper:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def fetch_articles(self, category):
        """
        Fetch news articles from a specific category
        
        :param category: The category of news articles to scrape
        :return: A list of news articles
        """
        # Make request to the news page
        url = f"{self.base_url}/category/{category}"
        response = requests.get(url)

        # Raise exception if the request was unsuccessful
        response.raise_for_status()

        # Parse page content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract articles
        articles = []
        for article_div in soup.find_all("div", class_="article"):
            title = article_div.find("h2").text
            summary = article_div.find("p", class_="summary").text
            published_at = article_div.find("span", class_="published-at").text
            published_at = datetime.strptime(published_at, "%Y-%m-%d %H:%M:%S")

            # Append article list
            articles.append({
                'title' : title,
                'summary' : summary,
                'published_at' : published_at
            })
        
        # Return list of articles
        return articles