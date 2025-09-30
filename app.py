from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Project, Task

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({'message': 'Email already registered'}), 409
    hashed_password = generate_password_hash(data['password'])
    new_user = User(name=data['name'], email=data['email'], role=data['role'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201

@app.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    result = [{'id': u.id, 'name': u.name, 'email': u.email, 'role': u.role} for u in users]
    return jsonify(result)

@app.route('/projects', methods=['POST'])
def create_project():
    data = request.json
    project = Project(name=data['name'], description=data['description'])
    db.session.add(project)
    db.session.commit()
    return jsonify({'message': 'Project created'}), 201

@app.route('/projects', methods=['GET'])
def list_projects():
    projects = Project.query.all()
    result = [{'id': p.id, 'name': p.name, 'description': p.description} for p in projects]
    return jsonify(result)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = Task(title=data['title'], description=data['description'], status='To Do',
                deadline=data['deadline'], project_id=data['project_id'], assigned_user_id=data['assigned_user_id'])
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Task created'}), 201

@app.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = Task.query.all()
    result = [{'id': t.id, 'title': t.title, 'status': t.status, 'deadline': t.deadline,
               'project_id': t.project_id, 'assigned_user_id': t.assigned_user_id} for t in tasks]
    return jsonify(result)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = User.query.get_or_404(user_id)
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.role = data.get('role', user.role)
    # Only update password if provided
    if 'password' in data and data['password']:
        user.password = generate_password_hash(data['password'])
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.json
    project = Project.query.get_or_404(project_id)
    project.name = data.get('name', project.name)
    project.description = data.get('description', project.description)
    db.session.commit()
    return jsonify({'message': 'Project updated successfully'})


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    task = Task.query.get_or_404(task_id)
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.status = data.get('status', task.status)
    task.deadline = data.get('deadline', task.deadline)
    task.project_id = data.get('project_id', task.project_id)
    task.assigned_user_id = data.get('assigned_user_id', task.assigned_user_id)
    db.session.commit()
    return jsonify({'message': 'Task updated successfully'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted successfully'})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'})

@app.route('/')
def home():
    return "API is running"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
