#install flask before running it
from flask import Flask,jsonify,request
app=Flask(__name__)
Languages=[{'name':'Java'},{'name':'Python'},{'name':'Ruby'}]

#Easy GET REST API
@app.route('/',methods=['GET'])
def test():
	return jsonify({'message':'it works'})

#REST API for All Language List
@app.route('/lang/',methods=['GET'])
def returnAll():
	return jsonify(Languages)

#REST API for one Language List
@app.route('/lang/<string:name>/',methods=['GET'])
def returnOne(name):
	langs=[language for language in Languages if language['name']==name]
	return jsonify({'Languages':langs[0]})

#Post API
@app.route('/lang',methods=['POST'])
def addOne():
	lang={'name':request.json["name"]}
	Languages.append(lang)
	return jsonify({'languages':Languages})	

#Put API
@app.route('/lang/<string:name>',methods=['PUT'])
def editOne(name):
	langs=[language for language in Languages if language['name']==name]
	langs[0]['name']=request.json['name']
	return jsonify({'language':langs[0]})	

#DELETE API
@app.route('/lang/<string:name>',methods=['DELETE'])
def removeOne(name):
	langs=[language for language in Languages if language['name']==name]
	Languages.remove(langs[0])
	return jsonify({'languages':Languages})

#Running this API
if __name__ == '__main__':
	app.run(debug=True,port=8080)