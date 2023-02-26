import pymongo

client = pymongo.MongoClient("mongodb+srv://MunishMongodb:MunishMongodb@cluster0.vgq1qcd.mongodb.net/?retryWrites=true&w=majority")
db=client.test
print(db)

d = {
    "name" : "Munish",
    "sunrname" : "Sharmaq",
    "email" : "munishsharma971@gmail.com"
    }

db1 = client['mongotest']
coll = db1["test"]
coll.insert_one(d)