import os

class Assembler:

    def __init__(self, inputAsm):
        self.__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.file = open(os.path.join(self.__location__, inputAsm))
        self.symbol_table = {}

    class Parser:
        def __init__(self):
            self.current_line = 0
            self.total_lines = self.file.readlines()
            self.current_text = ""
        
        def has_more_lines(self):
            next_line = self.total_lines[self.current_line+1]
            if next_line:
                return True
            else:
                return False
            
        def advance(self):
            self.current_line += 1
            self.current_text = self.total_lines[self.current_line]

        def instructionType(self):
            if self.current_text[0] == '@':
                return 'A'
            elif self.current_text[0] == '(':
                return 'L'
            else:
                return 'C'
            
        def symbol(self):
            if self.instructionType() == 'A':
                return self.current_text[1:]
            elif self.instructionType() == 'L':
                return self.current_text[1:-1]
            
        def dest(self):
            if self.instructionType() == 'C':
                index = self.current_text.find('=')
                if index != -1:
                    return self.current_text[:index]
                
        def comp(self):
            if self.instructionType() == 'C':
                if self.dest() != None:
                    dest_index = self.current_text.find('=')
                    comp_index = self.current_text.find(';')
                    return self.current_text[dest_index+1:comp_index]
                
        def jump(self):
            if self.instructionType() == 'C':
                comp_index = self.current_text.find(';')
                return self.current_text[comp_index+1:]



                    





 
                

