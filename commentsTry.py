f = open("clsfun.py")
lineNo = 0
a = list(map(str,f))

for i in a:
    lineNo += 1
    if '#' in i:
        l = list(map(str,i))
        ind = l.index('#')
        after = len(l)-ind
        if l[ind+1] != " ":
            print("Add space between # and comment on line no: ",lineNo,".")
        if after > 72:
            print("Suggested to limit a comment to 72 characters on line no: ",lineNo,".")
        if l[ind-2] != " " and l[ind-1] != " ":
            print("Seperate code and comment with minimum 2 spaces on line no: ",lineNo,".")