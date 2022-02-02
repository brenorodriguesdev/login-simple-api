import pymongo

myclient = pymongo.MongoClient("mongodb://admin:1@localhost:27017/")
mydb = myclient["admin"]
mycol = mydb["login"]

def insert(login): 
    return mycol.insert_one(login)
def findByLogin(login):
    return mycol.find_one({ "login": login })