import logging
import os

import azure.functions as func
import pymongo
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = os.environ.get("NEIGHBORLY_MONGODB_CONNECTION_STRING")
        client = pymongo.MongoClient(url)
        database = client[os.environ.get("NEIGHBORLY_MONGODB_DATABASE")]
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)
