#TODO: We probably want to implement some kind of request timeout. It looks like there are a few different ways of implementing it. We can talk to server team about this, they are also using flask. 
from flask import Flask
from APIs.assignmentAPI import constructAssignmentBlueprint
from APIs.loginAPI import constructLoginBlueprint
from DB_stubs_for_api.assignmentStub import AssignmentImplStub
from DB_stubs_for_api.loginStub import loginImplStub
from RequestHandlers.AssignmentHandler import *
from RequestHandlers.LoginHandler import *

#initialize whatever and make dependencies
asnImpl = AssignmentImplStub()
asnHandler = AssignmentHandlerImpl(asnImpl)

lgnImpl = loginImplStub()
lgnHandler = LoginHandler(lgnImpl)

#start up the app and import all the blueprint apis, inject dependencies
app = Flask(__name__)
app.register_blueprint(constructAssignmentBlueprint(asnHandler))
app.register_blueprint(constructLoginBlueprint(lgnHandler))


if __name__ == "__main__":
    app.run(debug=True)