import keyword
import nltk     
class listdemo:
    import math	
    name=[]
    def getname(self):
        n=input("Enter a name:\n")
        self.name.append(n)
        self.menu()
    def display(self): #import statement
        print(self.name)
        self.menu()

        
    import numpy as np
    def search(self):
        n=input("Enter name to be searched in the list:\n")
        for i in self.name:
            if i==n:
                print("Name Found")
            else :
                print("Name not Found")
        self.menu()

    def exit_(self):
        exit
        
    import pandas
    def menu(self):
        print("1:New Name\n2:Display Name\n3:Search Name\n4:Exit")
        c=int(input("Enter your choice:"))
        if c==1:
            self.getname()
        if c==2:
            self.display()
        if c==3:
            self.search()
        if c==4:
            self.exit_()

ob=listdemo()
ob.menu()
