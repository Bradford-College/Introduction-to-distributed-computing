Run the server

# FastAPI to simulate client server 

This project demonstrates a simple user management system using FastAPI.

## Installation

To install FastAPI, use the following command:

```sh
pip install fastapi
```

You will also need an ASGI server to run the FastAPI application. Install `uvicorn` using:

```sh
pip install uvicorn
```

## Running the Server

To run the server, use the following command:

```sh
uvicorn main:app --reload
```

## Endpoints

### Fetch All Users

To fetch all users, send a GET request to:

```sh
http://localhost:8000/users
```

### Fetch a Specific User by ID

To fetch a specific user by ID, send a GET request to:

```sh
http://localhost:8000/users/{user_id}
```

Replace `{user_id}` with the actual user ID.

### Add a New User

To add a new user, send a POST request to:

```sh
http://localhost:8000/users
```

Include the user data in the request body as JSON.

### Update an Existing User by ID

To update an existing user by ID, send a PUT request to:

```sh
http://localhost:8000/users/{user_id}
```

Replace `{user_id}` with the actual user ID and include the updated user data in the request body as JSON.

### Delete a User by ID

To delete a user by ID, send a DELETE request to:

```sh
http://localhost:8000/users/{user_id}
```

Replace `{user_id}` with the actual user ID.

## Testing

You can test the endpoints using tools like `curl`, `Postman`, or directly through your browser.

