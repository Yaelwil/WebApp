from pymongo import MongoClient
import uuid

# MongoDB Connection
MONGO_URI = "mongodb://mongodb_primary:27017"
client = MongoClient(MONGO_URI)
db = client['polybot']  # Name of the database
users_collection = db['users']  # Name of the collection


def get_all_users():
    """
    Retrieve all users from the MongoDB collection.
    """
    try:
        # Fetch all users from the MongoDB collection
        users = users_collection.find()

        # Convert the MongoDB cursor to a list of dictionaries
        users_list = []
        for user in users:
            user_data = {
                'user_id': user.get('user_id'),
                'username': user.get('username'),
                'email': user.get('email'),
            }
            users_list.append(user_data)

        return users_list

    except Exception as e:
        return {"error": str(e)}