from pymongo import MongoClient

mongo_client = MongoClient('mongodb://db:27017')
mongo_db = mongo_client['sentences_database']
users = mongo_db['users']
