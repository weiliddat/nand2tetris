// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@EQTRUE1
D;JEQ
@SP
A=M
M=0
@EQEND1
0;JMP
(EQTRUE1)
@SP
A=M
M=-1
(EQEND1)
@SP
M=M+1
// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@EQTRUE2
D;JEQ
@SP
A=M
M=0
@EQEND2
0;JMP
(EQTRUE2)
@SP
A=M
M=-1
(EQEND2)
@SP
M=M+1
// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@EQTRUE3
D;JEQ
@SP
A=M
M=0
@EQEND3
0;JMP
(EQTRUE3)
@SP
A=M
M=-1
(EQEND3)
@SP
M=M+1
// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@LTTRUE4
D;JLT
@SP
A=M
M=0
@LTEND4
0;JMP
(LTTRUE4)
@SP
A=M
M=-1
(LTEND4)
@SP
M=M+1
// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@LTTRUE5
D;JLT
@SP
A=M
M=0
@LTEND5
0;JMP
(LTTRUE5)
@SP
A=M
M=-1
(LTEND5)
@SP
M=M+1
// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@LTTRUE6
D;JLT
@SP
A=M
M=0
@LTEND6
0;JMP
(LTTRUE6)
@SP
A=M
M=-1
(LTEND6)
@SP
M=M+1
// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@GTTRUE7
D;JGT
@SP
A=M
M=0
@GTEND7
0;JMP
(GTTRUE7)
@SP
A=M
M=-1
(GTEND7)
@SP
M=M+1
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@GTTRUE8
D;JGT
@SP
A=M
M=0
@GTEND8
0;JMP
(GTTRUE8)
@SP
A=M
M=-1
(GTEND8)
@SP
M=M+1
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@GTTRUE9
D;JGT
@SP
A=M
M=0
@GTEND9
0;JMP
(GTTRUE9)
@SP
A=M
M=-1
(GTEND9)
@SP
M=M+1
// push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 53
@53
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
// push constant 112
@112
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
// neg
@SP
M=M-1
A=M
D=M
M=-D
@SP
M=M+1
// and
@SP
M=M-1
A=M
D=M
A=A-1
M=M&D
// push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
// or
@SP
M=M-1
A=M
D=M
A=A-1
M=M|D
// not
@SP
M=M-1
A=M
D=M
M=!D
@SP
M=M+1
(END_LOOP)
@END_LOOP
0;JMP
