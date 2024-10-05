from flask import Flask, render_template,flash,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' 
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)  # Hashed password,adjust length as needed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
        #from main import app, db, User
        #with app.app_context():
             #new_user = User(username='john_doe', email='john@example.com', password='password123')
      #db.session.add(new_user)
     #db.session.commit()  worked!

# Create the database tables (only needed in development or when initializing)
with app.app_context():
    db.create_all()



users = {
    'john@example.com': {
        'password': 'password123',
        'username': 'john_doe'
    },
    'jane@example.com': {
        'password': 'password456',
        'username': 'jane_smith'
    }
}
# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/diet_planner')
def diet_planner():
    return render_template('diet_planner.html')

@app.route('/water_intake')
def water_intake():
    return render_template('water_intake.html')

@app.route('/exercise')
def exercise():
    return render_template('exercise.html')

@app.route('/food_calorie')
def food_calorie():
    return render_template('food_calorie.html')

@app.route('/progress')
def progress():
    # Assuming you have a function to get user data
    user_data = {
        'water_intake': '2.5 liters',
        'current_workout': 'Full Body Workout',
        'age': 25,
        'chosen_diet': 'Keto Diet',
        'affirmation': 'You are strong and capable!'
    }
    return render_template('progress.html', user_data=user_data)

@app.route('/planner')
def planner():
    return render_template('planner.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        if email in users:
            flash('User already exists. Please login.', 'danger')
        else:
            password = request.form['password']
            username = request.form['username']
            users[email] = {'password': password, 'username': username}
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email in users:
            if users[email]['password'] == password:
                flash(f'Login successful as {users[email]["username"]}!', 'success')
                return redirect(url_for('about'))
            else:
                flash('Incorrect password. Please try again.', 'danger')
        else:
            flash('User not found. Please register.', 'danger')

    return render_template('login.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # Handle the form submission and update the user's profile
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        if not name or not username  or not email:
            flash('All fields are required!', 'danger')
            return redirect(url_for('profile'))

        # Update current user details
        current_user.name = name
        current_user.username = username
        current_user.email = email

        try:
            db.session.commit()
            flash('Profile updated successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating profile: {str(e)}', 'danger')
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))

    # (Fetch the current user's data from the database)
    return render_template('profile.html', users=users)



    

if __name__ == '__main__':
    app.run(debug=True)


