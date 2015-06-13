from flask import Flask

HTML_SUFFIX = ".html"

app = Flask(__name__)


##########################################################################
#                              RENDER RESPOSES                           #   
##########################################################################

def view(name):
    #TODO: create a helper to validate the view name and return an html
    return app.send_static_file(name)

##########################################################################
##########################################################################
#                              ROUTES                                    #   
##########################################################################
#TODO: seprate this section in another file

@app.route('/')
def index():
    return view('index.html')


@app.route('/api/menu')
def menu():
    return "json menu usuario"

@app.route('/auth/login')
def login():
    return "login"

@app.route('/auth/logout')
def logout():
    return "logout"

@app.route('/auth/register')
def getRegister():
    return "regiter form"


##########################################################################


##########################################################################
#                              SERVICE                                   #   
##########################################################################

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')

##########################################################################

