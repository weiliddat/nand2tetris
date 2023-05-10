// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

    // reset screen
    @SCREEN
    M=0

(LOOP)
    @KBD
    D=M

    @BLACK
    D;JGT

    @WHITE
    D;JEQ

    // goto LOOP
    @LOOP
    0;JMP

(END)
    @END
    0;JMP

(BLACK)
    // init fill size, 256 * 32
    @8192
    D=A
    @s
    M=D

    // init fill index
    @i
    M=0

    (BLOOP)
        // if i >= s goto BLOOPEND
        @i
        D=M
        @s
        D=D-M
        @BLOOPEND
        D;JGE

        // blacken screen + i 
        @SCREEN
        D=A
        @i
        D=D+M
        A=D
        M=-1

        // i = i + 1
        @i
        M=M+1

        @BLOOP
        0;JMP

    (BLOOPEND)
        @LOOP
        0;JMP

(WHITE)
    // init fill size, 256 * 32
    @8192
    D=A
    @s
    M=D

    // init fill index
    @i
    M=0

    (WLOOP)
        // if i >= s goto WLOOPEND
        @i
        D=M
        @s
        D=D-M
        @WLOOPEND
        D;JGE

        // blacken screen + i 
        @SCREEN
        D=A
        @i
        D=D+M
        A=D
        M=0

        // i = i + 1
        @i
        M=M+1

        @WLOOP
        0;JMP

    (WLOOPEND)
        @LOOP
        0;JMP
