from flask import Flask
from APIs.assignmentAPI import constructAssignmentBlueprint
from APIs.loginAPI import constructLoginBlueprint
from DB_stubs_for_api.assignmentStub import AssignmentImplStub
from DB_stubs_for_api.loginStub import loginImplStub
from RequestHandlers.AssignmentHandler import *
from RequestHandlers.LoginHandler import *

#initialize whatever and make dependencies
asnImpl = AssignmentImplStub()
asnHandler = AssignmentHandlerStub(asnImpl)

lgnImpl = loginImplStub()
lgnHandler = LoginHandler(lgnImpl)

#start up the app and import all the blueprint apis, inject dependencies
app = Flask(__name__)
app.register_blueprint(constructAssignmentBlueprint(asnHandler))
app.register_blueprint(constructLoginBlueprint(lgnHandler))


if __name__ == "__main__":
    app.run(debug=True)