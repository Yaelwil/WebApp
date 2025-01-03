from flask import Flask, jsonify
from register import register_user  # Import the register function from register.py
from all_users import get_all_users

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_root_post():
    return jsonify({"message": "OK"}), 200

@app.route('/users', methods=['GET'])
def get_users():
    # Fetch all users using the function defined in all_users.py
    users_list = get_all_users()

    if "error" in users_list:
        return jsonify({"error": users_list["error"]}), 500

    # Return the user data as a JSON response
    return jsonify(users_list), 200

@app.route('/register', methods=['Post'])
def register():
    return register_user()

@app.route('/health_check', methods=['GET'])
def health_check():
    return jsonify({"status": "Healthy"}), 200  # A health check endpoint should generally use GET

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
