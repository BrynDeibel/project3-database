from flask import Flask
from APIs.assignmentAPI import constructAssignmentBlueprint
from DB_stubs_for_api.assignmentStub import AssignmentImplStub
from RequestHandlers.AssignmentHandler import *

#initialize whatever and make dependencies
asnImpl = AssignmentImplStub()
asnHandler = AssignmentHandlerStub(asnImpl)

#start up the app and import all the blueprint apis, inject dependencies
app = Flask(__name__)
app.register_blueprint(constructAssignmentBlueprint(asnHandler))
