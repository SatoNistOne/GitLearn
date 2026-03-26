import os
from flask import Flask
from flask_login import LoginManager
from config import Config
from app.models import db

def create_app():
    app = Flask(
        __name__,
        template_folder='../templates',
        static_folder='../static'
    )
    app.config.from_object(Config)
    app.config['JSON_AS_ASCII'] = False
    app.jinja_env.ensure_ascii = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()
        init_lessons()

    from app.routes import main
    app.register_blueprint(main)

    return app

def init_lessons():
    from app.models import Lesson, db
    from app.lessons import LESSONS_DATA

    existing = Lesson.query.count()
    if existing == 0:
        for lesson_data in LESSONS_DATA:
            lesson = Lesson(
                title=lesson_data['title'],
                slug=lesson_data['slug'],
                content=lesson_data['content'],
                order=lesson_data['order'],
                interactive_task=lesson_data.get('interactive_task'),
                expected_output=lesson_data.get('expected_output')
            )
            db.session.add(lesson)
        db.session.commit()
