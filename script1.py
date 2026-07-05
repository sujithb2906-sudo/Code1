
 num=int(input("Enter how many numbers you want to sum: "))
 if num<=0:
     raise ValueError("Enter a positive number")
 elif num==1:
     raise ValueError("Sorry,no single number")
 elif num>=10:
     raise ValueError("Sorry,number is too large")

 sum = 0
 for i in range(num):
     chances = 3
     for j in range(chances):
         n = int(input("Enter the numbers: "))
         chances = chances - 1;
         if n < 0:
             print("Sorry, the number you entered is negative")
             print("You have only {chances} chances", chances)
             if (chances == 0):
                 raise Error("Sorry, you have only {} chances".format(chances))
         else:
             sum = sum + n
             break

 print("sum is", sum)

 avg=sum/num
 print("average is", avg)

 if sum%2==0:
     print("Even number")
 else:
     print("odd number")

count=0

for i in range(2, sum//2):
    if sum%i==0:
        count=count+1
if count==0:
    print("prime number")
else:
    print("not prime number")
