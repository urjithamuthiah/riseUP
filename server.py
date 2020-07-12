from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '2ca73fe6900670f73913665aedbc8a74'

@app.route('/home')
def home():
    return render_template('cc_landing_page.html', title='Home')


#need a sign up template
@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/org_login", methods = ['GET', 'POST'])
def org_login():
    form = LoginForm()
    if form.validate_on_submit():
        #not sure how to check whether the login information is correct
        if form.username.data == 'username' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('org_login_page.html', title = 'Organization Login', form = form)


@app.route("/user_login", methods = ['GET', 'POST'])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        #not sure how to check whether the login information is correct
        if form.username.data == 'username' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('user_login_page.html', title = 'User Login', form = form)


if __name__ == '__main__':
    app.run(debug=True)
