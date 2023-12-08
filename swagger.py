from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

# Your Flask routes
@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    """
    This is an example endpoint that returns a greeting.
    ---
    parameters:
      - name: name
        in: path
        type: string
        required: true
        description: The name for the greeting.
    responses:
      200:
        description: A greeting message.
    """
    greeting = f"Hello syed Hanan, {name}!"
    return jsonify({'message': greeting})

if __name__ == '__main__':
    app.run(debug=True)
