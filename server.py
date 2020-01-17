from flask import Flask, request, Response, render_template
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
import db_accessor
from flask_cors import CORS

#db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)
CORS(app)
# class Employees(Resource):
#     def get(self):
#         conn = db_connect.connect() # connect to database
#         query = conn.execute("select * from employees") # This line performs query and returns json result
#         return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

# class Tracks(Resource):
#     def get(self):
#         conn = db_connect.connect()
#         query = conn.execute("select trackid, name, composer, unitprice from tracks;")
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return jsonify(result)

# class Employees_Name(Resource):
#     def get(self, employee_id):
#         conn = db_connect.connect()
#         query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return jsonify(result)
@app.route('/', methods=['GET', 'POST'])

class All_Data(Resource):
    def get(self):
        results = db_accessor.select_all()
        return jsonify(results)

class Add_Session(Resource):
	def post(self):
		# import pdb; pdb.set_trace();
		buyin = float(request.json['buyin'])
		cashout = float(request.json['cashout'])
		location = request.json['location']
		bigblind = float(request.json['bigblind'])
		littleblind = float(request.json['littleblind'])	
		startime = request.json['startime']
		endtime = request.json['endtime']
		
		results = db_accessor.insert_row(buyin,cashout,location,bigblind,littleblind,startime,endtime)
		return jsonify(results)

api.add_resource(All_Data, '/all') # Route_1
api.add_resource(Add_Session, '/addSession') # Route_2
# api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(port='5002')
     