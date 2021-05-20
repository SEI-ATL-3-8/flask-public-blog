# each folder forms an importable module in pythoh
# when you import a module, python looks for a file called __init__.py in that folder and runs it.
# use a file like this to package up the contents of the module in a tidy way

from .comments_routes import apply_comments_routes
from .posts_routes import apply_posts_routes
from .topics_routes import apply_topics_routes

# this is a function that takes in an app object
# we import this function in application.py and invoke it, passing it our app object
def apply_routes(app):
  apply_comments_routes(app)
  apply_posts_routes(app)
  apply_topics_routes(app)

# there is another way to do routing: instead of defining a function / importing that function into application.py / invoking it there, import the app object into this file:

# from application import app
# apply_comments_routes(app)

# however this creates a circular import reference: app is importing routes, but routes is also importing app.
# this doesn't create an infinite loop (python is able to handle circular imports just fine) and will work in our case
# but it is a bad habit to get into, and you should be aware of circular imports as an anti-pattern in general
# https://stackabuse.com/python-circular-imports/