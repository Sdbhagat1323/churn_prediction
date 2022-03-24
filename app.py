from flask import Flask, jsonify

app = Flask(__name__)

data = {"user":"swapnil",
"mobile":"8999543199"}

@app.route("/")
def hemo():
    data = {"user":"swapnil",
		"password": "xyz"}
	
    return jsonify({"data":data})

if __name__ == "__main__":
	app.run(debug= True)
