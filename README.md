# Scrybe
A python library to provide extensive control over terminal and console output

## The cns object
The cns object (short for console) is the primary way that you will use Scrybe.
When created it can optionally take a settings object.  This will store most of the high-level
information that the cns object needs.  The cns object has a buffer attribute that is a two-
dimensional list of characters.  The best way to use this is to use the write and map methods.

### Initializing the Object
To start using a cns object: 
```
import Scrybe.virtual_console

//You may optionally include a settings object as an argument
console = virtual_console.cns()
```

### .place(row, col, val, color=colors.DEFAULT)
The place method will place the first character of the stringified val at row / col in the buffer.
The place method will then return True or False depending on whether or not this was successful.

### .write(row, col, value, color=colors.DEFAULT, wrapping=0)
The write method will insert a string or a list of characters into the buffer starting at row / col.  
Where map will cut off anything outside of the buffer, .write will wrap around to the start of the 
next row and continue.  The behavior of this can be modified by setting the wrapping key-argument.
<br>`wrapping=-1` does not wrap.
<br>`wrapping=0` wraps to the start of the next line.
<br>`wrapping=1` wraps to col instead of the beginning.

### .map(row, col, 2dVal, color=colors.DEFAULT)
The map method takes a 2-dimension list of chars or a list of strings as the 2dVal argument.
It then iterates through the 2dVal from left to right, top to bottom, placing each character
in the buffer, starting at row / col.  This returns True if any characters were successfully 
written and False otherwise.

### writing colored text
Stored in the buffer with each character is an ANSI color sequence.  For your convenience, 
many of these sequences are stored in `colors.py`.  By default, all characters are stored 
in the buffer with `colors.DEFAULT`.

### .render()
The render method will clear the console or terminal depending on your OS and then print the buffer.
This does not clear the buffer.  When rendering starts, the "active color" is set to `colors.DEFAULT` 
and that color is written to the stdout stream.  Whenever a color other than the active color is detected 
that color is written to stdout and it becomes the active color.

### .clear_buffer()
The clear_buffer method will reset the buffer to be a 2d list of values.  The default values in the
new buffer are equal to `settings.buffer_default` and the dimensions are equal to `settings.terminal_rows`
and `settings.terminal_cols`.

### .clear_console()
Clears the console / terminal using `os.system("clear")` on Unix and `os.system("clr")` on Windows.
