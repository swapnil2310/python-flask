
from flask import  render_template , url_for , flash , redirect
from flaskblog.forms import RegistrationForm , LoginForm
from flaskblog.models import User , Post
from flaskblog import app , db , bcrypt

posts= [
    {
        'title':'Blog Post 1',
        'author' : 'Swapnil Srivastava',
        'content':'First Blog',
        'date_posted':'Nov 1st 2018'
    },
    {
        'title':'Blog Post 2',
        'author':'Dhanapal R',
        'content':'Second Blog',
        'date_posted':'Nov 2st 2018',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html' , title='About')

@app.route("/register" , methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data , email = form.email.data , password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created. You can login Now!','success')
        return redirect(url_for('login'))
    return render_template('register.html' , title='Register',form=form)

@app.route("/login" , methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have logged in successfully!','success')
            return redirect(url_for('home'))
        else:
            flash('Invalid Email or Password','danger')
    return render_template('login.html' , title='Login',form=form)

