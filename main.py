from tinydb import TinyDB
from tinydb.table import Document


# create TinyDB instance
db = TinyDB('db.json', indent=4) 


# Insert doucment into database
db.insert_multiple([
    {'name': 'Zarif', 'age': 35},
    {'name': 'Aziz', 'age': 25},
    {'name': 'Abror', 'age': 30},
    {'name': 'Alisher', 'age': 20},
    {'name': 'Abdulaziz', 'age': 19},

])

# Get document from database
data = db.all()
for doc in data:
    print(doc.doc_id, doc['name'], doc['age'])
