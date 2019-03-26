from db import visit_db
from flask_restful import Resource


class Visit(Resource):
    @staticmethod
    def get():
        current_user = visit_db.get_user_num() + 1
        visit_db.update_user_num(current_user)

        return f'Hello, user {current_user}'
