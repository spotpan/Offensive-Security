import math

forest = open("forest.txt","r")
forestlist = forest.read().strip().split("\\x")
lenforest = len(forestlist)
assert(lenforest == 256 ** 2)

valArray = {}



for i in range(lenforest):
    if forestlist[i] != "00":
        valArray[forestlist[i]] = i

for key in sorted(valArray):
    print(key, valArray[key], end=" ")
    print("First:", valArray[key]//256, "Second:", valArray[key]%256)
