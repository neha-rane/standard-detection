f = open("codes\\clsfun.py")
lineNo = 0
a = list(map(str,f))
for i in a:
    if 'import' not in i:
        break
    lineNo += 1
for i in range(lineNo, len(a)):
    if 'import' in a[i]:
        print("Import Statement placed wrongly on line number: ",i+1)
