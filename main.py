from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

@app.route('/')
def root():
    return 'Hola Mundo'

@app.route("/users/<user_id>")
def get_user(user_id):
    user = {'id': user_id, 'name': 'Nayid', 'phone': '12345'}

    query = request.args.get('query')
    if query:
        user['query'] = query
    
    return jsonify(user), 200

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201

if __name__ in "__main__":
    app.run(debug=True)