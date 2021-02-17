#program for printing table
table= int(input("enter the digit for table you want:\n"))
for i in range(1,11):
    print("multiplication of ",str(table) + "x" + str(i) + " is :",table*i)


#program for printing table in reverse order
table= int(input("enter the digit for table you want:\n"))
for i in range(10,0,-1):
    print("multiplication of ",str(table) + "x" + str(i) + " is :",table*i)