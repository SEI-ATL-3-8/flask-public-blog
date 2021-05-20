from flask import request
import models

def all_topics():
  if request.method == 'GET':
    topics = models.Topic.query.all()
    return { "topics": [t.to_json() for t in topics] }
  elif request.method == 'POST':
    topic = models.Topic(name=request.json["name"])
    models.db.session.add(topic)
    models.db.session.commit()
    return { "topic": topic.to_json() }

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


def single_topic_all_posts(id):
  topic = models.Topic.query.filter_by(id=id).first()
  posts = topic.posts
  return {
    "topic": topic.to_json(),
    "posts": [p.to_json() for p in posts]
  }
