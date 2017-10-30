# pip install SQLAlchemy  
from flask import Flask,render_template, request, Response,redirect
import json
import redis
from collections import OrderedDict
from datetime import datetime
import os


app = Flask(__name__)
app.debug = True
db = redis.Redis('127.0.0.1')


@app.route('/')
def main():
	return render_template('main.html')

@app.route('/regist')
def regist():
	return render_template('regist.html')	

@app.route('/story1')
def story1():
	name = request.args.get('name','')
	return render_template('story.html', name=name)	
	
@app.route('/story2')
def story2():
	name = request.args.get('name','')
	return render_template('story2.html', name=name)	

@app.route('/story3')
def story3():
	name = request.args.get('name','')
	return render_template('story3.html', name=name)

@app.route('/countdown')
def countdown():
	name = request.args.get('name','')
	return render_template('countdown.html', name=name)		



@app.route('/game')
def index():	
	result = request.args.get('name','')

	return render_template('game.html', result=result)


@app.route('/fin')
def fins():
	context = {}
	
	username = request.args.get('username','')
	range_time = request.args.get('range_time','')
	context["t_min"] = range_time.split(":")[0]
	context["t_sec"] = range_time.split(":")[1]
	
	# Xdata = request.args.get('Xdata')
	# Ydata = request.args.get('Ydata')
	# Xre_data = Xdata.split(",")
	# Yre_data = Ydata.split(",")
	data = request.args.get('detect_range')
	re_data = data.split("|")
	context["len"] = len(re_data[1:])
	collecttion_data = re_data[1:]

	context["datas"] = []
	for each in collecttion_data:
		try:
			context["datas"].append((each.split(',')[1],each.split(',')[2]))
		except:
			pass
	print context["datas"]
	# for each in Xre_data:
	# 	context["datas"].append(
	# 		(each,)
	# 		)

	# for each in Yre_data:
	# 	context["datas"].append(
	# 		(each,)
	# 		)

	# context["Xpath"] = []
	# previ_x = Xre_data[2:][0]
	# for each in Xre_data[2:]:
	# 	context["Xpath"].append([previ_x,each])
	# 	previ_x = each

	# context["Ypath"] = []
	# previ_y = Yre_data[2:][0]
	# for each in Yre_data[2:]:
	# 	context["Ypath"].append([previ_y,each])
	# 	previ_y = each




	filename = 'score.json'
	print "username - "+username
	print "range_time - "+str(range_time)
	if username == ""  or str(range_time) == "":
		
		with open(filename) as f:
			data = json.load(f)
			context["data"] = data
	else:
		
		
		with open(filename , 'r') as f:
			data = json.load(f)
			data["score"].append({ username : range_time })

		os.remove(filename)
		with open(filename, 'w') as f:
			f.write(json.dumps(data, ensure_ascii=True))

			context["data"] = data
	

	return render_template('fin.html', context = context)
	
	



@app.route('/stream', defaults={'path':'stream'}, methods=["PUT"])
@app.route('/game <path:path>', methods=["PUT"])
def inbound(path):
	if request.method == "PUT":
		message = request.json
		db.publish('sub', json.dumps(message))
		return json.dumps(message), 201
	if not db.exists(path):
		return "ERROR"



def event_stream():
	pubsub = db.pubsub()
	pubsub.subscribe('sub')
	for msg in pubsub.listen():
		print msg
		yield u"data: %s\n\n" %msg["data"]



@app.route('/sub')
def stream():
	return Response(event_stream(), mimetype="text/event-stream")





if __name__ == '__main__':
	app.run(threaded=True)
	# app.run(debug=True,port=5000)