
import machenical.subjects as me
import CS.subjects as cs
import IT.subjects as it
import Civil_Engg.subjects as ce

class Exam:
    def __init__(self):
        self.Name=None
        self.Class=None
        self.Clg=None
        self.Roll=None
        self.subj=None
        self.login()


    def login(self):
        self.uname=input("Enter user name :")
        self.Password=input("Enter Password :")

        if self.uname==self.Password:
            print("you succesfully login")
            self.info()

        else:
            print("login fail")

    def info(self):
        print()
        self.Name=input("Enter name :")
        self.Class=input("Enter class :")
        self.Clg=input("Enter college :")
        self.Roll=input("Enter Roll no :")

        print("choose Branch for giving Exam\n")
        print("1.Machenical Engineering")
        print("2.Information technology")
        print("3.Computer Science") 
        print("4.Civil Engineering") 
        print()

        choice=int(input("Enter your choice :"))
        if choice==1:
            self.subj=self.Branch(me)

        elif choice==2:
            self.subj=self.Branch(it)

        elif choice==3:
            self.subj=self.Branch(cs)
        else:
            self.subj=self.Branch(ce)

    def Branch(self,branch):
        print()
        print("1.First Semester ")
        print("2.Second Semester ")
        print()
        choice=int(input("Enter your choice :"))
        print()
        if choice==1:
            #FIrst semester subject
            
            return branch.First_sem()
        else:
            #second semester subject
            return branch.second_sem()
            


class Calculation(Exam):

    def __init__(self):
        Exam.__init__(self)
        print()
        print("you want to calculate your mark choose Yes or No")
        print()

        choice=input("Enter yes or no :")
        if choice=='yes' or choice=='Yes':
            self.calci()
        else:
            exit()
        
    def calci(self):
        self.subj_mark=[]
        for i in range(0,len(self.subj)):
            mark=float(input(f"Enter mark of {self.subj[i]} :" ))
            self.subj_mark.append(mark)

        for i in self.subj_mark:
            if i>=40:
                self.result='Pass'
            else:
                self.result='Fail'

        self.total=len(self.subj)*100
        self.obtained=sum(self.subj_mark)
        self.percent=self.obtained/len(self.subj)


class Result(Calculation):
    def __init__(self):
        Calculation.__init__(self)
        print("="*60,"\n")
        print(" "*10,"college :",self.Clg,"\n")
        print("="*60)

        print("|"," "*8,"Student Name   :",self.Name," "*(29-len(self.Name)),"|")
        print("|"," "*8,"class          :",self.Class," "*(29-len(self.Class)),"|")
        print("|"," "*8,"rollno         :",self.Roll," "*(29-len(str(self.Roll))),"|")

        print("="*60)
        print()
        
        print(" ","Subject Name    :  Total Marks   :   Obtained marks   :")
        print(" ","-"*55)
        
        for i in range(0,len(self.subj)):
            l=len(self.subj[i])
            print(" ",self.subj[i]," "*(14-l),":\t100 "," "*5,":\t",self.subj_mark[i],"\t\t:")

        print("="*60)
        print()
        print(" result Status :",self.result)
        print(" total Mark    :",self.total)
        print(" Obtained Mark :",self.total)
        print(" percent       :",self.percent)
        print("="*60)


r=Result()