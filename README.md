# Scrybe
A python library to provide extensive control over terminal and console output

## The virtual_console object
The virtual_console object is the primary way that you will use Scrybe.
When created it can optionally take a settings object.  This will store most of the high-level
information that the virtual_console object needs.  The virtual_console object has a buffer attribute that is a two-
dimensional list of characters.  The best way to use this is to use the write and map methods.

### Initializing the Virtual Console Object
To start using a virtual_console object: 
```
import Scrybe.virtual_console

//You may optionally include a settings object as an argument
//You may include a vc_buffer object as an argument, but this will set the newly created
//  virtual_console's settings object to point to the included vc_buffer's settings object
console = virtual_console.virtual_console()
```

### Using the Virtual Console

#### .render()
The render method will clear the console or terminal depending on your OS and then print the buffer.
This does not clear the buffer.  When rendering starts, the "active color" is set to `colors.DEFAULT` 
and that color is written to the stdout stream.  Whenever a color other than the active color is detected 
that color is written to stdout and it becomes the active color.

#### .clear_console()
Clears the console / terminal using `os.system("clear")` on Unix and `os.system("clr")` on Windows.

### Methods for User Input

#### .get_input()
Pauses the application and waits for any non-modifier key to be pressed.  This does not currently return 
`<SHIFT>`, `<CTRL>`, `<TAB>`, etc presses, but will return both capital letters and symbols.  
<br>In the future, I would like to be able to return these special keys instead.  I would also like to 
find a way to optionally spin off the get_input() call as a separate thread or task so that the application 
can continue while waiting for user input.  This would likely take the form of a user_input object.

#### .query(text="Press Enter to Continue...") //Not made yet
Pauses the application and writes a box with the provided text to the screen.  The box will contain an empty 
line that the user writes to.  The user can delete text with backspace.  The written string will be returned 
when the user presses enter.

## The VC_Buffer Object
Sits underneath every virtual_console object.  Any method of a buffer object can be executed directly to the 
virtual_console object.  The call will be passed along from the virtual_console to its buffer object using
the __getattr__ implementation.

### Initializing a VC_Buffer Object
To start using a vc_buffer object
```
import Scrybe.vc_buffer()

//You may optionally include a settings object as an argument
buffer = vc_buffer.vc_buffer()
```
It is recommended that you use a virtual_console object to retrieve and interpret the contents of a vc_buffer object.

### Methods for Drawing to the Buffer

#### .place(row, col, val, color=colors.DEFAULT)
The place method will place the first character of the stringified val at row / col in the buffer.
The place method will then return True or False depending on whether or not this was successful.

#### .write(row, col, value, color=colors.DEFAULT, wrapping=0)
The write method will insert a string or a list of characters into the buffer starting at row / col.  
Where map will cut off anything outside of the buffer, .write will wrap around to the start of the 
next row and continue.  The behavior of this can be modified by setting the wrapping key-argument.
<br>`wrapping=-1` does not wrap.
<br>`wrapping=0` wraps to the start of the next line.
<br>`wrapping=1` wraps to col instead of the beginning.

#### .map(row, col, 2dVal, color=colors.DEFAULT)
The map method takes a 2-dimension list of chars or a list of strings as the 2dVal argument.
It then iterates through the 2dVal from left to right, top to bottom, placing each character
in the buffer, starting at row / col.  This returns True if any characters were successfully 
written and False otherwise.

#### .map_buffer(row, col, buffer) // Not yet implemented
This method will take a buffer and write its contents to the called object's buffer.  This 
will be implemented after the buffer is split into its own object that the virtual_console 
object will manage.

#### .map_color(color, row, col, width=1, height=1)
The map_color method takes a single color value or a 2d list of color values.  It then maps
the color/colors to the buffer starting at row / col.  If a single color is given, it will
map that color to the buffer in each traversed spot.  If a 2d list of colors is given, the
method will map colors to the buffer according to the list up to width-by-height.  If the
width / height are larger than the given 2d list of colors, the colors will be tiled.

#### writing colored text
Stored in the buffer with each character is an ANSI color sequence.  For your convenience, 
many of these sequences are stored in `colors.py`.  By default, all characters are stored 
in the buffer with `colors.DEFAULT`.  A list of ANSI sequences can be found [Here](http://bluesock.org/~willg/dev/ansi.html).

#### .clear_buffer()
The clear_buffer method will reset the buffer to be a 2d list of values.  The default values in the
new buffer are equal to `settings.buffer_default` and the dimensions are equal to `settings.terminal_rows`
and `settings.terminal_cols`.

## The Future
By version 1.0 the following will have been accomplished:
1. Write automated tests for feature set
2. .get_input must work on Linux systems
3. .query must be implemented
