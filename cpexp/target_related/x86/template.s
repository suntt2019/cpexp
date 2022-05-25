global    _start

    section .data
    start_message:  db        "Start:", 10

; PREFIX_END
    section .text
main:
    ; do something
    ret
; SUFFIX_BEGIN

    section .text
_start:
    mov     rax, 1
    mov     rdi, 1
    mov     rsi, start_message
    mov     rdx, 7
    syscall

    call    main

    ; exit
    mov     rdi, rax
    mov     rax, 60
    syscall
