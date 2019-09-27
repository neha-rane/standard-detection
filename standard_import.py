f = open("testcases/clsfun.py")
lineNo = 0
a = list(map(str,f))

i = 0

#for i in range(len(a)):
while i<len(a):
    temp = a[i]
    a[i] = temp.strip()
    if a[i]=="":
        i+=1
        continue
    elif a[i][0] =="\"" and a[i][1] =="\"" and a[i][2] =="\"":
        lineNo += 1
        i += 1
        while "\"\"\"" not in a[i]:
            lineNo += 1
            i += 1
        i += 1
        continue
    elif a[i][0] == "\'" and a[i][1] == "\'" and a[i][2] == "\'":
        i += 1        
        while "\'\'\'" not in a[i]:
            lineNo += 1
            i += 1
        i+= 1
        continue
    elif a[i][0] == "#":
        continue
    if 'import' not in a[i]:
        break
    lineNo += 1
    i += 1


while i<len(a):
    temp = a[i]
    a[i] = temp.strip()
    if a[i]=="":
        i+=1
        continue
    elif a[i][0] =="\"" and a[i][1] =="\"" and a[i][2] =="\"":
        lineNo += 1
        i += 1
        while "\"\"\"" not in a[i]:
            lineNo += 1
            i += 1
        i+=1
        continue
    elif a[i][0] == "\'" and a[i][1] == "\'" and a[i][2] == "\'":
        i += 1
        
        while "\'\'\'" not in a[i]:
            lineNo += 1
            i += 1
        i+= 1
        continue
    elif a[i][0] == "#":
        continue
    if 'import' in a[i] and ('#' not in a[i] and '"' not in a[i]):
        print("Import Statement placed wrongly on line number: ",i+1)
    i += 1
