from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from scipy import interpolate
app = Flask(__name__)
api = Api(app)

class ModelInterpolate (Resource):
  	def post(self):
  			test = self.handle_request_data(request.data)
  			return test

  	def handle_request_data(self, data):
  			x_points = [42384,42415,42444,42475,42505,42536,42566,42597,42628,42658,42689,42719]
  			return {"data": "from handle request data"}


  	def interpolate (self, x_points, y_points, x):
  			tck = interpolate.splrep(x_points, y_points)
  			return interpolate.splev(x, tck)


api.add_resource(ModelInterpolate, "/interpolate")

if __name__ == "__main__":
	app.run(debug=True)