secret=26
a=int(input("guess the number:"))
if(secret==a):
    print("correct!you guessed it")
elif(secret>=a):
    print("Too low")
elif(secret<=a):
    print("Too high")
else:
    print("invalid")
