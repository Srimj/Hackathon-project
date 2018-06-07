from flask import Flask,render_template,request,redirect, session
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'hellothere'
bcrypt = Bcrypt(app)
# @app.route('/<user>', methods=['post', 'get'])
# def tuna(user):
# 	return "Hello %s" % user


# @app.route('/<user>', methods=['post' , 'get'])
# def index(user):
# 	a=[1,2,3]
# 	if request.method == 'POST':
# 		return redirect('/login')
	
# 	return "hello %s" % user , render_template('index.html' , a=a)

@app.route('/logout' , methods=['post' , 'get'])
def logout():
	if session['login']:
		session['login'] = False
		session['email'] = ''
		print("hello")
	return redirect('/login')


@app.route('/home', methods=['post' , 'get'])
def home():
	if request.method == 'POST':
		return redirect('/logout')
	if session['login']:
		return render_template('home.html')
	else:
		return redirect('/login')


@app.route('/register', methods=['post' , 'get'])
def register():

	if request.method == 'POST':
		pw_hash = bcrypt.generate_password_hash(request.form['password'])
		t[request.form['Email']]=pw_hash
		return redirect('/login')
	return render_template('register.html')



@app.route('/login' , methods=['post', 'get'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['submit'] == 'login':
			if request.form['Email'] in t.keys():
			 	if bcrypt.check_password_hash(t[request.form['Email']] , request.form['password']):
			 		session['login'] = True
			 		session['Email'] = request.form['Email']
			 		return redirect('/home')
			 	else:
			 		error = 'password does not match'	
			else:
				error = 'email does not match'
		elif request.form['submit'] == 'register':
			return redirect('/register')

		return render_template('login.html' , error=error)
	return render_template('login.html' , error=error)

if __name__ == '__main__':
	app.jinja_env.globals.update(chr=chr)
	t = {}
	app.run(host="0.0.0.0",port=8000, debug=True,threaded=True)

