from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)
API_VERSION = "2.2.0" 

@app.route('/generate-password', methods=['GET'])
def generate_password():
 # Get length from query params (default = 12)
 length = int(request.args.get('length', 12))

 # Allowed characters: letters + digits + special characters
 chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?/"

 # Generate random password
 password = ''.join(random.choice(chars) for _ in range(length))

 return jsonify({"password": password})

# --- New Endpoint 1: Health Check (200 OK) ---
@app.route('/health', methods=['GET'])
def health_check():
    """
    Returns 200 OK to indicate the service is running and responsive.
    Ideal for load balancers and container orchestration platforms.
    """
    return jsonify({
        "status": "UP",
        "message": "Service is healthy and running."
    }), 200

# --- New Endpoint 2: Version Information ---
@app.route('/version', methods=['GET'])
def get_version():
    """
    Returns the currently deployed API version.
    """
    return jsonify({
        "api_name": "Secure Password Generator API",
        "version": API_VERSION,
        "status": "Production Ready"
    }), 200

# --- New Endpoint 3: Help with API usage ---
@app.route('/help', methods=['GET'])
def get_help():
    """
    Returns Help Info.
    """
    return jsonify({
        "/generate-password": "generate random password",
        "/health": "running status of API",
        "/version": "Get version of API",
        "/help": "Get info on available endpoints"
    }), 200

if __name__ == '__main__':
 app.run(debug=True)

