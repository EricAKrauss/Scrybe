if __name__ == "__main__":
    import config
else:
    try:
        from Scrybe import config
    except ImportError:
        import config

os = config.getOS()
if os == "Windows":
    import msvcrt

def get_input():
    os = config.getOS()
    if os == "Windows":
        while True:
            if msvcrt.kbhit():
                return str(msvcrt.getch())[-2]
    if os == "Unix":
        os.system("""bash -c 'read -s -n 1'""")

if __name__ == "__main__":
    key = get_input()
    print(key)
    a = input("...")



