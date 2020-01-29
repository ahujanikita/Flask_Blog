from flask import Flask, render_template, url_for, flash
from forms import RegisterationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dad947f405683967651db65228f5007c'

posts = [
    {
        'author': 'Nikita Ahuja',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '21 April, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '25 April, 2020'
    }
]
@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html',posts=posts) 

@app.route('/about')
def about():
    return render_template('about.html', title = 'About') 

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!')
    return render_template('register.html',title = 'Register', form = form) 

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title = 'Login', form = form) 



if __name__ == '__main__':
    app.run(debug=True)