global    _start

; PREFIX_END
    section .text
main:
    ; do something
    ret
; SUFFIX_BEGIN

    section .text
_start:

    call    main

    ; exit
    mov     rdi, rax
    mov     rax, 60
    syscall
