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

