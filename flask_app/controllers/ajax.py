from flask import redirect, render_template, request, session
from flask_app import app
from flask_app.models import User
from flask_app.config.regex import EMAIL_REGEX

@app.route('/ajax/user/username', methods=['POST'])
def valid_username():
  if len(request.form['username']) < 3:
    return render_template('partials/username.html',reason='short')
  if len(request.form['username']) > 45:
    return render_template('partials/username.html',reason='long')
  if(User.get_by_username(request.form)):
    return render_template('partials/username.html',reason='taken')
  return ""

@app.route('/ajax/user/email', methods=['POST'])
def valid_email():
  if not EMAIL_REGEX.match(request.form['email']):
    return render_template('partials/email.html',reason='not_email')
  if len(request.form['email']) > 100:
    return render_template('partials/email.html',reason='long')
  if(User.get_by_email(request.form)):
    return render_template('partials/email.html',reason='taken')
  return ""

@app.route('/ajax/user/password', methods=['POST'])
def valid_password():
  if len(request.form['password']) < 8:
    return render_template('partials/password.html',reason='short')
  return ""

@app.route('/ajax/user/confirm_password', methods=['POST'])
def valid_confirm_password():
  if not request.form['confirm_password'] == request.form['password']:
    return render_template('partials/confirm_password.html',reason='not_valid')
  return ""

@app.route('/ajax/user/login', methods=['POST'])
def valid_login():
  user = User.get_by_email(request.form)
  if not user:
    return render_template('partials/login.html')
  if not user.validate_pw(request.form['password']):
    return render_template('partials/login.html')
  session['user']=user.id
  return render_template('partials/login.html',valid=True)
