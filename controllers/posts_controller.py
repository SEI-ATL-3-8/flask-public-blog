from flask import request
import models

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
