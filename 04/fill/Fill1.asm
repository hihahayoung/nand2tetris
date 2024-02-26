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
    @KBD
    D=M

    // Input O

    @INPUT
    D;JNE

    // Input X
    @NOINPUT
    D;JEQ


    (INPUT)
        @COUNT
        M=0

        (FILLB)
            @8192 // This is because there are 8K memory blocks 1024*8
            D=A // Set D as the address
            D=D-M // Subtract count from address

            @LOOP
            D;JLT

            @COUNT
            D=M // Set D as the initial count value

            @SCREEN
            A=A+D // Set the screen index
            M=-1 // Set the color to black

            @COUNT
            M=M+1 // Add 1 to count

            @FILLB
            0;JMP


    (INPUT)
        @COUNT
        M=0

        (FILLW)
            @8192 // This is because there are 8K memory blocks 1024*8
            D=A // Set D as the address
            D=D-M // Subtract count from address

            @LOOP
            D;JLT

            @COUNT
            D=M // Set D as the initial count value

            @SCREEN
            A=A+D // Set the screen index
            M=0 // Set the color to white

            @COUNT
            M=M+1 // Add 1 to count

            @FILLW
            0;JMP


