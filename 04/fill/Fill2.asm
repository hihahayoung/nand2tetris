@color         // declare color variable
M=0            // by default is white

(loop)
    @SCREEN    // RAM address 16384
    D=A

    @pixels 
    M=D       // pixel address (starting point: 16384, max: 16384+8192=24576)

    @KBD      // D = ascii code of a keyboard input
    D=M

    @black
    D;JGT     // if(keyboard > 0) goto black

    @color
    M=0       // otherwise white
    
    @color_screen
    0;JMP     // jump to subroutine that actually changes the color of screen

    (black)
        @color
        M=-1  // set to black

    (color_screen)
        @color
        D=M
        @pixels
        A=M
        M=D   // M[pixels] = @color

        @pixels
        M=M+1
        D=M

        @24576 // loop until end of pixels
        D=D-A
        @color_screen
        D;JLT

@loop
0;JMP         // infinite loop
