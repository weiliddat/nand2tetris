// function SimpleFunction.test 2
@SimpleFunction.SimpleFunction.test
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push local 0
@0
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
M=M-1
A=M
D=M
A=A-1
M=M+D
// not
@SP
A=M-1
M=!M
// push argument 0
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
M=M-1
A=M
D=M
A=A-1
M=M+D
// push argument 1
@1
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D
// return
@LCL // frame = LCL
D=M
@R13
M=D
@5 // retAddr = *(frame-5)
A=D-A
D=M
@R14
M=D
@SP // *ARG = pop()
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG // SP = ARG+1
D=M+1
@SP
M=D
@R13 // THAT = *(frame-1)
AM=M-1
D=M
@THAT
M=D
@R13 // THIS = *(frame-2)
AM=M-1
D=M
@THIS
M=D
@R13 // ARG = *(frame-3)
AM=M-1
D=M
@ARG
M=D
@R13 // LCL = *(frame-4)
AM=M-1
D=M
@LCL
M=D
@R14 // goto retAddr
A=M
0;JMP
@END_LOOP
0;JMP
(TRUE)
@SP
A=M
M=-1
@RET
A=M
0;JMP
(FALSE)
@SP
A=M
M=0
@RET
A=M
0;JMP
(END_LOOP)
@END_LOOP
0;JMP
