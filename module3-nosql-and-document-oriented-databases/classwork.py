import sqlite3
import pymongo
import dns

"""
How was working with MongoDB different from working with PostgreSQL?
- The commands were different and NoSQL commands were more annoying
especially after practicing SQL more and then just shifting gears
But in the end, its not that different. 
"""

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

password = 'f0dQb2KI8pqrxThT'
# remove this when uploading to GitHub - must be private
dbname = 'test'

client = pymongo.MongoClient \
    ("mongodb+srv://BGogineni:" + password + "@ds18-cluster.ktudr.mongodb.net/"
     + dbname + "?retryWrites=true&w=majority")
db = client.test

db.test.insert_one({'x': 1})
# inserts this dictionary into the database
db.test.count_documents({'x': 1})
# counts the number of key-value pairs with 'x':1
db.test.find({'x': 1})
# returns a cursor
list(db.test.find({'x': 1}))
# returns all of the values where x = 1
db.test.find_one({'x': 1})
# only returns the first one it finds where the search = true

max_doc = {
    'food': 'lasagna',
    'color': 'maroon',
    'number': 7
}
jim_doc = {
    'animal': 'ostrich',
    'color': 'blue',
    'fav cities': ['New York', 'Chicago', 'London']
}
# MongoDB does not have a super set structure
# so the order does not have to have the same structure either
# keys do HAVE to be strings though

all_docs = [max_doc, jim_doc]

db.test.insert_many(all_docs)

result = list(db.test.find())
# returns all the contents of the db
# uses list again - otherwise it would show a cursor

more_docs = []
for i in range(10):
    doc = {'even': i % 2 == 0, 'value': i}
    more_docs.append(doc)

db.test.insert_many(more_docs)

list(db.test.find({'even': True, 'value': 0}))
# finds the first value because has two parameters
list(db.test.find({'even': True}))
# finds all evens - basically the SQL where function

change = db.test.update_one({'x': 1}, {'$inc': {'x': 3}})
# updates one instance of 'x': 1 by increasing 'x' by 3
change.matched_count()
change.modified_count()
# does exactly what the function says

if __name__ == "__main__":
    print(result)
