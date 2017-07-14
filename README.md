# Scrybe
A python library to provide extensive control over terminal and console output

## The cns object
The cns object (short for console) is the primary way that you will use Scrybe.
When created it can optionally take a settings object.  This will store most of the high-level
information that the cns object needs.  The cns object has a buffer attribute that is a two-
dimensional list of characters.  The best way to use this is to use the write and map methods.

### .write(row, col, val)
The write method will place the first character of the stringified val at row / col in the buffer.
The write method will then return True or False depending on whether or not this was successful.

### .map(row, col, 2dVal)
The map method takes a 2-dimension list of chars or a list of strings as the 2dVal argument.
It then iterates through the 2dVal from left to right, top to bottom, placing each character
in the buffer, starting at row / col.  This returns True if any characters were successfully written.
