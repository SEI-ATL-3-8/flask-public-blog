from flask import request
import models

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