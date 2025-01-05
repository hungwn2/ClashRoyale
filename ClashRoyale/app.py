from flask import Flask, render_template, request
import requests
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()
API_BASE_URL = "https://api.clashroyale.com/v1"
API_TOKEN = os.getenv("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjQ4YjBhNmIwLTBmOWUtNGE2MC05MjBiLTFkMjY5NmM5NTFlMyIsImlhdCI6MTczNDM3NTc2MCwic3ViIjoiZGV2ZWxvcGVyLzEzYWRkMDlhLTI4ZWMtMTI4NC0zNzlkLTk2NzdlZjlmNGNiMSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxMjkuOTcuMTI1LjIzIl0sInR5cGUiOiJjbGllbnQifV19.MuzivUtCDJfgi7G9Jv8j3VLW1266_1BjpqkqNiVAxSZu3jqd7GG811yynGhoKmGp8ROodgvAEd7KZ-sz69Neiw")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/player", methods=["GET"])
def player():
    player_tag = request.args.get("tag")
    if not player_tag:
        return render_template("player.html", error="Please provide a player tag.")

    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(f"{API_BASE_URL}/players/%23{player_tag}", headers=headers)  # Note: Add '#' to the tag.
    
    if response.status_code == 200:
        player_data = response.json()
        return render_template("player.html", player=player_data)
    else:
        error_message = response.json().get("message", "An error occurred.")
        return render_template("player.html", error=error_message)

if __name__ == "__main__":
    app.run(debug=True)