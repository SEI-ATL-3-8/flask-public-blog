import os
from dotenv import load_dotenv
from flask import Flask, request

import models

load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
models.db.init_app(app)

def root():
  return { "message": "ok" }
app.route('/', methods=["GET"])(root)

def posts_index():
  posts = models.Post.query.all()
  return { "posts": [p.to_json() for p in posts] }
app.route('/posts', methods=["GET"])(posts_index)

def posts_create():
  post = models.Post(
    title=request.json["title"],
    body=request.json["body"],
  )

  models.db.session.add(post)
  models.db.session.commit()

  return { "post": post.to_json() }
app.route('/posts', methods=["POST"])(posts_create)

if __name__ == '__main__':
  port = os.environ.get('PORT') or 5000
  app.run(port=port, debug=True)
