import flask, flask.views
import functools

app = flask.Flask(__name__)
app.secret_key = "nose"

def login_required(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        if 'user' in flask.session:
            # if user in session it's ok to call that method
            return method(*args,**kwargs)
        else:
            return "not logged in"
    return wrapper


class Index(flask.views.MethodView):
    def get(self):
        return "index.html"
    def post(self):
        return "post index" + flask.request.form['user'] 

class Home(flask.views.MethodView):
    @login_required
    def get(self):
        return "welcome home"

class Login(flask.views.MethodView):
    def get(self):
        flask.session['user'] = 'user'
        return "login form"
    def post(self):
        flask.session['user'] = flask.request.form['user']
        return "process login"

class Logout(flask.views.MethodView):
    def get(self):
        flask.session.pop('user',None)
        return "process logout"

app.add_url_rule('/',view_func = Index.as_view('index'),methods=['GET','POST'])
app.add_url_rule('/home',view_func = Home.as_view('home'),methods=['GET','POST'])
app.add_url_rule('/login',view_func = Login.as_view('login'),methods=['GET','POST'])
app.add_url_rule('/logout',view_func = Logout.as_view('logout'),methods=['GET','POST'])


app.debug = True
app.run(host='0.0.0.0')
