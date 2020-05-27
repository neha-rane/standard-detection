import tkinter 
import webbrowser
import os,inspect	
from tkinter import Menu
from tkinter import Text
from tkinter import Scrollbar
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Tk
from tkinter import * 

class standardDetectionIde:

    warning = []
    ideRoot = Tk()
    ideRoot.geometry("1000x700")
    ideWidth = 1000
    ideHeight = 1000
    ideTextArea = Text(ideRoot)
    ideNumberLine=Text(ideRoot)
    ideMenuBar = Menu(ideRoot)
    ideFileMenu = Menu(ideMenuBar, tearoff=0)
    ideTerminalMenu = Menu(ideMenuBar, tearoff=0)
    ideHelpMenu = Menu(ideMenuBar, tearoff=0)
    ideScrollBar = Scrollbar(ideTextArea)
    testFile = None
    # Line numbers widget
    #ideTextArea.line_numbers_canvas = tkinter.Canvas(ideTextArea, width=30, bg='#555555', highlightbackground='#555555', highlightthickness=0)
    #ideTextArea.line_numbers_canvas.pack(side=tkinter.LEFT, fill=tkinter.Y)

    
    def check(self,f):  # main standard detection code
        lineNo = 0
        line = 0
        a = list(map(str,f))
        i = 0


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

        
        while i<len(a):  #print("exit  loop 1")
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
                #i+=1
                continue
            elif a[i][0] == "\'" and a[i][1] == "\'" and a[i][2] == "\'":
                i += 1
                
                while "\'\'\'" not in a[i]:
                    lineNo += 1
                    i += 1
                #i+= 1
                continue
            elif a[i][0] == "#":
                i+=1
                continue
            if 'import' in a[i] and ('#' not in a[i] and '"' not in a[i] and '\'' not in a[i]):
                warn = "Import Statement placed wrongly on line number: " + str(i + 1)
                self.warning.append(warn)
            i += 1

        k = 0
    
        while k < len(a):
            line += 1
              
            if '#' in a[k]:  # Comments 
                l = list(map(str,a[k]))
                ind = l.index('#')
                after = len(l) - ind
                if l[ind + 1] != " ":
                    warn = "Add space between # and comment on line no: " + str(line)
                    self.warning.append(warn)
                elif after > 72:
                    warn = "Suggested to limit a comment to 72 characters on line no: " + str(line)
                    self.warning.append(warn)
                elif ((ind + 1) % 4 == 0) and (l[ind + 1] == " "):
                    break
                elif l[ind - 2] != " " and l[ind-1] != " ":
                    warn = "Seperate code and comment with minimum 2 spaces on line no: " + str(line)
                    self.warning.append(warn)

            
            paranthesis = [')','(','[',']']
            comma = [',',';', ':']
            binary = ['+','-','/','*','%','=']
            assignment = ['!=','==','+=','-=','/=','*=','%=']
            temp = a[k]

            
            
            for j in paranthesis:  # Whitespaces around paranthesis
                if j in temp:
                    ind = temp.index(j)
                    lc = len(temp)
                    if ((ind == lc) or (ind == lc - 1) or (ind == lc - 2) or (ind == 0) or (ind == (-1))):
                        break
                    elif ((temp[ind - 2] in binary) or (temp[ind + 2] in binary)):
                        break
                    elif(temp[ind - 1] == " " or temp[ind - 1] == " "):
                        warn = "Avoid Whitespaces before or after paranthesis on line no: " + str(line)
                        self.warning.append(warn)

            
            for l in comma:  # Whitespaces around Comma
                if l in temp:
                    ind = temp.index(l)
                    # print(ind)
                    if temp[ind - 1] == " ":
                        warn = "Avoid Whitespaces before a comma, semicolon or colon on line no: " + str(line)
                        self.warning.append(warn)
                        break
            
            
            #temp = a[k]
            #temp1 = temp.strip()
            #if "class" in temp1:  # Checking new line between Class and following LOC
            #   if "\n" not in a[k + 1]:
            #        warn = "Suggested Blank line between class definition and next line of code, check line No: "+str(line)
            #        self.warning.append(warn)
            
        
            for j in assignment:  # Checking spaces around Binary Operators
                if j in temp:
                    ind = temp.index('=')
                    # print(ind)
                    v = (ind - 1) + ind
                    if v in assignment:
                        if temp[ind - 2] != " " or temp[ind + 1] != " ":
                            warn = "Recommended Space before and after assignment operater on line no: " + str(line)
                            self.warning.append(warn)
                    elif j in binary and temp:
                        ind = temp.index(j)
                        if temp[ind - 1] != " " or temp[ind + 1] != " ":
                            warn = "Recommended Space before and after binary operater on line no: " + str(line)
                            self.warning.append(warn)


            k += 1

    def __init__(self,**kwargs):
        # try:
            # self.ideRoot.wm_iconbitmap("Notepad.ico")
        # except KeyError:
            # pass
        try:
            self.ideWidth = kwargs['width']
        except KeyError:
            pass
        try:
            self.ideHeight = kwargs['height']
        except KeyError:
            pass
        
        self.ideRoot.title("Standard Detection IDE")
        self.ideRoot.grid_rowconfigure(0, weight = 1)
        self.ideRoot.grid_columnconfigure(0, weight = 1)
        self.ideTextArea.grid(sticky = N + E + S + W)
        self.ideFileMenu.add_command(label = "New",command=self.newFile)
        self.ideFileMenu.add_command(label = "Open",command=self.ideOpenFile)
        self.ideFileMenu.add_command(label = "Save",command=self.saveFile)
        self.ideFileMenu.add_separator()
        self.ideFileMenu.add_command(label = "Exit", command=self.quitApplication)
        self.ideMenuBar.add_cascade(label = "File", menu=self.ideFileMenu)
        self.ideTerminalMenu.add_command(label = "Check File", command=self.runFile)
        self.ideMenuBar.add_cascade(label = "Run", menu=self.ideTerminalMenu)
        self.ideHelpMenu.add_command(label = "About SD-IDE", command=self.ideShowAbout)
        self.ideHelpMenu.add_command(label = "Read About Standards", command=self.ideShowStandards)
        self.ideMenuBar.add_cascade(label = "Help", menu=self.ideHelpMenu)
        self.ideRoot.config(menu = self.ideMenuBar)
        self.ideScrollBar.pack(side = RIGHT,fill = Y)
        self.ideScrollBar.config(command=self.ideTextArea.yview)
        self.ideTextArea.config(yscrollcommand=self.ideScrollBar.set)

    def quitApplication(self):
        self.ideRoot.destroy()

    def ideShowStandards(self):
        webbrowser.open("https://www.python.org/dev/peps/pep-0008/")

    def ideShowAbout(self):
	    messagebox.showinfo("SD-IDE","A standard detection IDE for Python made SPIT students.")

    def ideOpenFile(self):	
        self.testFile = filedialog.askopenfilename(defaultextension = ".py",filetypes = [("All Files","*.*"),("Text Documents","*.txt")])
        if self.testFile == "":
            self.testFile = None
        else:
            self.ideRoot.title(os.path.basename(self.testFile) + " - SD-IDE")
            self.ideTextArea.delete(1.0,END)
            file = open(self.testFile,"r")
            self.ideTextArea.insert(1.0,file.read())
            file.close()

    def newFile(self):
        self.ideRoot.title("Untitled - SD-IDE")
        self.testFile = None
        self.ideTextArea.delete(1.0,END)  

    def saveFile(self):
        if self.testFile == None:
            self.testFile = filedialog.asksaveasfilename(initialfile = 'Untitled.py', defaultextension = ".py",filetypes=[("All Files","*.*"),("Text Documents","*.txt")]) 
            if self.testFile == "":
                self.testFile = None
            else:
                file = open(self.testFile,"w")
                file.write(self.ideTextArea.get(1.0,END))
                file.close()
                self.ideRoot.title(os.path.basename(self.testFile) + " - SD-IDE")
        else:
            file = open(self.testFile,"w")
            file.write(self.ideTextArea.get(1.0,END))
            file.close()

    def runFile(self):
        self.saveFile()
        file = open(self.testFile)
        self.check(file)
        message = ""
        for i in range(len(self.warning)):
            message += self.warning[i] + "\n"
        self.popupmsg(message)
        file.close()  

    def run(self):
		 
        self.ideRoot.mainloop()   # Run main application  

    def popupmsg(self,msg):
        root = Tk()
        root.title("Recommendations")
        t = Text(root,height = 30,width = 100)
        t.pack()
        t.insert(END,msg)
        root.mainloop()

ide = standardDetectionIde(width = 600,height = 400)
ide.run()















































