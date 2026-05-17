from flask import Flask, request
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}"

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot ishlayapti"

@app.route(f"/webhook/{TOKEN}", methods=["POST"])
def webhook():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        requests.post(f"{URL}/sendMessage", json={
            "chat_id": chat_id,
            "text": text
        })

    return "ok"
