
// RAM[2] = RAM[0] * RAM[1]

    // i=1
    @i
    M=1

    // sum=0
    @sum
    M=0

(LOOP)
    // if i > RAM[1] goto STOP
    @i
    D=M
    @R1
    D=D-M
    @STOP
    D;JGT

    // sum=sum+RAM[0]

    @R0
    D=M
    @sum
    D=D+M
    @sum
    M=D

    // i = i+1
    @i
    M=M+1

    // goto LOOP
    @LOOP
    0;JMP

(STOP)
    // R2=sum
    @sum
    D=M
    @R2
    M=D

(END)
    @END
    0;JMP
