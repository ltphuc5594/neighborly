import azure.functions as func
import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:
    id = req.params.get('id')
    print("--------------->", id)

    if id:
        try:
            url = "mongodb://labdemo:9oMnympboqcd6bUXbTUnig9PNuORjVNunYYsmRvDjGaWWdE9ypPbLoUa7UW7XvhCNV32KySVC3RqACDbORv3Cw==@labdemo.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@labdemo@" 
            client = pymongo.MongoClient(url)
            database = client['test']
            collection = database['advertisements']

            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)
            print("----------result--------")

            result = dumps(result)
            print(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)
