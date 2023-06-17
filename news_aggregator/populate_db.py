from pymongo import MongoClient
import datetime

connection_string = "mongodb+srv://holzheuc:ymmMpiBwKUL3uKDK@newsaggregatorcluster.bfjhaay.mongodb.net/"

# Create client to interact with MongoDB
client = MongoClient(connection_string)

# Select database
db = client.newsAggregatorDB

# Select collection
articles = db.articles

# Sample articles to insert
sample_articles = [
    {
        'title': 'AI Breakthroughs in 2023',
        'url': 'https://example.com/ai-2023',
        'source': 'Tech News',
        'date': datetime.datetime(2023, 6, 16, 8, 0),
        'category': 'Technology',
        'keywords': ['AI', 'Machine Learning', '2023']
    },
    {
        'title': 'AI Breakthroughs in 2023',
        'url': 'https://example.com/ai-2023',
        'source': 'Tech News',
        'date': datetime.datetime(2023, 6, 15, 10, 30),
        'category': 'Technology',
        'keywords': ['AI', 'Machine Learning', '2023']
    },
    {
        'title': 'New Study Reveals Health Benefits of Green Tea',
        'url': 'https://example.com/green-tea',
        'source': 'Health Magazine',
        'date': datetime.datetime(2023, 6, 15, 10, 30),
        'category': 'Health',
        'keywords': ['Green Tea', 'Health']
    }
]

# Insert sample articles into the collection
articles.insert_many(sample_articles)

print("Sample articles inserted into the database.")