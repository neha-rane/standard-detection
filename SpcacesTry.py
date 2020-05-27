f = open("clsfun.py")
lineNo = 0
a = list(map(str,f))

i = 0
while i < len(a):
    temp = a[i]
    temp = temp.strip()
    #print(temp)
     
    if "class" in temp:
        if "\\n" not in a[i+1]:
            print("Suggested Blank line between class definition next loc.")
    i += 1
            

