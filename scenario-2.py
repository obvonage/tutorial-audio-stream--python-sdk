from dotenv import load_dotenv
from flask import Flask, request, jsonify
import vonage

from os import environ as env

# Load environment variables from a .env file:
load_dotenv('.env')

# Load in configuration from environment variables:
VONAGE_APPLICATION_ID = env['VONAGE_APPLICATION_ID']
CONF_NAME = env['CONF_NAME']
STREAM_URL = env['STREAM_URL']


uuid = ""

ncco = [
    {
        "action": "talk",
        "text": "Please wait while we connect you to the conference"
    },
    {
        "action": "conversation",
        "name": CONF_NAME
    }
]

app = Flask(__name__)

@app.route("/webhooks/answer")
def answer_call():
    global uuid, in_conf
    # print parameters
    print("request.args ", request.args)
    uuid = request.args.get('uuid')
    print("uuid ", uuid)

    return (jsonify(ncco))

@app.route("/webhooks/event", methods=['POST'])
def events():
    return ("200")

@app.route("/stream")
def stream():

    client = vonage.Client(application_id=VONAGE_APPLICATION_ID, private_key='private.key')
    client.voice.send_audio(uuid, stream_url=[STREAM_URL])
    return ("200")


if __name__ == '__main__':
    app.run(host="localhost", port=9000)

