from .db import db

class Topic(db.Model):
  __tablename__ = 'topics'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  posts = db.relationship('Post', secondary="taggings", backref="topics")
  def to_json(self):
    return {
      "id": self.id,
      "name": self.name,
    }
