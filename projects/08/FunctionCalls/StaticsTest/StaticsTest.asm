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
// function Class1.set 0
(Class1.set)
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
// pop static 0
@Class1.0
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
// pop static 1
@Class1.1
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
// push constant 0
@0
D=A
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
// function Class1.get 0
(Class1.get)
// push static 0
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static 1
@Class1.1
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
@Sys.init$ret.1 // push returnAddress
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
(Sys.init$ret.1) // returnAddress
@END_LOOP
0;JMP
// function Class2.set 0
(Class2.set)
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
// pop static 0
@Class2.0
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
// pop static 1
@Class2.1
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
// push constant 0
@0
D=A
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
// function Class2.get 0
(Class2.get)
// push static 0
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static 1
@Class2.1
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
@Sys.init$ret.2 // push returnAddress
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
(Sys.init$ret.2) // returnAddress
@END_LOOP
0;JMP
// function Sys.init 0
(Sys.init)
// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Class1.set 2
@Class1.set$ret.3 // push returnAddress
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
@2
D=D-A
@ARG
M=D
@SP // LCL = SP
D=M
@LCL
M=D
@Class1.set
0;JMP
(Class1.set$ret.3) // returnAddress
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
// push constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Class2.set 2
@Class2.set$ret.4 // push returnAddress
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
@2
D=D-A
@ARG
M=D
@SP // LCL = SP
D=M
@LCL
M=D
@Class2.set
0;JMP
(Class2.set$ret.4) // returnAddress
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
// call Class1.get 0
@Class1.get$ret.5 // push returnAddress
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
@Class1.get
0;JMP
(Class1.get$ret.5) // returnAddress
// call Class2.get 0
@Class2.get$ret.6 // push returnAddress
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
@Class2.get
0;JMP
(Class2.get$ret.6) // returnAddress
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
