from app.models import db
from app.models.user import User
from sqlalchemy.exc import SQLAlchemyError


class UserService:
    @staticmethod
    def create_user(name):
        try:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()
            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Error creating user: {e}")

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_users():
        return User.query.all()

    @staticmethod
    def update_user(user_id, name=None):
        user = User.query.get(user_id)
        if not user:
            return None
        if name:
            user.name = name
        try:
            db.session.commit()
            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Error updating user: {e}")

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return False
        try:
            db.session.delete(user)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Error deleting user: {e}")
