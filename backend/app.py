from flask import Flask, jsonify, render_template, request, redirect, url_for
from register import add_user  # Import the add_user function from register.py
from get_users import get_all_users

# Updated template folder path to reflect the 'frontend' folder
app = Flask(__name__, template_folder='./templates')

users = [
    # Sample user (for in-memory persistence)
    # You might want to use a database in the future
]

@app.route('/')
def home():
    # Add a link to the 'add_user_form' page in the template
    return render_template('home.html')

@app.route('/users', methods=['GET'])
def get_users():
    # Fetch all users using the function from get_users.py
    users_list = get_all_users()

    if "error" in users_list:
        return jsonify({"error": users_list["error"]}), 500

    return render_template('users.html', users=users_list)

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        # This is where user data is being captured
        name = request.form.get("name")
        email = request.form.get("email")

        # Check if the user already exists (based on email, or another unique identifier)
        if any(user['email'] == email for user in users):
            return "User already exists!", 400  # You can redirect to a page with an error message

        # Add the user if they don't exist
        users.append({'name': name, 'email': email})
        return redirect(url_for('get_users'))  # Redirect to the user list after successful addition

    return render_template('register.html')  # Display the form if the method is GET

# Endpoint to handle the form submission for adding a user (alternative POST route)
@app.route('/add_user', methods=['POST'])
def add_user_endpoint():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
        email = data['email']

        result = add_user(username, password, email)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/health_check', methods=['GET'])
def health_check():
    return jsonify({"status": "Healthy"}), 200  # A health check endpoint should generally use GET

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
