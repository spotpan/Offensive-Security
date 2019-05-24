myfile = open("flag.txt", "r")

text = myfile.read()

newfile = open("soln.txt","w")

newfile.write(text)

newfile.close()

myfile.close()
