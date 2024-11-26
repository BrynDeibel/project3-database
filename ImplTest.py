import asyncio
import sys
sys.path.append('..')
from DB_Impls.assignment_fb_db_impl import *

impl = AssignmentInterfaceFirebase()
read = asyncio.run(impl.readAssignments())

print ("hellow")