from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Route 1: /posts
@app.route('/posts', methods=['GET'])
def get_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json()
    return jsonify(data)

# Route 2: /comments
@app.route('/comments', methods=['GET'])
def get_comments():
    response = requests.get('https://jsonplaceholder.typicode.com/comments')
    data = response.json()
    return jsonify(data)

# Route 3: /albums
@app.route('/albums', methods=['GET'])
def get_albums():
    response = requests.get('https://jsonplaceholder.typicode.com/albums')
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

