# Project Management Tool

## Description
A full-stack web application for managing software projects, tasks, and users with roles (Admin, Manager, Developer). This tool allows creation, editing, deletion, and listing of projects, tasks, and users through a RESTful API backend built with Flask and a React-based frontend.

## Features
- User management with roles
- Project CRUD with assignment functionality
- Task CRUD with deadline and status tracking
- Edit and delete operations for users, projects, and tasks
- Clean UI with React hooks and state management
- Backend REST API using Flask and SQLite

## Technologies Used
- Backend: Python 3, Flask, Flask-SQLAlchemy, Flask-CORS, Werkzeug for password hashing
- Frontend: React, Functional Components, Hooks (useState, useEffect)
- Database: SQLite (via SQLAlchemy)
- Tools: Postman for testing APIs, npm, VS Code

## Setup Instructions

### Backend
1. Create and activate a Python virtual environment
2. Install required packages:
  pip install flask flask-sqlalchemy flask-cors werkzeug
3. Run the Flask app:
  python app.py
This starts the backend server at `http://127.0.0.1:5000`

### Frontend
1. Navigate to the frontend directory
2. Install npm dependencies:
  npm install
3. Start the React development server:
  npm start
This runs the frontend on `http://localhost:3000`

## API Endpoints

- **Users**
- `GET /users` - List all users
- `POST /users` - Create user
- `PUT /users/:id` - Update user by ID
- `DELETE /users/:id` - Delete user by ID

- **Projects**
- `GET /projects` - List all projects
- `POST /projects` - Create project

- **Tasks**
- `GET /tasks` - List all tasks
- `POST /tasks` - Create task

## Usage
- Use the UI on `localhost:3000` to create, edit, and delete users, projects, and tasks.
- API can be tested through Postman.

## Assumptions & Notes
- User authentication is optional and not implemented.
- Roles are assigned but no access control enforced.
- Passwords are hashed in backend.
- UI supports editing and deleting users; extend for projects/tasks as needed.

## Author
- Full Name: [UMESH H S]
- Contact: [uhs260066@gmail.com]
