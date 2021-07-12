print("WELCOME TO CHAT BOT ")
name = str(input("TELL ME YOUR NAME "))

if(name == "shiva") or (name == "shiva dutt") or (name == "dutt"):
    print("vaanga shiva THATHHU")
    input("Epdi irukeenga ?")
    print("nee epdi irundha enakenna da venna . veliya po")
    input()
elif name in ["thrishal", "THRISHAL", "thirishal", "thirshal", "thirshal"]:
    print("unaku laam badhil solla mudiyadhu poda")
    input()
elif name in ["hareesh", "HAREESH"]:
    print("WELCOME BOSS")
    A = str(input("HOW ARE YOU BOSS "))
    if(A == "fine") or (A == "FINE"):
        print("glad to hear that")
        input()
    elif(A == "not fine") or ("not bad"):
        print("sorry to hear that")
        input()
else:
    print("Hello", name)
    cani = str(input("Can I ask you a question ?(yes or no)"))
    if cani in ["yes", "yup", "YES", "y"]:
        age = int(input("What's your age ? "))
        if(age >= 18):
            print("wow you can vote.")
            vt = int(input("HOW MANY TIMES HAVE YOU VOTED ? "))
            if(vt == 0):
                print("wait fot the next election ")
                input()
            else:
                print("How was your experience ?")
                brief = str(input("share your experience "))
        elif(age < 18):
            print("Hello child")
            nxtvt = int(input("How many years do you have to vote ?"))
            if(nxtvt < 2):
                print("just few years")
                input()
            else:
                print("wait for it")
                input()

    elif cani in ["no", "NO"]:
        print("bye", name, "see you soon")
        input()
