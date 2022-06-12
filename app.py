from flask import Flask, render_template, request
from forms import SignUpForm
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"


posts = [
    {
     "author":" Barbara",
     "title" : "Jumpin!",
     "content" : "Lots of frogs can leap more than 20 times their body length",
     "date_posted" : "April 3, 2021"
    },
    {
        "author": " Jake",
        "title": "Grizzly!",
        "content": "The bite of a grizzly bear is strong enough to crush a bowling ball, ikes!",
        "date_posted": "April 4, 2021"
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/animal')
def animal():
    return render_template('animal.html', posts=posts, title="Fun Animal facts")

@app.route('/signup',methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template("userdata.html", result=result)
    return render_template('signup.html', form=form)