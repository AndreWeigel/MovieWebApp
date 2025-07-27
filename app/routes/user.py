from flask import Blueprint, render_template, request, redirect, url_for
from app.services.user import UserService

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['GET'])
def index():
    users = UserService.get_users()
    return render_template('index.html', users=users)

@user_routes.route('/create-user', methods=['POST'])
def create_user():
    name = request.form.get('name')
    if name:
        UserService.create_user(name)
    return redirect(url_for('user_routes.index'))

