from .db import db

class Post(db.Model):
  __tablename__ = 'posts'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String, nullable=False)
  body = db.Column(db.String)
  def to_json(self, include_comments=False):
    if include_comments:
      return {
        "id": self.id,
        "title": self.title,
        "body": self.body,
        "comments": [c.to_json() for c in self.comments]
      }
    else:
      return {
        "id": self.id,
        "title": self.title,
        "body": self.body,
      }
