from dotenv import load_dotenv
from flask import Flask, request, jsonify

from os import environ as env

# Load environment variables from a .env file:
load_dotenv('.env')

# Load in configuration from environment variables:
STREAM_URL = env['STREAM_URL']


app = Flask(__name__)

ncco = [
    {
        "action": "stream",
        "streamUrl": [
            STREAM_URL
        ]
    }
]

@app.route("/webhooks/answer")
def answer_call():
    return jsonify(ncco)

@app.route("/webhooks/event", methods=['POST'])
def events():
    return ("200")

if __name__ == '__main__':
    app.run(host="localhost", port=9000)
