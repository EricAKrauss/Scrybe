import os, sys

class settings:
    def __init__(self):
        self.os = self.getOS()
        self.terminal_cols = 30
        self.terminal_rows = 20
        self.buffer_default = "."

    def getOS(self=None):
        os = sys.platform[:3]
        if os == "win":
            return "Windows"
        if os == "lin":
            return "Unix"
        return sys.platform
