// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

//// Replace this comment with your code.


(LOOP)

    @SCREEN // RAM address 16384
    D=A

    @PIXELS
    M=D
    
    @KBD
    D=M

    @BLACK
    D;JGT

    @COLOR
    M=0

    @FILL
    0;JMP

    (BLACK)
        @COLOR
        M=-1
    
    (FILL)
        @COLOR
        D=M
        
        @PIXELS
        A=M // PIXEL ADDRESS starting from 16384
        M=D // M[PIXELS] = @COLOR

        @PIXELS
        M=M+1 // Increse the pixel index by 1
        D=M // And store the index as D

        @24576 // Loops until the end of pixels
        D=D-A

        @FILL
        D;JLT

@LOOP
0;JMP
