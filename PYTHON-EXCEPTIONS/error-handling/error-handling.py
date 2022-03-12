import json
from flask import Flask, jsonify, abort
from db import fetch_blogs, fetch_blog, NotFoundError, NotAuthorizedError

app = Flask(__name__)

@app.route("/")
def main_page():
    message = "This is my new application"
    return message

@app.route("/blogs")
def all_blogs():
    # jsonify - allows the app to transform the data to json
    blogs = jsonify(fetch_blogs())
    return blogs

@app.route("/blogs/<id>")
def get_blog(id):
    try:
        blog = jsonify(fetch_blog(id))
        return blog
    except NotFoundError:
        abort(404, description="Resource not found")
    except NotAuthorizedError:
        abort(403, description="Access denied")
app.run()
