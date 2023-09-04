from flask import *
from threading import Thread

app = Flask("gdp")

@app.route("/")
def home():
	return "Alive"

def run():
	app.run(host="0.0.0.0", port=8080)

def alivef():
	t = Thread(target=run)
	t.start()