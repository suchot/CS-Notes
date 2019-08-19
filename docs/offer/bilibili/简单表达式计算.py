while True:
    s = input()
    if s=='END':
        break
    eval('print('+s+')')
    