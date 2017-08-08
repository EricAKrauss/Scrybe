import os, sys
from math import floor

if __name__ == "__main__":
    import config, colors
    import user_input, vc_buffer
else:
    from Scrybe import config, colors
    from Scrybe import user_input
    from Scrybe import vc_buffer

class virtual_console():
    def __init__(self, settings=None, buffer=None):
        ## Initialize Settings
        self.settings = settings
        if self.settings == None:
            self.settings = config.settings()

        ## Initialize Buffer
        self.buffer = buffer
        if self.buffer == None:
            self.buffer = vc_buffer.vc_buffer(self.settings)
        else:
            ##Override settings with included buffer's settings
            self.settings = self.buffer.settings

        ## Define get_input method
        self.get_input = user_input.get_input

    ## Simplifies attribute calls
    def __getattr__(self, string):
        if hasattr(self.settings, string):
            return getattr(self.settings, string)
        else:
            return getattr(self.buffer, string)

    def __str__(self):
        outString = ""
        activeColor = colors.DEFAULT
        outString += activeColor
        for row in self.buffer:
            for col in row:
                if col[-1] != activeColor:
                    activeColor = col[-1]
                    outString += activeColor
                outString += col[0]
            outString += "\n"
        return outString[:-1]

    ## Clears the Console/Terminal
    def clear_console(self):
        if self.os == "Windows":
            cmd = os.system('cls')
            return
        if self.os == "Unix":
            cmd = os.system("clear")
            return
        return os.system("clear")
        
    ## Clear the Console, print the buffer
    def render(self):
        self.clear_console()
        self.print_frame()

    ## Prints the frame to the console in color
    def print_frame(self):
        activeColor = colors.DEFAULT
        sys.stdout.write(activeColor)

        for r in self.buffer:
            for c in r:
                if c[1] != activeColor:
                    activeColor = c[1]
                    sys.stdout.write(activeColor)

                print(c[0], end="")
            print("\n", end="")
        print()
