mark=int(input("Enter the mark:"))
if(mark>=90 and mark<=100):
    print("GRADE A")
elif(mark>=80 and mark<=89):
    print("GRADE B")
elif(mark>=70 and mark<=79):
    print("GRADE C")
elif(mark>=60 and mark<=69):
    print("GRADE D")
elif(mark<60):
    print("GRADE F")

else:
    print("INVALID MARK")



