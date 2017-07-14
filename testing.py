import config
import virtual_console

settings = config.settings()

console = virtual_console.cns(settings)
while True:
    console.map(0,0,["aaa", "axa", "aaa"])
    console.render()
