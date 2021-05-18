# Public blog... in flask!

### Overview
We will build a flask app that provides a backend for a public blog. We need to satisfy all the following use cases:

| http verb  | route | notes | 
| ------------- | ------------- | --- | 
|GET    | /                              | just says 'ok' |
|GET    | /posts                         | |
|GET    | /posts/:id                     | |
|POST   | /posts                         | |
|PUT    | /posts/:id                     | |
|DELETE | /posts/:id                     | |
|POST   | /posts/:id/comments            | |
|GET    | /posts/:id/comments            | |
|GET    | /topics                        | |
|POST   | /topics                        | |
|PUT    | /topics/:topicId/posts/:postId | associates a post with a topic |
|DELETE | /topics/:topicId/posts/:postId | disassociates a post from a topic |
|GET    | /topics/:id/posts              | |


### Setup
1. Clone down the repo & `cd` into it
1. `python3 -m venv virt-env` to set up a virtual environment folder in this project
1. activate your virtual environment (different commands for mac vs windows). your `pip3 list` should be mostly empty
1. `pip3 install -r requirements.txt`; this is like `npm i` after cloning down an express repo. It downloads everything in `requirements.txt`

### Notes
- simplest possible approach: 1 file for models, all routes in application.py
- trailing slashes matter on your routes!
- `to_json` & `__repr__`
- if you define the belongsTo / hasMany on both ends, you get a warning that you're supposed to use backref instead. backref successfully defines the inverse
- building a m-t-m: need a table, a class w/ 2 ForeignKey declarations, and a secondary
- decorators
- multiple methods in a single route
