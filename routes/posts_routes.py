from controllers import posts_controller

def apply_posts_routes(app):
  app.route('/posts', methods=["GET", "POST"])(posts_controller.all_posts)
  app.route('/posts/<int:id>', methods=["PUT", "GET", "DELETE"])(posts_controller.single_post)
