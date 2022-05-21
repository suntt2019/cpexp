global    _start

    section .data
    start_message:  db        "Start:", 10

    section .bss
    print_int_tmp: resb 10  ; int64 max 10 digits

    section .text
_print_int:                 ; Function: print_int(int64 x)
    push    rbp
    mov     rbp, rsp

    mov     rax, [rbp+16]   ; Save parameter to rax
    mov     rdi, print_int_tmp
    add     rdi, 9          ; Init addr, add tmp max_size -1
    mov     rbx, 10         ; BX = 10
    mov     rcx, 0          ; CX = 0
print_int_loop:             ; do {
    xor     rdx, rdx        ;   DX = 0
    div     rbx             ;   (DX AX) / BX = AX ... DX
    add     dl, 30h         ;   30h = ASCII '0'
    mov     [rdi], dl       ;   al -> tmp
    dec     rdi             ;   DI--
    inc     rcx             ;   CX++
    cmp     rax, 0          ; }while(AX > 0)
    ja      print_int_loop  ;
    inc     rdi             ; DI--

    ; System call write(1): (rax, rdi, rsi, rdx) = (1, stdout, addr, len)
    mov     rax, 1
    mov     rsi, rdi
    mov     rdi, 1
    mov     rdx, rcx
    syscall

    mov     rsp, rbp
    pop     rbp
    ret
; PREFIX_END
    section .text
_main:
    mov     rax, 1234
    push    rax
    call    print_int
    add     rsp, 8

    mov     rax, 0
    ret
; SUFFIX_BEGIN

    section .text
_start:
    mov     rax, 1
    mov     rdi, 1
    mov     rsi, start_message
    mov     rdx, 7
    syscall

    call    _main

    ; System call exit(60): (rax, rdi) = (60, exit_code)
    mov     rdi, rax
    mov     rax, 60
    syscall
