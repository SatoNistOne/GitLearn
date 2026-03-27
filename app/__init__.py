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

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

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
    from app.models import Lesson, LessonStep, Hint, QuizQuestion, QuizAnswer, db
    from app.lessons import LESSONS_DATA

    existing = Lesson.query.count()
    if existing == 0:
        for lesson_data in LESSONS_DATA:
            lesson = Lesson(
                title=lesson_data['title'],
                slug=lesson_data['slug'],
                description=lesson_data.get('description', ''),
                order=lesson_data['order']
            )
            db.session.add(lesson)
            db.session.flush()

            for step_data in lesson_data.get('steps', []):
                step = LessonStep(
                    lesson_id=lesson.id,
                    title=step_data['title'],
                    content=step_data['content'],
                    step_type=step_data['step_type'],
                    order=step_data['order'],
                    is_interactive=step_data.get('is_interactive', False),
                    expected_command=step_data.get('expected_command')
                )
                db.session.add(step)

            for hint_data in lesson_data.get('hints', []):
                hint = Hint(
                    lesson_id=lesson.id,
                    step_id=hint_data.get('step_id'),
                    content=hint_data['content'],
                    hint_order=hint_data.get('hint_order', 1)
                )
                db.session.add(hint)

            for quiz_data in lesson_data.get('quiz_questions', []):
                question = QuizQuestion(
                    lesson_id=lesson.id,
                    question_text=quiz_data['question_text'],
                    points=quiz_data.get('points', 10),
                    order=quiz_data['order']
                )
                db.session.add(question)
                db.session.flush()

                for answer_data in quiz_data.get('answers', []):
                    answer = QuizAnswer(
                        question_id=question.id,
                        answer_text=answer_data['answer_text'],
                        is_correct=answer_data['is_correct']
                    )
                    db.session.add(answer)

        db.session.commit()
