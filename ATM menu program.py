balance=1000
print("1)check balance")
print("2)deposit")
print("3)withdraw")
print("4)exit")
choose=int(input("Enter your choice:"))
if(choose==1):
    print("your balance is:",balance)
elif(choose==2):
    amount=int(input("Enter your deposit:"))
    newbalance=balance+amount
    print("your new balance is:",newbalance)
elif(choose==3):
    amount=int(input("Enter your withdraw:"))
    if(amount<=1000):
        new_balance=balance-amount
        print("your new balance after withdrawal is",new_balance)
    else:
        print("insufficient amount")
elif(choose==4):
    print("thanks for using the ATM")
else:
    print("invalid choice")
    
    
