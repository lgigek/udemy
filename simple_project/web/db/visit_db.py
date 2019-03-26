from pymongo import MongoClient

client = MongoClient('mongodb://db:27017')
db = client.test_db
col_user_num = db['user_num']

col_user_num.insert({'num_of_users': 0})


def get_user_num():
    return col_user_num.find({})[0]['num_of_users']


def update_user_num(current_num):
    col_user_num.update({}, {'$set': {"num_of_users": current_num}})
