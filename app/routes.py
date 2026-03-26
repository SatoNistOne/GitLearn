from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.models import db, User, Lesson, UserProgress
from app.forms import LoginForm, RegisterForm

main = Blueprint('main', __name__)

@main.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@main.route('/')
def index():
    lessons = Lesson.query.order_by(Lesson.order).all()
    return render_template('index.html', lessons=lessons)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.dashboard'))
        flash('Неверное имя пользователя или пароль', 'error')
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('main.dashboard'))
    return render_template('register.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/dashboard')
@login_required
def dashboard():
    lessons = Lesson.query.order_by(Lesson.order).all()
    progress = {p.lesson_id: p for p in current_user.progress}
    completed_count = sum(1 for p in progress.values() if p.completed)
    total_count = len(lessons)
    return render_template('dashboard.html', lessons=lessons, progress=progress, completed_count=completed_count, total_count=total_count)

@main.route('/lesson/<slug>')
def lesson(slug):
    lesson = Lesson.query.filter_by(slug=slug).first_or_404()
    user_progress = None
    if current_user.is_authenticated:
        user_progress = UserProgress.query.filter_by(user_id=current_user.id, lesson_id=lesson.id).first()
        if not user_progress:
            user_progress = UserProgress(user_id=current_user.id, lesson_id=lesson.id)
            db.session.add(user_progress)
            db.session.commit()
    prev_lesson = Lesson.query.filter(Lesson.order < lesson.order).order_by(Lesson.order.desc()).first()
    next_lesson = Lesson.query.filter(Lesson.order > lesson.order).order_by(Lesson.order.asc()).first()
    return render_template('lesson.html', lesson=lesson, user_progress=user_progress, prev_lesson=prev_lesson, next_lesson=next_lesson)

@main.route('/api/progress', methods=['POST'])
@login_required
def update_progress():
    data = request.get_json()
    lesson_id = data.get('lesson_id')
    completed = data.get('completed', False)
    current_step = data.get('current_step', 0)

    progress = UserProgress.query.filter_by(user_id=current_user.id, lesson_id=lesson_id).first()
    if not progress:
        progress = UserProgress(user_id=current_user.id, lesson_id=lesson_id)
        db.session.add(progress)

    progress.completed = completed
    progress.current_step = current_step
    db.session.commit()

    return jsonify({'status': 'success'})

@main.route('/api/verify-command', methods=['POST'])
@login_required
def verify_command():
    data = request.get_json()
    user_command = data.get('command', '').strip()
    expected = data.get('expected', '').strip()

    if not expected:
        return jsonify({'correct': True, 'message': 'Задание без проверки команды'})

    if user_command.lower() == expected.lower():
        return jsonify({'correct': True, 'message': 'Верно! Команда выполнена правильно.'})
    else:
        return jsonify({'correct': False, 'message': 'Неверно. Попробуйте еще раз.'})
