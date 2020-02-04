from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = 'f09683b9ca36c6011bf12c18ce7ed560'

posts = [
	{
		"author": "Mario Noseda",
		"title": "Blog Post 1",
		"content": "First post content",
		"date_posted": "February 02, 2020"
	},
	{
		"author": "Celina Steffani",
		"title": "Blog Post 2",
		"content": "Second post content",
		"date_posted": "February 03, 2020"
	}
]


@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", posts=posts)

@app.route("/about")
def about():
	return render_template("about.html", title="About")

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template("login.html", title="Login", form=form)



if __name__ == "__main__":
	app.run(debug=True)