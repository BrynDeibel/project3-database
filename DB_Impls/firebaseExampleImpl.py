from firebase import firebase

firebase = firebase.FirebaseApplication('https://database-team-project3-default-rtdb.firebaseio.com', None)

#Creates a new entry or overrides a previous entry in TestFolder with a given FileID
result = firebase.put('/TestFolder', 'FileID', 
                        {'key1': 'value1',
                        'key2': 'value2'})
print(result)

#Creates a new entry in TestFolder and automatically generates it a new ID
result = firebase.post('/TestFolder',
                        {'key1': 'value1',
                        'key2': 'value2'})
print(result)
              
#Gets the values of an entry in TestFolder with a given  FileID
result = firebase.get("/TestFolder", "FileID")
print(result)

#Gets the values of all entries in TestFolder
result = firebase.get("/TestFolder", "")
print(result)

#Delete a given entry in TestFolder
result = firebase.delete('/TestFolder', 'FileID')
print(result)
