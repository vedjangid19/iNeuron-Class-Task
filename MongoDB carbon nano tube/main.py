import carbonnanotube

connection_url = """mongodb://test:test@testmongodb-shard-00-00.ebwjm.mongodb.net:27017,testmongodb-shard-00-01.ebwjm.mongodb.net:27017,testmongodb-shard-00-02.ebwjm.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-ee07ny-shard-0&authSource=admin&retryWrites=true&w=majority"""

a = carbonnanotube.CarbonNanoTube()
db = a.make_connection(connection_url)
a.create_database("nanotubeDatabase")
a.create_collection("nanotube")
dict1 = {"name": "sudhanshu",
         "email_id": "ved@gmail.com",
         "product": ["one neuron", "tech neuron", "kid neuron", "drone fleetmatics"],
         "company": "ineuron private limited"
         }
a.insertion(dict1)
# a.insertion(dict1)

# a.delete_document(dict1)
a.update_document({"name": "sudhanshu"}, {"$set": {"name": "SUDHANSHU KUMAR"}})
list = a.find_document({"name": "SUDHANSHU KUMAR"})
for i in list:
    print(i)

a.insert_bulk_data("carbon_nanotubes.csv")
