from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

@app.route('/generate-password', methods=['GET'])
def generate_password():
 # Get length from query params (default = 12)
 length = int(request.args.get('length', 12))

 # Allowed characters: letters + digits + special characters
 chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?/"

 # Generate random password
 password = ''.join(random.choice(chars) for _ in range(length))

 return jsonify({"password": password})

if __name__ == '__main__':
 app.run(debug=True)

