num=int(input("enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("the given number is polindrome")
else:
    print("the given number is not polindrome")