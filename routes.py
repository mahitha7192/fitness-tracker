from flask import flash, redirect, render_template, url_for

from app import app, db
from app.forms import ExerciseForm, LoginForm, RegistrationForm
from app.models import Exercise, User


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check your email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    exercises = Exercise.query.all()
    return render_template('dashboard.html', title='Dashboard', exercises=exercises)

@app.route('/log_exercise', methods=['GET', 'POST'])
def log_exercise():
    form = ExerciseForm()
    if form.validate_on_submit():
        exercise = Exercise(description=form.description.data)
        db.session.add(exercise)
        db.session.commit()
        flash('Exercise logged successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('log_exercise.html', title='Log Exercise', form=form)
