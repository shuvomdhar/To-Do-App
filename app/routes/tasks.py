from flask import Blueprint, render_template, request, redirect, flash, url_for, session
from app import db
from app.models import Task, User

tasks_bp = Blueprint('tasks', __name__)

def login_required():
    """Check if user is logged in"""
    if 'user_id' not in session:
        return False
    return True

@tasks_bp.route('/tasks')
def view_tasks():
    if not login_required():
        flash('Please login to access your tasks', 'info')
        return redirect(url_for('auth.login'))
    
    # Get tasks for the current user only
    user_id = session['user_id']
    tasks = Task.query.filter_by(user_id=user_id).all()
    username = session.get('username', 'User')
    
    return render_template('tasks.html', tasks=tasks, username=username)

@tasks_bp.route('/add', methods=['POST'])
def add_task():
    if not login_required():
        return redirect(url_for('auth.login'))
    
    title = request.form.get('title')
    if title:
        user_id = session['user_id']
        new_task = Task(title=title, status='Pending', user_id=user_id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully', 'success')
    else:
        flash('Please enter a task title', 'danger')

    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_status(task_id):
    if not login_required():
        return redirect(url_for('auth.login'))
    
    user_id = session['user_id']
    # Only allow users to modify their own tasks
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    
    if task:
        if task.status == 'Pending':
            task.status = 'Working' 
        elif task.status == 'Working':
            task.status = 'Done'
        else:
            task.status = 'Pending'
        db.session.commit()
        flash('Task status updated', 'success')
    else:
        flash('Task not found', 'danger')
    
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/clear', methods=['POST'])
def clear_tasks():
    if not login_required():
        return redirect(url_for('auth.login'))
    
    user_id = session['user_id']
    # Only clear tasks for the current user
    Task.query.filter_by(user_id=user_id).delete()
    db.session.commit()
    flash('All your tasks cleared', 'info')
    return redirect(url_for('tasks.view_tasks'))