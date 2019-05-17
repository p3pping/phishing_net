from flask_restful import Resource
from flask import Flask, request
from db.phish_db import phish_db

class DebugIncrement(Resource):
    def get(self):
        session = phish_db.sessionmaker()
        all_increments = phish_db.get_all_increments(session)
        return_msg = { "increments": [] }
        for increment in all_increments:
            return_msg["increments"].append({
                "table": increment.table,
                "value": increment.value
                })

        return return_msg

class DebugUrl(Resource):
    def get(self):
        session = phish_db.sessionmaker()
        all_url_ratings = phish_db.gel_all_url_ratings(session)
        return_msg = { "increments": [] }
        for url_rating in all_url_ratings:
            return_msg["increments"].append({
                "id": url_rating.id, 
                "url": url_rating.link,
                "rating": url_rating.rating
                })

        return return_msg