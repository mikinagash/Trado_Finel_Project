from pymongo import MongoClient
class Mongodb:
    # miki
    def search_query(self,key,value):
        cluster = MongoClient("mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority")
        db = cluster["trado_qa"]
        collection = db["orders"]
        results = collection.find({key:value})
        for result in results:
            return result["lastName"]


