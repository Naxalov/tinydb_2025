from tinydb import TinyDB
from tinydb.table import Document


# create TinyDB instance
db = TinyDB('db.json', indent=4) 
data = db.all()
for doc in data:
    if doc['job'] == 'developer':
        print(doc.doc_id, doc['name'], doc['age'])