from flask import Flask, request
from prometheus_flask_exporter.multiprocess import UWsgiPrometheusMetrics


import handlers


app = Flask(__name__)
metrics = UWsgiPrometheusMetrics(app)
metrics.info('pystringer', 'a hello-world app', version='0.0.1')
metrics.register_endpoint('/metrics')


@app.route('/', methods=['POST', 'GET'])
def index():
    return f'Valid requests: {", ".join(handlers.__VALID_REQUESTS__)}'


@metrics.counter('requests_served', 'Number of total requests',
         labels={'request': lambda: request.data.encode('UTF-8')})
@app.route('/<req>', methods=['POST'])
def req_handler(req):
    return handlers.__entry__(req, request.get_data())


if __name__ == '__main__':
    app.run()
