from flask import Flask, request
from flask_restful import Resource, Api
from url_rating import UrlRating
from url_rank import UrlRank
from db.phish_db import PhishDB, phish_db

app = Flask(__name__)
api = Api(app)

if(__name__ == "__main__"):
    api.add_resource(UrlRating, '/rating')
    api.add_resource(UrlRank, '/rank')
    app.run(debug=True)
