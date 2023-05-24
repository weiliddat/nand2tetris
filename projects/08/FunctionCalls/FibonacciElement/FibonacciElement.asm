@256 // SP=256
D=A
@SP
M=D
@Sys.init$ret.0 // push returnAddress
D=A
@SP
M=M+1
A=M-1
M=D
@LCL // push LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG // push ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS // push THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT // push THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP // ARG = SP - 5 - number_args
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP // LCL = SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.init$ret.0) // returnAddress
@END_LOOP
0;JMP
// function Main.fibonacci 0
(Main.fibonacci)
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
// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@RET1
D=A
@RET
M=D
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@TRUE
D;JLT
@FALSE
0;JMP
(RET1)
@SP
M=M+1
// if-goto IF_TRUE
@SP
M=M-1
A=M
D=M
@Main.Main.fibonacci$IF_TRUE
D;JNE
// goto IF_FALSE
@Main.Main.fibonacci$IF_FALSE
0;JMP
// label IF_TRUE
(Main.Main.fibonacci$IF_TRUE)// push argument 0        
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
// label IF_FALSE
(Main.Main.fibonacci$IF_FALSE)// push argument 0
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
// push constant 2
@2
D=A
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
// call Main.fibonacci 1
@Main.fibonacci$ret.1 // push returnAddress
D=A
@SP
M=M+1
A=M-1
M=D
@LCL // push LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG // push ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS // push THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT // push THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP // ARG = SP - 5 - number_args
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP // LCL = SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.1) // returnAddress
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
// push constant 1
@1
D=A
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
// call Main.fibonacci 1
@Main.fibonacci$ret.2 // push returnAddress
D=A
@SP
M=M+1
A=M-1
M=D
@LCL // push LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG // push ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS // push THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT // push THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP // ARG = SP - 5 - number_args
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP // LCL = SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.2) // returnAddress
// add
@SP
M=M-1
A=M
D=M
A=A-1
M=M+D
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
(END_LOOP)
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
@256 // SP=256
D=A
@SP
M=D
@Sys.init$ret.3 // push returnAddress
D=A
@SP
M=M+1
A=M-1
M=D
@LCL // push LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG // push ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS // push THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT // push THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP // ARG = SP - 5 - number_args
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP // LCL = SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.init$ret.3) // returnAddress
@END_LOOP
0;JMP
// function Sys.init 0
(Sys.init)
// push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Main.fibonacci 1
@Main.fibonacci$ret.4 // push returnAddress
D=A
@SP
M=M+1
A=M-1
M=D
@LCL // push LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG // push ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS // push THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT // push THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP // ARG = SP - 5 - number_args
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP // LCL = SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.4) // returnAddress
// label WHILE
(Sys.Sys.init$WHILE)// goto WHILE
@Sys.Sys.init$WHILE
0;JMP
(END_LOOP)
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
