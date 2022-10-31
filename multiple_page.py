# import json
# from unittest import result
# source env/bin/activate


from flask import Flask
from flask import json
from flask import jsonify
# from controller
from controller.user_controller import func
# python3 -m venv env
# from requests import request

# return jsonify({"jay age": jay,
#                     "shubham age": shubham,
#                     "dishant age ": dishant, })
a,b,c = func()

print(a,b,c)





# app = Flask(__name__)


# @app.route("/")
# def welcome():
#     # return "Hello World"
#     return jsonify({"about" :'Hello, World!'})



# @app.route("/home")
# def home():
#     return "This is home page"

# # import controller.user_controller

# from controller import user_controller


# if __name__ == "__main__":
#     app.run(debug=True)
