from flask import Flask, request
import handlers


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return f'Valid requests: {", ".join(handlers.__VALID_REQUESTS__)}'


@app.route('/<req>', methods=['POST'])
def req_handler(req):
    return handlers.__entry__(req, request.get_data())


if __name__ == '__main__':
    app.run()
