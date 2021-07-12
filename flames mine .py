#my flames python program
a=list(input("Enter the first name: ").lower().replace(" ",""))
at=str("".join(a)).upper()
b=list(input("Enter the first name: ").lower().replace(" ",""))
bt=str("".join(b)).upper()
go=True
while go:
    for i in a:
        if i in b:
            a.remove(i)
            b.remove(i)
            go=True
            break
        else:
            go=False
count=(len(a)+len(b))
print("\n","Your flames number: ",count)
flames=["FRIEND","LOVE","AFFECTION","MARRIAGE","ENEMY","SIBLING"]
while count>6:
    count=count-6
print("\n \n")
if flames[count-1]=="MARRIAGE":
    print(at,"will MARRY",bt)
else:
    print(at,"will be the",flames[count-1],"of",bt)
input()
input()


