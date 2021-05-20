from .db import db
from .Post import Post
from .Comment import Comment
from .Topic import Topic
from .Tagging import Tagging

# when you import models, this file is all that python sees from the folder
# so this file is used to package up the whole folder
# ie anything that we want to be accessible via models.whatever needs to be imported into this file
