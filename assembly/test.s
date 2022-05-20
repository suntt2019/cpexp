global    _start

    section   .data
    start_message:  db        "Start:", 10      ; note the newline at the end

    section .bss
    print_int_tmp: resb 10  ; int64 max 10 digits

    section   .text
print_int:                  ; Function: print_int(int64 x)
    PUSH    rbp
    MOV     rbp, rsp

    MOV     rax, [rbp+16]    ; Save parameter to rax
    MOV     rdi, print_int_tmp
    ADD     rdi, 9          ; Init addr, add tmp max_size -1
    MOV     rbx, 10         ; BX = 10
    MOV     rcx, 0          ; CX = 0
print_int_loop:             ; do {
    XOR     rdx, rdx        ;   DX = 0
    DIV     rbx             ;   (DX AX) / BX = AX ... DX
    ADD     dl, 30h         ;   30h = ASCII '0'
    MOV     [rdi], dl       ;   al -> tmp
    DEC     rdi             ;   DI--
    INC     rcx             ;   CX++
    CMP     rax, 0          ; }while(AX > 0)
    JA      print_int_loop  ;
    INC     rdi             ; DI--

    ; System call write(1): (rax, rdi, rsi, rdx) = (1, stdout, addr, len)
    MOV     rax, 1
    MOV     rsi, rdi
    MOV     rdi, 1
    MOV     rdx, rcx
    SYSCALL

    MOV     rsp, rbp
    POP     rbp
    RET

main:
    MOV     rax, 65434
    PUSH    rax
    CALL    print_int
    ADD     rsp, 8

    MOV     rax, 0      ; return 0
    RET


_start:
    MOV     rax, 1
    MOV     rdi, 1
    MOV     rsi, start_message
    MOV     rdx, 7
    SYSCALL

    CALL    main

    ; System call exit(60): (rax, rdi) = (1, exit_code)
    MOV     rdi, rax
    MOV     rax, 60
    SYSCALL
