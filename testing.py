import config
import virtual_console
import colors

settings = config.settings()
settings.terminal_rows = 10

console = virtual_console.cns(settings)
console.map(0,0,["aaa", "axa", "aaa"], colors.RED)

line = ""
while True:
    console.render()
    print("Rendered")
    console.print(5,5,line, colors.CYAN, wrapping=1)
    line += virtual_console.get_input()
    
