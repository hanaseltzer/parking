from flask import Flask, render_template, request, jsonify
from db_querys.user import get_users
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
# Define a route for the root URL
@app.route('/')
def home():
    return "Hello, World!"

# Define a route for a page with dynamic content
@app.route('/get_users_data')
def get_users_data():
    users = get_users()
    return json.dumps(users)

# Define a route to handle form submissions (POST request)
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['data']
    return jsonify({'received_data': data})


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)