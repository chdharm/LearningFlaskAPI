from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
	try:
		dividebyzero=10/0
		return "Hello World"
	except Exception:
		return "Exception"
if __name__=='__main__':
	app.run()
	#app.run(debug=True)