import msvcrt

while True:
    key = msvcrt.getch()
    print(ord(key))
    if ord(key) == 27:
        break
