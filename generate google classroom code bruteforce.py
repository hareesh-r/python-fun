import random
string = "abcdefghijklmnopqrstuvwxyz"
string = [i for i in string]
string2 = "0123456789"
string2 = [i for i in string2]
weight = [5 for i in range(len(string))]+[2 for i in range(len(string2))]
fileholder = open("classcodes.txt","w")
counter=0
tempArr=[] 
while counter<=100000:
    a = random.choices(string+string2,weights=weight,k=7)
    temp = ""
    for i in a:
        temp+=str(i)
    if temp not in tempArr:
        fileholder.write(temp+"\n")
        print(*a," ",temp,end="\n",sep="")
        counter+=1
    tempArr.append(temp)
