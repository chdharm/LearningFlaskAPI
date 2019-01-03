from flask import Flask,render_template
app=Flask(__name__)

@app.route("/",methods=["GET"])
def index():
	return "<html><head><title>Hello Page</title></head><body><h1>Hello Body Content</h1></body></html>"

@app.route("/basictem",methods=["GET"])
def index2():
	places=[{'name':'Bangalore'},{'name':'Hyderabad'},{'name':'Mumbai'},{'name':'Pune'},{'name':'Chennai'},{'name':'Kolkata'}]
	user1={'name':'Dharmpal','language':'Python_2','lang':True}
	user2={'name':'Dharmpal','framework':'Flask','lang':False}
	return render_template("flask_template.html", user=user2,items=places)

if __name__=='__main__':
	app.run(debug=True)