import os

import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:
    id = req.params.get('id')

    if id:
        try:
            url = os.environ.get("NEIGHBORLY_MONGODB_CONNECTION_STRING")
            client = pymongo.MongoClient(url)
            database = client[os.environ.get("NEIGHBORLY_MONGODB_DATABASE")]
            collection = database['advertisements']

            query = {'_id': ObjectId(id)}
            collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
