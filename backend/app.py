from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/getroute/<number>/', methods=['GET'])
def get_route(number):
    print(number)
    req = requests.get("https://transport.tamu.edu/BusRoutesFeed/api/route/{}/buses/mentor".format(number))
    print(req.json())
    return req.json()


if __name__ == '__main__':
    app.run(debug=True)