from .db import db

class Comment(db.Model):
  __tablename__ = 'comments'
  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.String)
  post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
  post = db.relationship('Post', backref='comments')
  def to_json(self):
    return {
      "id": self.id,
      "body": self.body,
      "post_id": self.post_id
    }
