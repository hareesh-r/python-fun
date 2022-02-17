import random
string = "abcdefghijklmnopqrstuvwxyz"
string = list(string)
string2 = "0123456789"
string2 = list(string2)
weight = [5 for _ in range(len(string))] + [2 for _ in range(len(string2))]
fileholder = open("classcodes.txt","w")
counter=0
tempArr=[]
while counter<=100000:
    a = random.choices(string+string2,weights=weight,k=7)
    temp = "".join(str(i) for i in a)
    if temp not in tempArr:
        fileholder.write(temp+"\n")
        print(*a," ",temp,end="\n",sep="")
        counter+=1
    tempArr.append(temp)
