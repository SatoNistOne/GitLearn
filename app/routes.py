from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user
from app.models import db, User, Lesson, UserProgress, LessonStep, Attempt, Hint, QuizQuestion, QuizAnswer, UserActionLog, UserHint, QuizAttempt
from app.forms import LoginForm, RegisterForm
from datetime import datetime, date

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
        username_or_email = form.username_or_email.data
        user = User.query.filter(
            (User.username == username_or_email) | (User.email == username_or_email)
        ).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            user.last_login_at = datetime.utcnow()
            db.session.commit()
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.dashboard'))
        flash('Неверное имя пользователя, email или пароль', 'error')
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
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
    
    interactive_attempts = Attempt.query.filter(
        Attempt.user_id == current_user.id,
        Attempt.step_id != None
    ).count()
    
    return render_template('dashboard.html', lessons=lessons, progress=progress, completed_count=completed_count, total_count=total_count, interactive_attempts=interactive_attempts)

@main.route('/profile')
@login_required
def profile():
    lessons = Lesson.query.order_by(Lesson.order).all()
    completed_lessons = UserProgress.query.filter_by(user_id=current_user.id, completed=True).count()
    total_lessons = len(lessons)
    
    current_lesson = None
    in_progress = UserProgress.query.filter_by(user_id=current_user.id, completed=False).filter(UserProgress.current_step > 0).first()
    if in_progress:
        current_lesson = Lesson.query.get(in_progress.lesson_id)
    
    xp_current = current_user.total_experience
    xp_needed = 100
    level = 1
    temp_xp = xp_current
    
    while temp_xp >= xp_needed:
        temp_xp -= xp_needed
        level += 1
        xp_current = temp_xp
        xp_needed = int(xp_needed * 1.5)
    
    xp_percentage = (xp_current / xp_needed * 100) if xp_needed > 0 else 0
    
    hints_by_lesson = db.session.query(
        Lesson.title,
        db.func.count(UserHint.id).label('hint_count'),
        db.func.max(UserProgress.completed).label('is_completed')
    ).outerjoin(UserProgress, db.and_(
        UserProgress.lesson_id == Lesson.id,
        UserProgress.user_id == current_user.id
    )).outerjoin(
        UserHint, 
        db.and_(
            UserHint.lesson_id == Lesson.id,
            UserHint.user_id == current_user.id
        )
    ).group_by(Lesson.id, Lesson.title).order_by(Lesson.order).all()
    
    return render_template('profile.html', 
        completed_lessons=completed_lessons, 
        total_lessons=total_lessons, 
        current_lesson=current_lesson,
        xp_current=xp_current,
        xp_needed=xp_needed,
        xp_percentage=xp_percentage,
        hints_by_lesson=hints_by_lesson
    )

@main.route('/lesson/<slug>')
def lesson(slug):
    lesson = Lesson.query.filter_by(slug=slug).first_or_404()
    steps = LessonStep.query.filter_by(lesson_id=lesson.id).order_by(LessonStep.order).all()
    hints = Hint.query.filter_by(lesson_id=lesson.id).all()
    quiz_questions = QuizQuestion.query.filter_by(lesson_id=lesson.id).order_by(QuizQuestion.order).all()
    
    user_progress = None
    if current_user.is_authenticated:
        user_progress = UserProgress.query.filter_by(user_id=current_user.id, lesson_id=lesson.id).first()
        if not user_progress:
            user_progress = UserProgress(user_id=current_user.id, lesson_id=lesson.id)
            db.session.add(user_progress)
            db.session.commit()
        
        log = UserActionLog(user_id=current_user.id, lesson_id=lesson.id, action_type='lesson_viewed')
        db.session.add(log)
        db.session.commit()
        
        interactive_steps = [s for s in steps if s.is_interactive]
        if len(interactive_steps) == 0 and not user_progress.completed:
            user_progress.completed = True
            user_progress.completed_at = datetime.utcnow()
            user_progress.status = 'completed'
            db.session.commit()
    
    prev_lesson = Lesson.query.filter(Lesson.order < lesson.order).order_by(Lesson.order.desc()).first()
    next_lesson = Lesson.query.filter(Lesson.order > lesson.order).order_by(Lesson.order.asc()).first()

    continue_step_id = None
    if user_progress and not user_progress.completed and user_progress.current_step_id:
        continue_step_id = user_progress.current_step_id

    return render_template('lesson.html', lesson=lesson, steps=steps, hints=hints, quiz_questions=quiz_questions, user_progress=user_progress, prev_lesson=prev_lesson, next_lesson=next_lesson, continue_step_id=continue_step_id)

