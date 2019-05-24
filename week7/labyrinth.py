from pwn import *

array = [0x00000000000000e3, 0x00000000006010b0, 0x0000000000601130, 0x0000000000000000, 0x00000000000001f9, 0x00000000006010f0, 0x00000000006010d0, 0x0000000000000000, 0x0000000000000468, 0x00000000006010d0, 0x0000000000601130, 0x0000000000000000,
	0x0000000000000213, 0x0000000000601170,
	0x00000000006010d0, 0x0000000000000000,
	0x0000000000000121, 0x0000000000601110,
	0x0000000000601150, 0x0000000000000000,
	0x00000000000003a9, 0x0000000000601070,
	0x0000000000601110, 0x0000000000000000,
	0x000000000000019a, 0x0000000000601190,
	0x0000000000601070, 0x0000000000000000,
	0x000000000000013a, 0x0000000000601070,
	0x0000000000601190, 0x0000000000000000,
	0x0000000000000362, 0x0000000000601190,
	0x0000000000601090, 0x0000000000000000,
	0x00000000000002c6, 0x0000000000601190,
	0x00000000006010d0, 0x0000000000000000
]

nodes = "ABCDEFGHIJ"

myNodes = {}
alphaToAddr = {0x601070:"A", 0x601090:"B", 0x6010b0:"C", 0x6010d0:"D", 0x6010f0:"E", 0x601110:"F", 0x601130:"G", 0x601150:"H", 0x601170:"I", 0x601190:"J"}

pos = 0
curArray = []
for i in array:
    if i != 0:
        if i in alphaToAddr.keys():
            curArray.append(alphaToAddr[i])
        else:
            curArray.append(i)
    else:
        myNodes[nodes[pos]] = curArray
        curArray = []
        pos += 1


for key in sorted(myNodes.keys()):
    print(key, myNodes[key])
print(myNodes)

myList = []

def find(myNodes, pos, total, path):
    if total > 9595:
        return
    elif total == 9595:
        global myList
        myList.append(path)
        return path
    else:
        total = total + myNodes[pos][0]
        lpath = path + "L"
        rpath = path + "R"
        find(myNodes, myNodes[pos][1], total, lpath)
        find(myNodes, myNodes[pos][2], total, rpath)

find(myNodes, "A", 0, "")
print(myList)

REMOTE = False

bridge = ELF(sys.argv[1])

for item in myList:
	if REMOTE:
		p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1253)
		print(p.recvuntil(":"))
		p.sendline("joe215")
		p.recvuntil("?")
		p.sendline(item)
		response = p.recv()
		print(response)
	else:
		p = process(sys.argv[1])
		p.sendline(item)
		response = p.recv()
		print(response)

'''
REMOTE = True
for item in myList:
    if REMOTE:
        p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1253)
        print(p.recvuntil(":"))
        p.sendline("joe215")
        p.recvuntil("?")
        p.sendline(item)
        response = p.recvuntil(".")
        print(response)
'''
