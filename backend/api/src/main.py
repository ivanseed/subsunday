from flask import Flask
from flask_restful import Api

from resources import VotesResource
from datastore import DataStore
from models import Vote

from os import environ


def make_datastore():
    return DataStore(environ['DATASTORE_URI'])


def main():
    app = Flask(__name__)

    api = Api(app)

    store = make_datastore()
    store_context = dict(store=store)

    api.add_resource(VotesResource, r'/votes',
                     resource_class_kwargs=store_context)

    debug_mode = environ.get('DEBUG') is not None
    app.run(
        host='0.0.0.0',
        port=80,
        debug=debug_mode,
    )


if __name__ == '__main__':
    main()
