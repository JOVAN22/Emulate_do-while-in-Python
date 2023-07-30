
#ENUMERATE DO WHILE LOOP:
i=int(input("Enter the number"))

while True:
    print(i)
    i=i+1
    if(i<=100):
        print("i will be executed",end="")
        print("since ", i , " is less than 100")
    else:
        break
