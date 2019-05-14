from flask_restful import Resource
from flask import Flask, request
from db.phish_db import phish_db

class UrlRating(Resource):    
    def get(self):
        #if no url is provided gtfo
        if("url" not in request.args.keys()):
            return {
                "result" : "failed",
                "url" : "no 'url' supplied",
                "rating" : -1
            }

        #look for a rating
        url = request.args["url"]
        rating = phish_db.get_url_rating(url)       

        #found a rating
        if(rating > 0):
            return {
                "result" : "success",
                "url" : url,
                "rating" : rating
            }
        #no rating found
        return {
                "result" : "failed",
                "url" : url,
                "rating" : -1
            }
        
    def post(self):
        #if no url is provided gtfo
        if("url" not in request.args.keys()):
            return {
                "result" : "failed",
                "url" : "no 'url' supplied",
                "rating" : -1
            }

        url = request.args["url"]

        #do we have the url already?
        rating = phish_db.get_url_rating(url)
        url_row = None
        if(rating < 0):
            #create new rating
            url_row = phish_db.insert_url_rating(1,url,1)
            if(url_row is Exception):
                return {
                "result" : "failed",
                "url" : url,
                "rating" : -1
            }
            #rating created
            return {
                "result" : "success",
                "url" : url,
                "rating" : url_row.rating
                }
        
        #we already have a rating so update it
        rating += 1
        url_row = phish_db.set_url_rating(url, rating)

        return {
            "result" : "success",
            "url" : url,
            "rating" : url_row.rating
        }