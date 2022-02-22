import urllib.request
import json


from flask import Flask, request, jsonify
from flask import make_response

from helpers.environments import config
from helpers.helpers_logging import logging

app = Flask(__name__)

def sendData(payload):
    """
    This function sends the payload to the configured endpoint.
    """
    req = urllib.request.Request(config.hookurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(payload)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route("/", methods=["GET"])
def getindex():
    logging.debug("Received GET request")
    """Endpoint for the root of the Flask app."""
    return ({'message':'welcome'})

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    """Endpoint for the webhook."""
    if request.method == "GET":
        logging.debug("Received a GET request")
        # Return the verification code.
        return jsonify({'status': 'ok', 'code': 0})

    elif request.method == "POST":
        logging.debug("Received a POST request")
        # Receive the message from the user.
        message = request.json.get('message')
        # Send the message to channel   .
        sendData(message)
        print(message)
        return jsonify({'status': 'ok', 'code': 0})

@app.route("/webhook", methods=["GET", "POST"])
def postData():
    """Endpoint for receiving webhook messages."""
    if request.method == "GET":
        logging.debug("Received a GET request")
        # Return the verification code.
        return jsonify({'status': 'ok', 'code': 0})
    if request.method == "POST":
        data = request.get_json()
        commit_author = data["actor"]["displayName"]
        commit_repository = data['repository']['name']
        m = 'High priority incident has occurred -  ${issue.summary}. Click here to respond - ${request.url}'

        payload = {'text': m}

        sendData(payload)
        return jsonify({'status': 'ok', 'code': 0})