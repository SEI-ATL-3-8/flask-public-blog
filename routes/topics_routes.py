from controllers import topics_controller

def apply_topics_routes(app):
  app.route('/topics', methods=["GET", "POST"])(topics_controller.all_topics)
  app.route('/topics/<int:topic_id>/posts/<int:post_id>', methods=["PUT", "DELETE"])(topics_controller.single_topic_single_post)
  app.route('/topics/<int:id>/posts', methods=["GET"])(topics_controller.single_topic_all_posts)

