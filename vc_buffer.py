if __name__ == "__main__":
    import config
else:
    try:
        from Scrybe import config
        from Scrybe import colors
    except ImportError:
        import config, colors

class vc_buffer():
    def __init__(self, settings=None):
        if settings != None:
            self.settings = settings
        else:
            self.settings = config.settings()
        self.clear_buffer()

    def __iter__(self):
        for r in self.buffer:
            yield r

    def __getattr__(self, attr):
        return getattr(self.settings, attr)
    
    ## Clears the internal text buffer
    def clear_buffer(self):
        args = [self.terminal_rows,
                self.terminal_cols,
                self.buffer_default, colors.DEFAULT]
        self.buffer = init_buffer(*args)

    ## Maps val to the buffer at row, col
    ##   Map is a 2d list of strings or characters
    ##   Starts at top left corner 
    ##     proceeds from left to right, top to bottom
    ##   Returns True if it successfully writes anything
    def map(self, row, col, val, color=None):
        success = False
        for r in range(len(val)):
            for c in range(len(val[r])):
                success = self.place(row+r, col+c, val[r][c], color) or success
        return success

    ## Maps a color to one space or a quadratic area of
    ##   a size w*h
    ##   Starts at r1 / c1 and progresses by w then by h
    ##   color can be a 2d list of colors.  Will map
    ##     each color to the buffer in place of the given color
    ##   if the area that is being mapped is larger than the 2d
    ##     list of colors, the first color in the map will be used
    def map_color(self, color, r1, c1, w=1, h=1):
        success = False
        isColorMap = hasattr(color[-1], "__len__")
        for row in range(r1, r1+h):
            for col in range(c1, c1+w):
                canPlace = (row in range(len(self.buffer)) and col in range(len(self.buffer[row])))
                success = canPlace or success
                if not isColorMap:
                    self.buffer[row][col][-1] = color
                else:
                    if row-r1 in range(len(color)) and col-c1 in range(len(color[row-r1])):
                        self.buffer[row][col][-1] = color[row-r1][col-c1]
                    else:
                        print(row-r1 % len(color), col-c1, col-c1 % len(color[row-r1 % len(color)]) )
                        self.buffer[row][col][-1] = color[row-r1 % len(color)][col-c1 % len(color[row-r1 % len(color)])]
        return success

    ## Print will write a string or a list of characters
    ##   to the buffer starting at row, col.
    ##   Print has three wrapping modes:
    ##     -1: Doesn't wrap at all
    ##      0: Wrap to the start of the next line
    ##      1: Wrap to the next line starting at r
    def write(self, r, c, v, color=None, wrapping=-1):
        col = c
        row = r
        success = False
        while len(v) > 0:
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
            
            success = self.place(row, col, char, color) or success
            col += 1
        return success

    ## Returns True if it can write a char to the buffer
    def place(self, r, c, v, color=None):
        buf = self.buffer
        if r < 0 or r >= len(buf):
            return False
        if c < 0 or c >= len(buf[r]):
            return False
        if hasattr(v, "__str__"):
            if color != None:
                self.buffer[r][c] = [str(v)[0], color]
            else:
                self.buffer[r][c] = [str(v)[0], colors.DEFAULT]
            return True
        return False


def init_buffer(r, c, char=None, color=colors.DEFAULT):
    outArray = []
    for row in range(r):
        outArray.append([])
        for col in range(c):
            outArray[-1].append([char, color])
    return outArray
