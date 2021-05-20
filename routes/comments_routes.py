# how we're able to import controllers is related to how we structured controllers/__init__.py
# because there's nothing in that file, we can import a specific file from the controllers module. but if we had simply
# import controllers
# we couldn't then access controllers.comments_controller
# if we wanted to import controllers and then access controllers.comments_controller, we would need controllers/__init__.py to have contain:
# from . import comments_controller

from controllers import comments_controller

def apply_comments_routes(app):
  app.route('/posts/<int:id>/comments', methods=["POST"])(comments_controller.single_post_comments)
  