@main.route('/lesson/<slug>/continue')
@login_required
def continue_lesson(slug):
    lesson = Lesson.query.filter_by(slug=slug).first_or_404()
    user_progress = UserProgress.query.filter_by(user_id=current_user.id, lesson_id=lesson.id).first()
    
    if user_progress and not user_progress.completed and user_progress.current_step_id:
        return redirect(url_for('main.lesson', slug=slug, step_id=user_progress.current_step_id))
    
    return redirect(url_for('main.lesson', slug=slug))

@main.route('/api/progress', methods=['POST'])
@login_required
def update_progress():
    data = request.get_json()
    lesson_id = data.get('lesson_id')
    completed = data.get('completed', False)
    current_step = data.get('current_step', 0)
    current_step_id = data.get('current_step_id')
    time_spent = data.get('time_spent', 0)

    progress = UserProgress.query.filter_by(user_id=current_user.id, lesson_id=lesson_id).first()
    if not progress:
        progress = UserProgress(user_id=current_user.id, lesson_id=lesson_id)
        db.session.add(progress)

    progress.completed = completed
    progress.current_step = current_step
    if current_step_id:
        progress.current_step_id = current_step_id
    progress.time_spent += time_spent
    progress.last_accessed_at = datetime.utcnow()
    
    if completed and not progress.completed_at:
        progress.completed_at = datetime.utcnow()
        progress.status = 'completed'
    
    db.session.commit()
    return jsonify({'status': 'success'})

@main.route('/api/verify-command', methods=['POST'])
@login_required
def verify_command():
    data = request.get_json()
    user_command = data.get('command', '').strip()
    expected = data.get('expected', '').strip()
    lesson_id = data.get('lesson_id')
    step_id = data.get('step_id')
    time_taken = data.get('time_taken', 0)

    is_correct = user_command.lower() == expected.lower() if expected else True
    
    attempt = Attempt(
        user_id=current_user.id,
        lesson_id=lesson_id,
        step_id=step_id,
        input_command=user_command,
        expected_command=expected,
        is_correct=is_correct,
        time_taken=time_taken
    )
    db.session.add(attempt)
    
    if is_correct:
        progress = UserProgress.query.filter_by(user_id=current_user.id, lesson_id=lesson_id).first()
        if progress:
            progress.total_attempts += 1
            progress.correct_attempts += 1
            progress.current_step_id = step_id
            
            steps = LessonStep.query.filter_by(lesson_id=lesson_id).all()
            interactive_steps = [s for s in steps if s.is_interactive]
            
            if len(interactive_steps) > 0:
                completed_interactive = Attempt.query.filter_by(
                    user_id=current_user.id,
                    lesson_id=lesson_id,
                    is_correct=True
                ).count()
                
                if completed_interactive >= len(interactive_steps):
                    progress.completed = True
                    progress.completed_at = datetime.utcnow()
                    progress.status = 'completed'
            
            user = User.query.get(current_user.id)
            if user:
                user.total_experience += 10
        log = UserActionLog(user_id=current_user.id, lesson_id=lesson_id, step_id=step_id, action_type='step_completed')
        db.session.add(log)
    else:
        progress = UserProgress.query.filter_by(user_id=current_user.id, lesson_id=lesson_id).first()
        if progress:
            progress.total_attempts += 1
            progress.current_step_id = step_id

    db.session.commit()

    if is_correct:
        progress = UserProgress.query.filter_by(user_id=current_user.id, lesson_id=lesson_id).first()
        lesson_completed = progress.completed if progress else False
        return jsonify({
            'correct': True, 
            'message': 'Верно! Команда выполнена правильно.', 
            'points': 10,
            'lesson_completed': lesson_completed
        })
    else:
        return jsonify({'correct': False, 'message': 'Неверно. Попробуйте еще раз.'})

@main.route('/api/hint/<int:lesson_id>/<int:step_order>', methods=['POST'])
@login_required
def use_hint(lesson_id, step_order):
    hint = Hint.query.filter_by(lesson_id=lesson_id, step_id=step_order).first()
    
    if not hint:
        return jsonify({'error': 'Подсказка не найдена'}), 404

    user_hint = UserHint.query.filter_by(
        user_id=current_user.id, 
        lesson_id=lesson_id, 
        hint_id=hint.id
    ).first()
    
    if user_hint:
        return jsonify({'error': 'Подсказка уже использована'}), 400
    
    user_hint = UserHint(user_id=current_user.id, lesson_id=lesson_id, hint_id=hint.id)
    db.session.add(user_hint)

    progress = UserProgress.query.filter_by(user_id=current_user.id, lesson_id=lesson_id).first()
    if progress:
        progress.hints_used += 1

    log = UserActionLog(user_id=current_user.id, lesson_id=lesson_id, action_type='hint_used', details=f'Hint ID: {hint.id}')
    db.session.add(log)

    db.session.commit()
    return jsonify({'content': hint.content, 'penalty': 0})

