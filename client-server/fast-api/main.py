from fastapi import FastAPI, HTTPException
import json
from typing import List, Dict

# Import helper functions
from helper_functions.loadUsers import load_users
from helper_functions.saveUsers import save_users

#Create an Instance of the fastAPI class
app = FastAPI()

# Fetch all users
@app.get("/users")
def get_users():
    users = load_users()
    return {"users": users}

# Fetch a specific user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    users = load_users()
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}

# Add a new user
@app.post("/users")
def create_user(user: Dict):
    users = load_users()
    new_id = max([u["id"] for u in users]) + 1
    user["id"] = new_id
    users.append(user)
    save_users(users)
    return {"message": "User created successfully", "user": user}

# Update an existing user by ID
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: Dict):
    users = load_users()
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.update(updated_user)
    save_users(users)
    return {"message": "User updated successfully", "user": user}

# Delete a user by ID
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    users = load_users()
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    users.remove(user)
    save_users(users)
    return {"message": "User deleted successfully"}

