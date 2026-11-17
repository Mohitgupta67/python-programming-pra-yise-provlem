#this programe check whether the number is #prime number or not


num = int(input("Enter the desired number \n"))

if num <= 1:
    print("not a prime number")
else:
    for i in range(2 , num):
     if num % i == 0:
        print("not a prime number")
        break
    else:
        print("prime number")