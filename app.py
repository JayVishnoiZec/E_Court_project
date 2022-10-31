from flask import Flask
from flask_restful import Resource, Api
# from h11 import RemoteProtocolError

app = Flask(__name__)
api = Api(app)


class Help(Resource):
    def get(self):
        help = {"available REST APIAs are :"["/ping", "/info"]}
        return help


class Ping(Resource):
    def get(self):
        status = {"status": "Alive"}
        return status


class Employee(Resource):
    def get(self):

        employee_info = {
            "emp1": {
                "name": "jay",
                "salary": "8k",
                "company": "zecdata pvt."
            },
            "emp2": {
                "name": "keshav",
                "salary": "*k",
                "company": "zec"
            }}

        return employee_info


api.add_resource(Help, "/")
api.add_resource(Ping, "/ping")
api.add_resource(Employee, "/info")
#### how to create api which accepts perameters in python flask
# if __name__ == "__main__":
app.run(debug=True, port=5000, host="localhost")
