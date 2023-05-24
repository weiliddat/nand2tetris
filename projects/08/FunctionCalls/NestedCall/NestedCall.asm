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
// function Sys.init 0
(Sys.init)
// push constant 4000
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0
@THIS
D=A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// push constant 5000
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1
@THAT
D=A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// call Sys.main 0
@Sys.main$ret.1 // push returnAddress
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
@Sys.main
0;JMP
(Sys.main$ret.1) // returnAddress
// pop temp 1
@6
D=A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// label LOOP
(Sys.Sys.init$LOOP)// goto LOOP
@Sys.Sys.init$LOOP
0;JMP
// function Sys.main 5
(Sys.main)
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
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 4001
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0
@THIS
D=A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// push constant 5001
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1
@THAT
D=A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 1
@1
D=A
@LCL
D=M+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 2
@2
D=A
@LCL
D=M+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 3
@3
D=A
@LCL
D=M+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Sys.add12 1
@Sys.add12$ret.2 // push returnAddress
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
@Sys.add12
0;JMP
(Sys.add12$ret.2) // returnAddress
// pop temp 0
@5
D=A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
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
// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local 3
@3
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local 4
@4
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
// add
@SP
M=M-1
A=M
D=M
A=A-1
M=M+D
// add
@SP
M=M-1
A=M
D=M
A=A-1
M=M+D
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
// function Sys.add12 0
(Sys.add12)
// push constant 4002
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0
@THIS
D=A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// push constant 5002
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1
@THAT
D=A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
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
// push constant 12
@12
D=A
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
