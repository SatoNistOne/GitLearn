from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(128), unique=True, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login_at = db.Column(db.DateTime)
    total_experience = db.Column(db.Integer, default=0)
    streak_days = db.Column(db.Integer, default=0)
    max_streak_days = db.Column(db.Integer, default=0)
    last_activity_date = db.Column(db.Date)
    level = db.Column(db.Integer, default=1)
    progress = db.relationship('UserProgress', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    attempts = db.relationship('Attempt', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    quiz_attempts = db.relationship('QuizAttempt', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    action_logs = db.relationship('UserActionLog', backref='user', lazy='dynamic', cascade='all, delete-orphan')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    slug = db.Column(db.String(128), unique=True, nullable=False, index=True)
    description = db.Column(db.Text)
    order = db.Column(db.Integer, nullable=False, index=True)
    steps = db.relationship('LessonStep', backref='lesson', lazy='dynamic', cascade='all, delete-orphan', order_by='LessonStep.order')
    hints = db.relationship('Hint', backref='lesson', lazy='dynamic', cascade='all, delete-orphan')
    quiz_questions = db.relationship('QuizQuestion', backref='lesson', lazy='dynamic', cascade='all, delete-orphan')

class LessonStep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False, index=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    step_type = db.Column(db.String(20), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    expected_command = db.Column(db.String(256))
    is_interactive = db.Column(db.Boolean, default=False)

class Hint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False, index=True)
    step_id = db.Column(db.Integer, db.ForeignKey('lesson_step.id'), index=True)
    content = db.Column(db.Text, nullable=False)
    hint_order = db.Column(db.Integer, default=1)

class QuizQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False, index=True)
    question_text = db.Column(db.Text, nullable=False)
    points = db.Column(db.Integer, default=10)
    order = db.Column(db.Integer, nullable=False)
    answers = db.relationship('QuizAnswer', backref='question', lazy='dynamic', cascade='all, delete-orphan')

class QuizAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('quiz_question.id'), nullable=False, index=True)
    answer_text = db.Column(db.String(512), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False, default=False)

class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False, index=True)
    completed = db.Column(db.Boolean, default=False)
    current_step = db.Column(db.Integer, default=0)
    current_step_id = db.Column(db.Integer, db.ForeignKey('lesson_step.id'), nullable=True)
    total_attempts = db.Column(db.Integer, default=0)
    correct_attempts = db.Column(db.Integer, default=0)
    hints_used = db.Column(db.Integer, default=0)
    __table_args__ = (db.UniqueConstraint('user_id', 'lesson_id', name='unique_user_lesson'),)

class Attempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False, index=True)
    step_id = db.Column(db.Integer, db.ForeignKey('lesson_step.id'), nullable=True, index=True)
    input_command = db.Column(db.Text)
    is_correct = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

class QuizAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False, index=True)
    question_id = db.Column(db.Integer, db.ForeignKey('quiz_question.id'), nullable=False, index=True)
    selected_answer_id = db.Column(db.Integer, db.ForeignKey('quiz_answer.id'))
    is_correct = db.Column(db.Boolean, default=False)

class UserActionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    action_type = db.Column(db.String(50), nullable=False, index=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=True, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

class UserHint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False, index=True)
    hint_id = db.Column(db.Integer, db.ForeignKey('hint.id'), nullable=False)
