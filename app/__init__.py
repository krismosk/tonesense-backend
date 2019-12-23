from flask import Flask
from flask import Blueprint


# creates the flask app object
app = Blueprint('app', __name__)
# starts the debugger, if there's an error
# it will show in the browser. without this
# it will be too generic
app.config["DEBUG"] = True



from app import routes