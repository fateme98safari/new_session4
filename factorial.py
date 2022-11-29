import math

number=int(input("enter an integer number: "))
fact=1
i=1
while fact!=number:
       fact *= i
       i+=1

       if fact>number:
         print("no")
         break
       elif fact==number:
         print("yes")

           


