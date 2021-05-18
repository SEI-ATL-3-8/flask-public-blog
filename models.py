from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Post(db.Model):
  __tablename__ = 'posts'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String, nullable=False)
  body = db.Column(db.String)
  # TODO: hasMany comments
  def to_json(self):
    return {
      "id": self.id,
      "title": self.title,
      "body": self.body,
    }

class Comment(db.Model):
  __tablename__ = 'comments'
  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.String)
  # TODO: declare foreign key
  post_id = db.Column(db.Integer)

class Topic(db.Model):
  __tablename__ = 'topics'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)

class Tagging(db.Model):
  __tablename__ = 'taggings'
  id = db.Column(db.Integer, primary_key=True)
  # TODO: foreign key
  post_id = db.Column(db.Integer)
  topic_id = db.Column(db.Integer)

