from .db import db

class Tagging(db.Model):
  __tablename__ = 'taggings'
  id = db.Column(db.Integer, primary_key=True)
  post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
  topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
