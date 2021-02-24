from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from scipy import interpolate
import numpy as np
import pandas as pd
app = Flask(__name__)
api = Api(app)

class ModelInterpolate (Resource):
  	def post(self):
  			request_data = request.get_json()
  			test = self.handle_request_data(request_data)
  			return test

  	def handle_request_data(self, data):
  			x_points = [42384,42415,42444,42475,42505,42536,42566,42597,42628,42658,42689,42719]
  			y_min_points = data["y_min_points"]
  			y_opt_points = data["y_opt_points"]
  			y_max_points = data["y_max_points"]
  			date = np.empty(366, dtype=object) 
  			min = np.empty(366, dtype=object) 
  			opt = np.empty(366, dtype=object) 
  			max = np.empty(366, dtype=object) 
  			i = 42370 
  			j = 0 
  			while i < 42736:
  					date[j] = i
  					min[j] = (self.interpolate(x_points, y_min_points,i)).item()
  					opt[j] = (self.interpolate(x_points, y_opt_points,i)).item()
  					max[j] = (self.interpolate(x_points, y_max_points,i)).item()
  					i += 1
  					j += 1
  			return {"min": min.tolist(), "opt": opt.tolist(), "max": max.tolist()}


  	def interpolate (self, x_points, y_points, x):
  			tck = interpolate.splrep(x_points, y_points)
  			return interpolate.splev(x, tck)


api.add_resource(ModelInterpolate, "/interpolate")

if __name__ == "__main__":
	app.run(debug=True)