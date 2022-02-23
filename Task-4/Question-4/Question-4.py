# Q4.Write a program to check if the given number is a palindrome number.
x=int(input("Enter a number:"))
sid=x
r=0
while(x>0):
    dig=x%10
    r=r*10+dig
    x=x//10
if(sid==r):
    print("True")
else:
    print("Flase")