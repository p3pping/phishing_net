from flask_restful import Resource
from flask import Flask, request
from db.phish_db import phish_db

class DebugIncrement(Resource):
    def get(self):
        all_increments = phish_db.get_all_increments()
        return_msg = { "increments": [] }
        for increment in all_increments:
            return_msg["increments"].append({"table": increment.table, "value": increment.value})

        return return_msg