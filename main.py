from tinydb import TinyDB

# create TinyDB instance
db = TinyDB('db.json') 
# Insert doucment into database
db.insert({'name': 'Zarif', 'age': 35})