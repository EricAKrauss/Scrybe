import config
import os

class cns():
    def __init__(self, settings=None):
        ## Initialize Settings
        self.settings = settings
        if self.settings == None:
            self.settings = config.settings()

        ## Initialize Buffer
        self.clear_buffer()

    ## String Override
    def __str__(self):
        outStr = ""
        for r in self.buffer:
            for c in r:
                outStr += c
            outStr += "\n"

        ## Trims the last newline
        return outStr[:-1]

    ## Simplifies attribute calls
    def __call__(self, string):
        if hasattr(self, string):
            return getattr(self, string)
        if hasattr(self.settings, string):
            return getattr(self.settings, string)

    ## Maps val to the buffer at row, col
    ##   Can map 2d values
    ##   Starts at top left corner 
    ##     proceeds from left to right, top to bottom
    ##   Returns True if it successfully writes anything
    def map(self, row, col, val):
        success = False
        for r in range(len(val)):
            for c in range(len(val[r])):
                success = self.write(row+r, col+c, val[r][c]) or success

    ## Returns True if it can write a char to the buffer
    def write(self, r, c, v):
        buf = self.buffer
        if r < 0 or r >= len(buf):
            return False
        if c < 0 or c >= len(buf[r]):
            return False
        if hasattr(v, "__str__"):
            self.buffer[r][c] = str(v)[0]
            return True
        return False


    ## Clears the Console/Terminal
    def clear_console(self):
        if self("os") == "Windows":
            cmd = os.system('cls')
            return
        if self("os") == "Unix":
            cmd = os.system("clear")
            return
        return os.system("clear")

    ## Clears the internal text buffer
    def clear_buffer(self):
        args = [self("terminal_rows"),
                self("terminal_cols"),
                self("buffer_default")]
        self.buffer = init_array(*args)
        
    ## Clear the Console, print the buffer
    def render(self):
        self.clear_console()
        print(self)



def init_array(r, c, default=None):
    outArray = []
    for row in range(r):
        outArray.append([])
        for col in range(c):
            outArray[-1].append(default)
    return outArray
