global    _start


extern labs

extern printf

	section .data
	a: dd -1
	str_dGhpcyBzaG91bGRuJ3QgcHJpbnRcbg: db "this shouldn't print", 10, 0
	str_JWxkICVsZCAlYyAlZFxu: db "%ld %ld %c %d", 10, 0
	str_JWRcbg: db "%d", 10, 0

	section .bss
	t0: resd 1
	t1: resq 1
	t2: resq 1
	t3: resb 1
	t4: resd 1
	t5: resd 1
	t6: resq 1
	t7: resd 1
	t8: resb 1
	t9: resq 1
	t10: resq 1
	t11: resd 1
	t12: resd 1
	t13: resd 1

	section .text

add:
	push	rbp
	mov 	rbp, rsp
	sub 	rsp, 8
	mov 	dword [rbp-4], edi
	mov 	dword [rbp-8], esi
	mov 	eax, dword [rbp-4]
	add 	eax, dword [rbp-8]
	mov 	dword [t0], eax
	mov 	rsp, rbp
	pop 	rbp
	mov 	eax, dword [t0]
	ret

main:
	push	rbp
	mov 	rbp, rsp
	sub 	rsp, 10
	movsx	rax, dword [a]
	mov 	qword [t1], rax
	mov 	rax, 4
	add 	rax, qword [t1]
	mov 	qword [t2], rax
	cmp 	qword [t2], 0
	lahf
	mov	al, ah
	not 	al
	and 	al, 64
	shr 	al, 6
	mov 	byte [t3], al
	mov 	al, byte [t3]
	mov 	byte [rbp-1], al
	movsx	rax, byte [rbp-1]
	mov 	dword [t4], eax
	mov 	eax, dword [t4]
	mov 	dword [rbp-5], eax
	movsx	rdi, dword [a]
	movsx	rsi, dword [rbp-5]
	call	add
	mov 	dword [t5], eax
	mov 	eax, dword [t5]
	mov 	dword [rbp-5], eax
	movsx	rax, dword [rbp-5]
	mov 	qword [t6], rax
	mov 	rax, qword [t6]
	cmp 	rax, 0
	jg  	L1
	jmp 	L0
L1:	mov 	rdi, str_dGhpcyBzaG91bGRuJ3QgcHJpbnRcbg
	movsx	rsi, dword [rbp-5]
	xor 	rax, rax
	call	printf
	mov 	dword [t7], eax
	cmp 	dword [t7], 0
	lahf
	mov	al, ah
	not 	al
	and 	al, 64
	shr 	al, 6
	mov 	byte [t8], al
	mov 	al, byte [t8]
	cmp 	al, 1
	je  	L2
	jmp 	L0
L2:	movsx	rax, dword [rbp-5]
	mov 	qword [t9], rax
	mov 	rax, qword [t9]
	add 	rax, 10
	mov 	qword [t10], rax
	mov 	rax, qword [t10]
	mov 	dword [t11], eax
	mov 	eax, dword [t11]
	mov 	dword [rbp-5], eax
L0:	mov 	al, 98
	mov 	byte [rbp-6], al
	mov 	rdi, str_JWxkICVsZCAlYyAlZFxu
	movsx	rsi, dword [a]
	movsx	rdx, dword [rbp-5]
	movsx	rcx, byte [rbp-6]
	movsx	r8, byte [rbp-1]
	xor 	rax, rax
	call	printf
	mov 	dword [t12], eax
	mov 	eax, dword [t12]
	mov 	dword [rbp-10], eax
	mov 	rdi, str_JWRcbg
	movsx	rsi, dword [rbp-10]
	xor 	rax, rax
	call	printf
	mov 	dword [t13], eax
	mov 	rsp, rbp
	pop 	rbp
	mov 	eax, 0
	ret


    section .text
_start:

    call    main

    ; exit
    mov     rdi, rax
    mov     rax, 60
    syscall
