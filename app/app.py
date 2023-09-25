from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from flask import render_template, redirect, url_for
import psycopg2
import random

app = Flask(__name__)
CORS(app)

messages = []

RPI_2_IP = "192.168.1.22"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.json
    message = data.get("message")

    if message:
        messages.append(message)
        send_to_rpi_2(message)
        return jsonify({"message": "Message sent from RPI-1."})
    else:
        return jsonify({"error": "Invalid message data."}), 400


@app.route("/get_messages", methods=["GET"])
def get_messages():
    return jsonify({"messages": messages})


@app.route("/receive_message", methods=["POST"])
def receive_message():
    data = request.json
    message = data.get("message")

    if message:
        messages.append(message)
        return jsonify({"message": "Message received by RPI-1."})
    else:
        return jsonify({"error": "Invalid message data."}), 400


def send_to_rpi_2(message):
    url = f"http://{RPI_2_IP}:5000/receive_message"
    payload = {"message": message}
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Message sent to RPI-2.")
        else:
            print("Failed to send message to RPI-2.")
    except Exception as e:
        print("Error sending message to RPI-2:", str(e))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
