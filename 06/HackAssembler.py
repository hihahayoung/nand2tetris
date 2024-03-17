import os

class Assembler:
    def __init__(self, inputAsm):
        self.__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.path = os.path.join(self.__location__, inputAsm)
        self.file = open(os.path.join(self.__location__, inputAsm))
        self.output = ""

    class Parser:
        def __init__(self, file):
            self.current_line = 0
            self.total_lines = file.readlines()
            self.current_text = self.total_lines[self.current_line].strip()
            self.symbol_address = 0
            self.ram_address = 15
        
        def has_more_lines(self):
            try:
                next_line = self.total_lines[self.current_line+1]
                if next_line:
                    return True
            except:
                return False
            
        def advance(self):

            # Handle pseudocodes and blank lines
            if self.current_text == '\n' or self.current_text.find("//") != -1 or self.current_text == '':
                self.current_line += 1
                self.current_text = self.total_lines[self.current_line].strip()

            else:
                self.current_line += 1
                self.current_text = self.total_lines[self.current_line].strip()
                
                # The symbol address doesn't increase when the instruction is L type
                if self.current_text[0] != '(':
                    self.symbol_address += 1

        def instructionType(self):
            if self.current_text != '\n' and self.current_text.find("//") == -1 and self.current_text != '':
                if self.current_text[0] == '@':
                    return 'A'
                elif self.current_text[0] == '(':
                    return 'L'
                else:
                    return 'C'
            
        def symbol(self):
            if self.instructionType() == 'A':
                index = self.current_text.find('\n')
                if index != -1:
                    return self.current_text[1:index]
                else:
                    return self.current_text[1:]
            elif self.instructionType() == 'L':
                index = self.current_text.find(')')
                return self.current_text[1:index]
            
        def dest(self):
            if self.instructionType() == 'C':
                index = self.current_text.find('=')
                if index != -1:
                    return self.current_text[:index]
                else:
                    return 'null'
                
        def comp(self):
            if self.instructionType() == 'C':
                if self.dest() != None:
                    dest_index = self.current_text.find('=')
                    comp_index = self.current_text.find(';')
                    if dest_index != -1 and comp_index != -1:
                        return self.current_text[dest_index+1:comp_index]
                    elif dest_index != -1 and comp_index == -1:
                        return self.current_text[dest_index+1:]
                    elif dest_index == -1 and comp_index != -1:
                        return self.current_text[:comp_index]
                    else:
                        return self.current_text
                
        def jump(self):
            if self.instructionType() == 'C':
                comp_index = self.current_text.find(';')
                if comp_index != -1:
                    return self.current_text[comp_index+1:]
                else:
                    return 'null'
                
    class Code:
        def dest(self, str):
            destMap = {'null':'000', 
                       'M':'001', 
                       'D':'010', 
                       'DM':'011', 
                       'A':'100', 
                       'AM':'101', 
                       'AD':'110', 
                       'ADM':'111'}
            if str in destMap:
                return destMap[str]
            else:
                return destMap['null']
            
        def comp(self, str):
            compMap = {'0': '0101010', 
                       '1': '0111111', 
                       '-1': '0111010', 
                       'D': '0001100', 
                       'A': '0110000', 
                       '!D': '0001101', 
                       '!A': '0110001', 
                       '-D': '0001111', 
                       '-A': '0110011', 
                       'D+1': '0011111', 
                       'A+1': '0110111', 
                       'D-1': '0001110', 
                       'A-1': '0110010', 
                       'D+A': '0000010', 
                       'D-A': '0010011', 
                       'A-D': '0000111', 
                       'D&A': '0000000', 
                       'D|A': '0010101', 
                       'M': '1110000', 
                       '!M': '1110001', 
                       '-M': '1110011', 
                       'M+1': '1110111', 
                       'M-1': '1110010', 
                       'D+M': '1000010', 
                       'D-M': '1010011', 
                       'M-D': '1000111', 
                       'D&M': '1000000', 
                       'D|M': '1010101'
                        }
            if str in compMap:
                return compMap[str]

        def jump(self, str):
            jumpMap = {'null': '000', 
                        'JGT': '001', 
                        'JEQ': '010', 
                        'JGE': '011', 
                        'JLT': '100', 
                        'JNE': '101', 
                        'JLE': '110', 
                        'JMP': '111'
                        }
            if str in jumpMap:
                return jumpMap[str]
            else:
                return jumpMap['null']
            
    class symbolTable:
        def __init__(self):
            self.symbol_table = {
                'R0': 0,
                'R1': 1,
                'R2': 2,
                'R3': 3,
                'R4': 4,
                'R5': 5,
                'R6': 6,
                'R7': 7,
                'R8': 8,
                'R9': 9,
                'R10': 10,
                'R11': 11,
                'R12': 12,
                'R13': 13,
                'R14': 14,
                'R15': 15,
                'SP': 0,
                'LCL': 1,
                'ARG': 2,
                'THIS': 3,
                'THAT': 4,
                'SCREEN': 16384,
                'KBD': 24576
            }

        def addEntry(self, symbol, address):
            self.symbol_table[symbol] = address

        def contains(self, symbol):
            if symbol in self.symbol_table:
                return True
            else:
                return False
            
        def getAddress(self, symbol):
            if symbol in self.symbol_table:
                return self.symbol_table[symbol]

assembler = Assembler("add/Add.asm")
parser = assembler.Parser(assembler.file)
code = assembler.Code()
symbolTable = assembler.symbolTable()

# Pass 1
for i in range(len(parser.total_lines)):
    if parser.instructionType() == 'L':
        symbolTable.addEntry(parser.symbol(), parser.symbol_address+1)
    if parser.has_more_lines():
        parser.advance()


# Pass 2
parser.current_line = 0
parser.current_text = parser.total_lines[parser.current_line].strip()

for i in range(len(parser.total_lines)):
    if parser.instructionType() == 'A':
        if parser.symbol() in symbolTable.symbol_table:
            number = symbolTable.symbol_table[parser.symbol()]
        elif parser.symbol().isnumeric():
            number = int(parser.symbol())
        else:
            symbolTable.addEntry(parser.symbol(), parser.ram_address+1)
            parser.ram_address += 1
            number = symbolTable.symbol_table[parser.symbol()]
        current_output = bin(number)[2:].zfill(16) + '\n'
        assembler.output += current_output

    if parser.instructionType() == 'C':
        baseline = '111'
        dest = parser.dest()
        comp = parser.comp()
        jump = parser.jump()
        current_output = baseline + code.comp(comp) + code.dest(dest) + code.jump(jump) + '\n'
        assembler.output += current_output
        
    if parser.has_more_lines():
        parser.advance()
        


print(symbolTable.symbol_table)
print(assembler.output)