
# coding: utf-8

# In[2]:


from flask import Flask , render_template , url_for , flash , redirect
from forms import RegistrationForm , LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '39fe1dd9ee4672c0c1bb3c2c048b584c'

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
        flash(f'Account created for { form.username.data }!','success')
        return redirect(url_for('home'))
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

if __name__ == '__main__':
    app.run(debug=True)