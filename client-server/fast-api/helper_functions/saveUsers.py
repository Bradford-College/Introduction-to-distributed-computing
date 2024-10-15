import json
from typing import List, Dict

# Helper function to save users
def save_users(users: List[Dict]):
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)