import azure.functions as func
import pymongo
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        url = "mongodb://labdemo:9oMnympboqcd6bUXbTUnig9PNuORjVNunYYsmRvDjGaWWdE9ypPbLoUa7UW7XvhCNV32KySVC3RqACDbORv3Cw==@labdemo.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@labdemo@"
        client = pymongo.MongoClient(url)
        database = client['test']
        collection = database['advertisements']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)
