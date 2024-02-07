from routes import  app
@app.route('/')
@app.route('/index.html')
def home_page():
    return 'Home page'

@app.route('/about.html')
def about_page():
    return 'About Page'

@app.route('/login.html')
def login_page():
    return 'Login Page'


#@app.route('/films')
