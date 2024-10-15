# Distributed Computing Project

This project demonstrates a distributed computing system using FastAPI and Pyro4. The project is organized into two main components: a client-server application using FastAPI and a remote object invocation system using Pyro4.

## Project Structure

```
Distributed Computing/
├── client-server/
│   ├── fast-api/
│   │   ├── main.py
│   │   ├── helper_functions/
│   │   │   ├── loadUsers.py
│   │   │   ├── saveUsers.py
│   │   ├── users.json
│   │   ├── README.md
│   ├── Pyro4/
│   │   ├── server.py
│   │   ├── README.md
├── .gitignore
```

### client-server/fast-api/

This directory contains a FastAPI application for managing users.

- **main.py**: The main FastAPI application file. It defines the endpoints for fetching, creating, updating, and deleting users.
- **helper_functions/**: A directory containing helper functions.
    - **loadUsers.py**: Contains the `load_users` function to load users from a JSON file.
    - **saveUsers.py**: Contains the `save_users` function to save users to a JSON file.
- **users.json**: A JSON file containing sample user data.
- **README.md**: Instructions on how to run the FastAPI server and use the endpoints.

### client-server/Pyro4/

This directory contains a Pyro4 server for remote object invocation.

- **server.py**: The main Pyro4 server file. It defines a simple `Calculator` class and starts a Pyro4 daemon.
- **README.md**: Instructions on how to install Pyro4 and run the server and client.

### .gitignore

Specifies files and directories to be ignored by Git.

## Running the FastAPI Server

1. Navigate to the `client-server/fast-api/` directory.
2. Install the required dependencies:
     ```sh
     pip install fastapi uvicorn
     ```
3. Run the server:
     ```sh
     uvicorn main:app --reload
     ```

## Running the Pyro4 Server

1. Navigate to the `client-server/Pyro4/` directory.
2. Install the required dependency:
     ```sh
     pip install pyro4
     ```
3. Run the server:
     ```sh
     python server.py
     ```

## Endpoints for FastAPI

### Fetch All Users

```sh
GET /users
```

### Fetch a Specific User by ID

```sh
GET /users/{user_id}
```

### Add a New User

```sh
POST /users
```

### Update an Existing User by ID

```sh
PUT /users/{user_id}
```

### Delete a User by ID

```sh
DELETE /users/{user_id}
```

## Testing

You can test the FastAPI endpoints using tools like `curl`, `Postman`, or directly through your browser. For Pyro4, follow the instructions in the `client-server/Pyro4/README.md` to run the client and server.
