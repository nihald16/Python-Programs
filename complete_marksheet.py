#function for getting input from user
def get_input():
    name=input("enter name :")
    clg =input("enter clg name:")
    Date=input("Enter marksheet creation date in (dd/mm/yy) same format :")
    subject=['c','c++','java','python','c#']
    subject_marks={}

    for i in subject:
        score=float(input(f"enter marks of {i} here: "))
        subject_marks[i]=score
    
    return name,clg,Date,subject_marks

    #print marksheet 
def put_output(name,clg,Date,subject_marks):

    print(" "*20,"NAME         :",name)
    print(" "*20,"COLLEGE NAME :",clg)
    print("DATE :",Date)
    print()
    print("="*60)
    print("subject","total marks","obtain marks",sep=" "*10)

    for s,m in subject_marks.items():
        l=int(len(s))
        print(" ",s," "*(15-l),"100"," "*13,m)
        print()

    for m in subject_marks.values():   
        if m>35:
            result="PASS"
        else:
            result="FAIL"
            break

    obtain=sum(subject_marks.values())
    print("="*60)
    print("Total       : 500",end=" "*10),print("Final Result :",result)
    print("Obtain Marks:",obtain)
    print("percentage  :",obtain/5)
    

name,clg,date,subject_marks=get_input()
put_output(name,clg,date,subject_marks)
put_output(name,clg,date,subject_marks)
