f = open("test1.py")
lineNo = 0
a = list(map(str,f))

binary = ['+','-','/','*','=','%']

i = 0
while i < len(a):
    lineNo += 1
    temp = a[i]
    for j in binary:
        if j in temp:
            ind = temp.index(j)
            #print(ind)
            if temp[ind-1] != " " or temp[ind+1] != " ":
                print("Recommended Space before and after binary operater on line no: ",lineNo)

    i += 1