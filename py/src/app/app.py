from flask import Flask, request
from app import handlers


@app.route('/', methods=['POST', 'GET'])
def index():
    return f'Valid requests: {", ".join(handlers.VALID_REQUESTS)}'


@app.route('/<req>', methods=['POST'])
def req_handler(req):
    return handlers.__entry__(req, request.get_data())
