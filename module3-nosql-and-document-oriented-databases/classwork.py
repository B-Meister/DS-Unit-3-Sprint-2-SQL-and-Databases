import sqlite3
import pymongo
import dns

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

password = 'f0dQb2KI8pqrxThT'
dbname = 'test'
client = pymongo.MongoClient \
    ("mongodb+srv://BGogineni:" + password + "@ds18-cluster.ktudr.mongodb.net/"
     + dbname + "?retryWrites=true&w=majority")
# test is the dbname - near the end of the url

db = client.test

db.test.insert_one({'x': 1})
# result = ''

if __name__ == "__main__":
    pass
