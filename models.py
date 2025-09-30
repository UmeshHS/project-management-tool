from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    role = db.Column(db.String(20))  # 'Admin', 'Manager', 'Developer'
    password = db.Column(db.String(100))

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))
    status = db.Column(db.String(20))  # 'To Do', 'In Progress', 'Done'
    deadline = db.Column(db.String(20))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    assigned_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
