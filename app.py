
from flask import Flask, render_template, request, redirect, url_for
from api import * 
import emoji;

app = Flask(__name__)

@app.route('/')
def index():
    """Index page"""
    return render_template('index.html')

@app.route('/github')
def git():
        """Github page"""
        return render_template("index2.html")

@app.route('/sobre')
def sobre():
    """sobre page"""
    return render_template("about.html")


@app.route('/profile', methods=["GET", "POST"])
def profile():
	"""Render profile according to request"""

	
	user = request.form.get("username")
	
	if not user:
		return redirect(url_for('index'))

	
	if request.method == "POST":
		
		basic = basic_retrive(user)
		
		if not basic:
			return render_template("not_found.html")

		watch = watch_list(user)
		org = organizations(user)


		
		return render_template("profile.html", basic=basic, watch=watch, org=org, emoji=emoji)

	
	else:
		return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return render_template("404.html"), 404

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500


if __name__ == '__main__':
    app.run(debug=True)
