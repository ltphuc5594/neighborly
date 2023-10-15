import logging

import azure.functions as func
import pymongo
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://labdemo:9oMnympboqcd6bUXbTUnig9PNuORjVNunYYsmRvDjGaWWdE9ypPbLoUa7UW7XvhCNV32KySVC3RqACDbORv3Cw==@labdemo.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@labdemo@"
        client = pymongo.MongoClient(url)
        database = client['test']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)
