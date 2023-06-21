from pymongo import MongoClient

class Database:
    def __init__(self, uri, database_name):
        self.client = MongoClient(uri)
        self.db = self.client[database_name]
        self.news_collection = self.db['news']

    def insert_article(self, article):
        """
        Insert a single article into the database.
        
        :param article: A dictionary containing article information.
        """
        self.news_collection.insert_one(article)
    
    def insert_articles(self, articles):
        """
        Insert multiple articles into the database.
        
        :param articles: A list of dictionaries, each containing article information.
        """
        self.news_collection.insert_many(articles)
    
    def get_articles(self, filters=None, sort_by=None, limit=None):
        """
        Retrieve articles from the database with optional filters, sorting, and limit.
        
        :param filters: A dictionary specifying the filters.
        :param sort_by: A tuple (field_name, direction), where direction is 1 for ascending and -1 for descending.
        :param limit: An integer specifying the maximum number of articles to retrieve.
        :return: A list of articles.
        """
        query = self.news_collection.find(filters).limit(limit)

        if sort_by:
            query.sort(*sort_by)

        return list(query)

    def search_articles(self, query, limit=None):
        """
        Search articles based on a text query.
        
        :param query: The text query for searching articles.
        :param limit: An integer specifying the maximum number of articles to retrieve.
        :return: A list of articles.
        """
        search_query = {"$text": {"$search": query}}
        return list(self.news_collection.find(search_query).limit(limit))
    
    def update_article(self, article_id, updated_data):
        """
        Update a single article in the database.
        
        :param article_id: The id of the article to update.
        :param updated_data: A dictionary containing the data to update.
        """
        self.news_collection.update_one({"_id": article_id}, {"$set": updated_data})