@main.route('/api/quiz/submit', methods=['POST'])
@login_required
def submit_quiz_answer():
    data = request.get_json()
    question_id = data.get('question_id')
    answer_id = data.get('answer_id')
    lesson_id = data.get('lesson_id')
    step_id = data.get('step_id')
    time_taken = data.get('time_taken', 0)
    
    question = QuizQuestion.query.get_or_404(question_id)
    selected_answer = QuizAnswer.query.get_or_404(answer_id)
    
    is_correct = selected_answer.is_correct
    
    quiz_attempt = QuizAttempt(
        user_id=current_user.id,
        lesson_id=lesson_id,
        question_id=question_id,
        selected_answer_id=answer_id,
        is_correct=is_correct,
        time_taken=time_taken
    )
    db.session.add(quiz_attempt)
    
    progress = UserProgress.query.filter_by(user_id=current_user.id, lesson_id=lesson_id).first()
    lesson_completed = False
    
    if progress:
        if is_correct:
            progress.quiz_score += question.points
            progress.current_step_id = step_id
            
            all_correct = QuizAttempt.query.filter_by(
                user_id=current_user.id,
                lesson_id=lesson_id
            ).all()
            
            lesson_questions = QuizQuestion.query.filter_by(lesson_id=lesson_id).all()
            correct_count = sum(1 for a in all_correct if a.is_correct)
            
            if correct_count >= len(lesson_questions):
                progress.completed = True
                progress.completed_at = datetime.utcnow()
                progress.status = 'completed'
                lesson_completed = True
        
        user = User.query.get(current_user.id)
        if user and is_correct:
            user.total_experience += question.points
    
    db.session.commit()
    
    return jsonify({
        'correct': is_correct, 
        'points': question.points if is_correct else 0,
        'lesson_completed': lesson_completed
    })

@main.route('/api/stats')
@login_required
def get_stats():
    total_lessons = Lesson.query.count()
    completed_lessons = UserProgress.query.filter_by(user_id=current_user.id, completed=True).count()
    
    interactive_attempts = Attempt.query.filter(
        Attempt.user_id == current_user.id,
        Attempt.step_id != None
    ).count()
    correct_attempts = Attempt.query.filter(
        Attempt.user_id == current_user.id,
        Attempt.step_id != None,
        Attempt.is_correct == True
    ).count()
    
    hints_used = UserHint.query.filter_by(user_id=current_user.id).count()
    
    accuracy = (correct_attempts / interactive_attempts * 100) if interactive_attempts > 0 else 0
    
    return jsonify({
        'total_lessons': total_lessons,
        'completed_lessons': completed_lessons,
        'total_attempts': interactive_attempts,
        'correct_attempts': correct_attempts,
        'accuracy': round(accuracy, 1),
        'hints_used': hints_used,
        'experience': current_user.total_experience,
        'streak_days': current_user.streak_days
    })

@main.route('/api/streak', methods=['POST'])
@login_required
def update_streak():
    today = date.today()
    
    if current_user.last_activity_date == today:
        return jsonify({'streak_days': current_user.streak_days, 'max_streak_days': current_user.max_streak_days, 'message': 'Уже отмечено сегодня', 'xp_gained': 0})
    
    user = User.query.get(current_user.id)
    
    base_xp = 10
    streak_bonus = 0
    
    if user.last_activity_date:
        days_diff = (today - user.last_activity_date).days
        if days_diff == 1:
            user.streak_days += 1
            if user.streak_days >= 7:
                streak_bonus = 5
            if user.streak_days >= 30:
                streak_bonus = 15
            if user.streak_days >= 90:
                streak_bonus = 30
        elif days_diff > 1:
            user.streak_days = 1
    else:
        user.streak_days = 1
    
    if user.streak_days > user.max_streak_days:
        user.max_streak_days = user.streak_days
    
    xp_gained = base_xp + streak_bonus
    user.total_experience += xp_gained
    
    new_level = calculate_level(user.total_experience)
    if new_level > user.level:
        user.level = new_level
    
    user.last_activity_date = today
    db.session.commit()
    
    message = 'Серия обновлена!'
    if streak_bonus > 0:
        message += f' Бонус серии: +{streak_bonus} XP'
    
    return jsonify({
        'streak_days': user.streak_days, 
        'max_streak_days': user.max_streak_days,
        'level': user.level,
        'message': message,
        'xp_gained': xp_gained
    })

def calculate_level(experience):
    level = 1
    xp_required = 100
    
    while experience >= xp_required:
        experience -= xp_required
        level += 1
        xp_required = int(xp_required * 1.5)
    
    return level
