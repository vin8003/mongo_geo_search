from dbconnect import dbconnect
import json

data = open('jsondatastates.json', 'r').read()
str_data = json.loads(data)
db = dbconnect()

for i in str_data:
    db.uncleaned_data.insert_one(i)
