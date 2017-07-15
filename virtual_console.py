import config
import os, sys
import colors
from user_input import get_input

class cns():
    def __init__(self, settings=None):
        ## Initialize Settings
        self.settings = settings
        if self.settings == None:
            self.settings = config.settings()

        ## Initialize Buffer
        self.clear_buffer()

    ## Simplifies attribute calls
    def __call__(self, string):
        if hasattr(self, string):
            return getattr(self, string)
        if hasattr(self.settings, string):
            return getattr(self.settings, string)

    ## Maps val to the buffer at row, col
    ##   Map is a 2d list of strings or characters
    ##   Starts at top left corner 
    ##     proceeds from left to right, top to bottom
    ##   Returns True if it successfully writes anything
    def map(self, row, col, val, color=None):
        success = False
        for r in range(len(val)):
            for c in range(len(val[r])):
                success = self.write(row+r, col+c, val[r][c], color) or success

    ## Print will write a string or a list of characters
    ##   to the buffer starting at row, col.
    ##   Print has three wrapping modes:
    ##     -1: Doesn't wrap at all
    ##      0: Wrap to the start of the next line
    ##      1: Wrap to the next line starting at r
    def print(self, r, c, v, color=None, wrapping=-1):
        col = c
        row = r
        success = False
        while len(v) > 0:
            print(v)
            char = v[0]
            v = v[1:]

            if col >= len(self.buffer[row]):
                row += 1
                if wrapping == -1:
                    return success
                if wrapping == 0:
                    col = 0
                if wrapping == 1:
                    col = c
            if row >= len(self.buffer):
                return success
            
            success = self.write(row, col, char, color) or success
            col += 1
        return success

    ## Returns True if it can write a char to the buffer
    def write(self, r, c, v, color=None):
        buf = self.buffer
        if r < 0 or r >= len(buf):
            return False
        if c < 0 or c >= len(buf[r]):
            return False
        if hasattr(v, "__str__"):
            if color != None:
                self.buffer[r][c] = (str(v)[0], color)
            else:
                self.buffer[r][c] = (str(v)[0], colors.DEFAULT)
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
                (self("buffer_default"), colors.DEFAULT)]
        self.buffer = init_array(*args)
        
    ## Clear the Console, print the buffer
    def render(self):
        self.clear_console()
        self.print_frame()

    ## Prints the frame to the console in color
    def print_frame(self):
        activeColor = colors.DEFAULT

        for r in self.buffer:
            for c in r:
                if c[1] != activeColor:
                    activeColor = c[1]
                    sys.stdout.write(activeColor)

                print(c[0], end="")
            print("\n", end="")
        print()



def init_array(r, c, default=(None, colors.DEFAULT)):
    outArray = []
    for row in range(r):
        outArray.append([])
        for col in range(c):
            outArray[-1].append(default)
    return outArray
