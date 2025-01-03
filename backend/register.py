from pymongo import MongoClient
import uuid

# MongoDB Connection
MONGO_URI = "mongodb://mongodb_primary:27017/?directConnection=true"
client = MongoClient(MONGO_URI)
db = client['polybot']  # Name of the database
users_collection = db['users']  # Name of the collection

def add_user(username, password, email):
    """
    Add a new user to the MongoDB collection with a unique user_id.
    """
    try:
        if not username or not password or not email:
            raise ValueError("Missing required fields: username, password, or email")

        # Generate a unique user_id
        user_id = str(uuid.uuid4())

        # Insert user into MongoDB
        result = users_collection.insert_one({
            'user_id': user_id,
            'username': username,
            'password': password,  # In production, hash this!
            'email': email
        })

        # Ensure the user_id was properly inserted
        inserted_user = users_collection.find_one({"user_id": user_id})

        if inserted_user:
            return {"message": "User added successfully", "user_id": inserted_user['user_id']}
        else:
            raise Exception("Failed to insert user")

    except Exception as e:
        return {"error": str(e)}
