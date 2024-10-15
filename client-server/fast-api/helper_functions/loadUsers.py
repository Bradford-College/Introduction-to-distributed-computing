import json
from typing import List, Dict

# Helper function to load users
def load_users() -> List[Dict]:
    with open("users.json", "r") as f:
        return json.load(f)