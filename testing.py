a = '!translate -l de ko ja -n 50 -t "keepo"'
args = a.split('-')
args = args[1:]
langs = []
n = -1
text = ""
for elem in args:
    elem = "-" + elem.strip()
    if elem.find('-l') != -1:
        templangs = elem.split(' ')[1:]
        print(templangs)
    if elem.find('-n') != -1:
        n = elem.split(' ')[1]
        print(n)
    if elem.find('-t') != -1:
        text = elem.split(' ')[1]
        print(text)