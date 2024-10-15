'''
Instructions for Students:
1. Identify the Issues: Review the provided script and identify the errors mentioned above.
2. Fix the Problems: Update the script to correct the errors, ensuring that each function behaves as expected.
3. Test the Functions: After making changes, run the script to ensure it works correctly, adding a user, retrieving a user by ID, and deleting a user.

Expected Fixes:
1. Correct the variable name in the add_user function.
2. Change the assignment operator to the equality operator in the get_user function.
3. Implement a check in the delete_user function to handle non-existent user IDs.
4. Consider reducing reliance on the global variable by passing users as a parameter, or organizing the code differently.
'''

# Sample list of users
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

# Function to add a new user
def add_user(name):
    new_user = {"id": len(users) + 1, "name": name}
    users.append(new_user)  # Error: Not using the correct variable name for list

# Function to get user by ID
def get_user(user_id):
    for user in users:  # Error: Incorrect comparison, should use `==`
        if user["id"] = user_id:  # Error: Use of assignment operator instead of equality operator
            return user
    return "User not found"

# Function to delete a user by ID
def delete_user(user_id):
    global users  # Error: Using global variable
    users = [user for user in users if user["id"] != user_id]  # Error: No handling if user_id doesn't exist

# Test the functions
add_user("David")
print(get_user(2))
delete_user(1)
print(users)
