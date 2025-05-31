from pymongo import MongoClient

def get_database():
    client=MongoClient("localhost",27017)
    return client['pymongotestdb'] 

def add_items(collection):
    item_1 = {
        "_id": "U11T00001",
        "item_name": "Blender",
        "max_discount": "10%",
        "batch_number": "RR450020FRG",
        "price": 340,
        "category": "kitchen appliance"
    }
    item_2 = {
        "_id": "U11T00002",
        "item_name": "Egg",
        "category": "food",
        "quantity": 12,
        "price": 36,
        "item_description": "brown country eggs"
    }
    collection.find()
    
def main():
    dbname=get_database()
    collection=dbname["user"]
    found=collection.find()
    for f in found:
        print(f)
    
if __name__=="__main__":
    main()