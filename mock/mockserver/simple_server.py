from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return "Hello from flask server!"

# /123
@app.route("/<int:integer>")
def simple_route(integer):
    return jsonify({"number": integer})

@app.route("/books")
def books_route():
    list = [{"author": "Romanov А. N.", "year": "1861", "title": "Emancipation reform"}]
    return jsonify({"list": list})

app.run(host="0.0.0.0", port=8080)

# fetch("http://localhost:5000/123").then(response => {
#     response.json().then(json => {
#         console.log(JSON.stringify(json, null, 4));
#     });
# });