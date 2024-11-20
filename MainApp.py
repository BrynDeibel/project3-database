from flask import Flask
from APIs.assignmentAPI import constructAssignmentBlueprint
from DB_stubs_for_api.assignmentStub import AssignmentImplStub

#initialize whatever and make dependencies
assignmentStub = AssignmentImplStub()

#start up the app and import all the blueprint apis, inject dependencies
app = Flask(__name__)
app.register_blueprint(constructAssignmentBlueprint(assignmentStub))
