from flask import request, jsonify
from pymongo import MongoClient
import bcrypt
import logging

# MongoDB URI and Database Setup
MONGO_URI = "mongodb://mongodb_primary:27017"  # Change this if you're using a remote DB
client = MongoClient(MONGO_URI)
db = client['polybot']  # Name of the database
users_collection = db['users']  # Name of the collection

# Setting up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Debug: Register user function initialized.")

def register_user():
    data = request.get_json()

    # Check if all required fields are provided
    if not all(key in data for key in ['username', 'email', 'password']):
        return jsonify({"error": "Missing required fields"}), 400

    # Check if the user already exists
    existing_user = users_collection.find_one({"email": data['email']})
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    # Hash the password
    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

    # Create a new user document
    new_user = {
        "username": data['username'],
        "email": data['email'],
        "password": hashed_password.decode('utf-8')  # Store the hashed password as a string
    }

    # Insert the new user into the MongoDB collection
    try:
        result = users_collection.insert_one(new_user)
        logger.info(f"User registered with ID: {str(result.inserted_id)}")
    except Exception as e:
        logger.error(f"Error inserting user: {str(e)}")
        return jsonify({"error": "Error registering user"}), 500

    # Return the success response
    return jsonify({"message": "User registered successfully", "user_id": str(result.inserted_id)}), 201
