from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_cors import CORS, cross_origin
from scipy import interpolate
import numpy as np
import pandas as pd
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

class ModelInterpolate (Resource):
  	@cross_origin()
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
  					min[j] = float("{:.2f}".format((self.interpolate(x_points, y_min_points,i)).item()))
  					opt[j] = float("{:.2f}".format((self.interpolate(x_points, y_opt_points,i)).item()))
  					max[j] = float("{:.2f}".format((self.interpolate(x_points, y_max_points,i)).item()))
  					i += 1
  					j += 1
  			return {"min": min.tolist(), "opt": opt.tolist(), "max": max.tolist()}


  	def interpolate (self, x_points, y_points, x):
  			tck = interpolate.splrep(x_points, y_points)
  			return interpolate.splev(x, tck)

class WeirLevelInterpolate (Resource):
  	@cross_origin()
  	def get(self):
  			request_data = request.get_json()
  			x_points = [512,512.125,512.25,512.375,512.5,512.625,512.75,512.875,513,513.125,513.25,513.375,513.5,513.625,513.75,513.875,514,514.125,514.25,514.375,514.5,514.625,514.75,514.875,515,515.125,515.25,515.375,515.5,515.625,515.75,515.875,516,516.125,516.25,516.375,516.5,516.625,516.75,516.875,517,517.125,517.25,517.375,517.5,517.625,517.75,517.875,518,518.125,518.25,518.375]
  			y_points = [175000,180000,188000,190000,200000,205000,213000,219000,227395,238000,244000,250000,263000,275000,288000,300000,306093,325000,338000,350000,356000,381000,398000,400000,415352,438000,450000,468000,475000,507000,525000,538000,552853,580000,600000,613000,625000,663000,675000,694000,711039,744000,763000,775000,800000,834000,850000,875000,890193,913000,950000,969000]
  			level = request_data["level"]
  			volume = float("{:.2f}".format((self.interpolate(x_points, y_points,level)).item()))
  			return {"volume" : volume}
  	def interpolate (self, x_points, y_points, x):
  			tck = interpolate.splrep(x_points, y_points)
  			return interpolate.splev(x, tck)

class WeirVolumeInterpolate (Resource):
  	@cross_origin()
  	def get(self):
  			request_data = request.get_json()
  			y_points = [512,512.125,512.25,512.375,512.5,512.625,512.75,512.875,513,513.125,513.25,513.375,513.5,513.625,513.75,513.875,514,514.125,514.25,514.375,514.5,514.625,514.75,514.875,515,515.125,515.25,515.375,515.5,515.625,515.75,515.875,516,516.125,516.25,516.375,516.5,516.625,516.75,516.875,517,517.125,517.25,517.375,517.5,517.625,517.75,517.875,518,518.125,518.25,518.375]
  			x_points = [175000,180000,188000,190000,200000,205000,213000,219000,227395,238000,244000,250000,263000,275000,288000,300000,306093,325000,338000,350000,356000,381000,398000,400000,415352,438000,450000,468000,475000,507000,525000,538000,552853,580000,600000,613000,625000,663000,675000,694000,711039,744000,763000,775000,800000,834000,850000,875000,890193,913000,950000,969000]
  			volume = request_data["volume"]
  			level = float("{:.2f}".format((self.interpolate(x_points, y_points,volume)).item()))
  			return {"level" : level}
  	def interpolate (self, x_points, y_points, x):
  			tck = interpolate.splrep(x_points, y_points)
  			return interpolate.splev(x, tck)

class LuphohloLevelInterpolate (Resource):
  	@cross_origin()
  	def get(self):
  			request_data = request.get_json()
  			x_points = [984,984.4,985,985.4,986,986.4,987,987.4,988,988.4,989,989.4,990,990.4,991,991.4,992,992.4,993,993.4,994,994.4,995,995.4,996,996.4,997,997.4,998,998.4,999,999.4,1000,1000.4,1001,1001.4,1002,1002.4,1003,1003.4,1004,1004.4,1005,1005.4,1006,1006.4,1007,1007.4,1008,1008.4,1009,1009.4,1010,1010.4,1011,1011.4,1012,1012.4,1013,1013.4,1014,1014.4,1015,1015.6,1016]
  			y_points = [200000,300000,400000,450000,500000,600000,700000,800000,850000,900000,950000,970000,1000000,1100000,1300000,1500000,1700000,1900000,1990000,2000000,2200000,2400000,2500000,2900000,3000000,3400000,3600000,3800000,4000000,4200000,4500000,4700000,5000000,5500000,5700000,6200000,6500000,7000000,7200000,8000000,8200000,9000000,9200000,10000000,10200000,10600000,11900000,12000000,13000000,13200000,14000000,14500000,15000000,15500000,16000000,17000000,18000000,18000000,19000000,20000000,20500000,21240000,22000000,23600000,23690000]
  			level = request_data["level"]
  			volume = float("{:.2f}".format((self.interpolate(x_points, y_points,level)).item()))
  			return {"volume" : volume}
  	def interpolate (self, x_points, y_points, x):
  			tck = interpolate.splrep(x_points, y_points)
  			return interpolate.splev(x, tck)

class LuphohloVolumeInterpolate (Resource):
  	@cross_origin()
  	def get(self):
  			request_data = request.get_json()
  			y_points = [984,984.4,985,985.4,986,986.4,987,987.4,988,988.4,989,989.4,990,990.4,991,991.4,992,992.4,993,993.4,994,994.4,995,995.4,996,996.4,997,997.4,998,998.4,999,999.4,1000,1000.4,1001,1001.4,1002,1002.4,1003,1003.4,1004,1004.4,1005,1005.4,1006,1006.4,1007,1007.4,1008,1008.4,1009,1009.4,1010,1010.4,1011,1011.4,1012,1012.2,1013,1013.4,1014,1014.4,1015,1015.6,1016]
  			x_points = [200000,300000,400000,450000,500000,600000,700000,800000,850000,900000,950000,970000,1000000,1100000,1300000,1500000,1700000,1900000,1990000,2000000,2200000,2400000,2500000,2900000,3000000,3400000,3600000,3800000,4000000,4200000,4500000,4700000,5000000,5500000,5700000,6200000,6500000,7000000,7200000,8000000,8200000,9000000,9200000,10000000,10200000,10600000,11900000,12000000,13000000,13200000,14000000,14500000,15000000,15500000,16000000,17000000,17500000,18000000,19000000,20000000,20500000,21240000,22000000,23600000,23690000]
  			volume = request_data["volume"]
  			level = float("{:.2f}".format((self.interpolate(x_points, y_points,volume)).item()))
  			return {"level" : level}
  	def interpolate (self, x_points, y_points, x):
  			tck = interpolate.splrep(x_points, y_points)
  			return interpolate.splev(x, tck)

api.add_resource(WeirLevelInterpolate, "/weir-level-interpolate")
api.add_resource(WeirVolumeInterpolate, "/weir-volume-interpolate")
api.add_resource(LuphohloLevelInterpolate, "/luphohlo-level-interpolate")
api.add_resource(LuphohloVolumeInterpolate, "/luphohlo-volume-interpolate")
api.add_resource(ModelInterpolate, "/interpolate")

if __name__ == "__main__":
	app.run(debug=True)