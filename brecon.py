# for i in range(11):
#     if(i==5):
#         break
#     print("5 X", i + 1, "=", 5 * (i + 1))
# print("Loop ko chod kar nikal gaya")
# for i in range(11):
#     if (i==5):
#         print("Skip the iteration")
#         continue
#     print("5 X",i,"=",5*i)

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