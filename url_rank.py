from flask_restful import Resource
from flask import Flask, request

class UrlRank(Resource):
    def get(self):
        rating = {
            "url": "some url",
            "rating": 9001            
        }
        
        rank = "very low"
        url_rating = rating["rating"]
        
        if(url_rating > 9000):
            rank = "severe"
        elif(url_rating > 4000):
            rank = "high"
        elif(url_rating > 1000):
            rank = "moderate"
        elif (url_rating > 200):
            rank = "low"

        return_msg = {
            "result" : "success",
            "url" : "some url",
            "rank" : rank
        }

        return return_msg