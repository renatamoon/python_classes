from flask import Flask, jsonify, abort
from db import fetch_blogs, fetch_blog

app = Flask(__name__)

@app.route("/")
def main_page():
    message = "This is my new application"
    return message

@app.route("/blogs")
def all_blogs():
    blogs = jsonify(fetch_blogs())
    return blogs

@app.route("/blogs/<id>")


app.run()