f = open("codes\\clsfun.py")
lineNo = 0
a = list(map(str,f))
for i in a:
    a[i] = a.strip()
    if a[i][0]=="\"\"\"":
        lineNo += 1
        while "\"\"\"" not in a[i]:
            lineNo += 1
        continue
    elif a[i][0] == "\'\'\'":
        while "\'\'\'" not in a[i]:
            lineNo += 1
        continue
    elif a[i][0] == "#":
        continue
    if 'import' not in i:
        break
    lineNo += 1
for i in range(lineNo, len(a)):
    if 'import' in a[i]:
        print("Import Statement placed wrongly on line number: ",i+1)
