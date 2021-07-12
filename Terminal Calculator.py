#program to a calculator
#hareesh's calc
print(" Welcome to HAREESH's calculator \n Press ENTER to continue ")
www=input()
print("Enter your choice")
print("1. ADD            (1)")
print("2. SUB            (2)")
print("3. MULTIPLY       (3)")
print("4. DIVISION       (4)")
print("Enter your choice")
a=int(input())
if(a==1)or(a==11):
   print("ADDITION")
   print("enter no 1:")
   b=int(input())
   print("enter no 2")
   c=int(input())
   temp=b+c
   print("the answer is :",temp)
   input()
elif(a==2):
    print("SUBRACTION")
    print("enter no 1:")
    b=int(input())
    print("enter no 2:")
    c=int(input())
    temp=b-c
    print("the answer is :",temp)
    input()
elif(a==3):
    print("MULTIPLICATION")
    print("enter no 1:")
    b=int(input())
    print("enter no 2:")
    c=int(input())
    temp=b*c
    print("the answer is :",temp)
    input()
elif(a==4):
    print("DIVISION")
    print("enter no 1:")
    b=int(input())
    print("enter no 2:")
    c=int(input())
    temp=b/c
    print("the answer is :",temp)
    input()
else:
    print("invalid input")
