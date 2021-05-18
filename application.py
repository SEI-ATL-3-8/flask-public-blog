import os
from dotenv import load_dotenv
from flask import Flask, request
import sqlalchemy

import models

load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
models.db.init_app(app)

def root():
  return { "message": "ok" }
app.route('/', methods=["GET"])(root)

def all_posts():
  if request.method == 'GET':
    posts = models.Post.query.all()
    return { "posts": [p.to_json() for p in posts] }
  elif request.method == 'POST':
    post = models.Post(
      title=request.json["title"],
      body=request.json["body"],
    )
    models.db.session.add(post)
    models.db.session.commit()
    return { "post": post.to_json() }
app.route('/posts', methods=["GET", "POST"])(all_posts)

def single_post(id):
  post = models.Post.query.filter_by(id=id).first()
  if post == None:
    return { "message": "post not found" }, 404
  
  if request.method == 'GET':
    return { "post": post.to_json(include_comments=True) }
  elif request.method == 'PUT':
    post.title = request.json["title"]
    post.body = request.json["body"]
    models.db.session.add(post)
    models.db.session.commit()
    return { "post": post.to_json() }
  elif request.method == 'DELETE':
    models.db.session.delete(post)
    models.db.session.commit()
    return { "post": post.to_json() }
app.route('/posts/<int:id>', methods=["PUT", "GET", "DELETE"])(single_post)

def single_post_comments(id):
  post = models.Post.query.filter_by(id=id).first()
  comment = models.Comment(body=request.json["body"])
  post.comments.append(comment)
  models.db.session.add(post)
  models.db.session.add(comment)
  models.db.session.commit()
  return {
    "post": post.to_json(),
    "comment": comment.to_json()
  }
app.route('/posts/<int:id>/comments', methods=["POST"])(single_post_comments)

def all_topics():
  if request.method == 'GET':
    topics = models.Topic.query.all()
    return { "topics": [t.to_json() for t in topics] }
  elif request.method == 'POST':
    topic = models.Topic(name=request.json["name"])
    models.db.session.add(topic)
    models.db.session.commit()
    return { "topic": topic.to_json() }
app.route('/topics', methods=["GET", "POST"])(all_topics)

def single_topic_single_post(topic_id, post_id):
  post = models.Post.query.filter_by(id=post_id).first()
  topic = models.Topic.query.filter_by(id=topic_id).first()
  if request.method == "PUT":
    post.topics.append(topic)
  elif request.method == "DELETE":
    post.topics.remove(topic)
  models.db.session.add(post)
  models.db.session.commit()
  return {
    "topic": topic.to_json(),
    "post": post.to_json()
  }
app.route('/topics/<int:topic_id>/posts/<int:post_id>', methods=["PUT", "DELETE"])(single_topic_single_post)


def single_topic_all_posts(id):
  topic = models.Topic.query.filter_by(id=id).first()
  posts = topic.posts
  return {
    "topic": topic.to_json(),
    "posts": [p.to_json() for p in posts]
  }
app.route('/topics/<int:id>/posts', methods=["GET"])(single_topic_all_posts)



if __name__ == '__main__':
  port = os.environ.get('PORT') or 5000
  app.run(port=port, debug=True)
