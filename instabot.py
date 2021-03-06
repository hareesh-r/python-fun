#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time

import os

try:
    import tkinter

    from tkinter import *

    import tkinter.font as font

except:

    os.system("python -m pip install tkinter")

    import tkinter

    from tkinter import *

    import tkinter.font as font

try:

    from selenium import webdriver

except:

    os.system('python -m pip install selenium')

    from selenium import webdriver

try:

    from webdriver_manager.chrome import ChromeDriverManager

except:

    os.system('python -m pip install webdriver_manager')

    from webdriver_manager.chrome import ChromeDriverManager


def GUI_getinput(test_string):

    arr = []

    def func():

        string = str(reg.get())

        arr.append(string)

        screen.destroy()

    global screen

    screen = Tk()

    screen.title("Type and click Enter button")

    screen.geometry("665x470")

    screen.config(bg="dim grey")

    myFont = font.Font(weight="bold")

    Label(text=test_string, fg="white", font=myFont,
          bg="dodger blue", width="150", height="3").pack()

    reg = Entry(screen, text="Regulation Year", width="50", justify=CENTER)

    reg.focus_set()

    reg.pack(pady="10", padx="10", ipady=5)

    btn = Button(text="Enter", width="15",
                 fg="grey17", bg="white", command=func)

    btn.pack(ipady=5)

    screen.mainloop()

    return arr[0]


username1 = GUI_getinput("Enter your username")

password1 = GUI_getinput("Enter your password")

reciever1 = GUI_getinput("Enter reciever's username")

decider = GUI_getinput(
    "Enter 1 for Happy birthday in different languages\nEnter 2 for Custom messages")

if(decider == "2"):

    noOfTime1 = GUI_getinput("Enter how many no of time to send message")

    messageToSend = GUI_getinput("Enter what message you want to send")


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.instagram.com')

driver.implicitly_wait(300)

messageList = ['Tamil:- Iniya Pirandha naal nal vaazhuthukal',
               'Albanian: ???G??zuar dit??lindjen???',
               'Bosnian: ???Sretan ro??endan???',
               'Bulgarian: ???Chestit Rozhden den???',
               'Catalan: ???Per molts anys???',
               'Cheinese: ???Sh??ngr?? ku??il?????',
               'Czech: ???V??echno nejlep???? k narozenin??m???',
               'Danish: ???Tillykke med f??dselsdagen???',
               'Dutch: Fijne verjaardag???',
               'Filipino: ???Maligayang kaarawan???',
               'Finnish: ???Hyv???? syntym??p??iv???????',
               'French: ???Bon anniversaire???',
               'Galician: ???Feliz Aniversario???',
               'German: ???Alles Gute zum Geburtstag???',
               'Greek: ???Charo??mena gen??thlia???',
               'Hebrew: ????????? ?????????? ?????????',
               'Hungarian: ???Boldog sz??let??snapot???',
               'Icelandic: ???Til hamingju me?? afm??li?????',
               'Igbo: ???Ezi ncheta ???m???m??????',
               'Indonesian: ???Selamat ulang tahun???',
               'Irish: ???L?? breithe shona duit???',
               'Italian: ???Buon compleanno???',
               'Japanese: ????????????????????????????????????????????????',
               'Kazakh: ???Tw??an k??ni?? qutt?? bols??n???',
               'Khmer: ???Rikreay??? thngai??? kamnaet???',
               'Korean: ???Saeng-il chugha???',
               'Kurdish: ???Rojb??na te p??roz be???',
               'Latin: ???Felix natalis???',
               'Lithuanian: ???Su gimtadieniu???',
               'Luxembourgish: ???Alles Guddes fir d??i Gebuertsdag???',
               'Malay: ???Selamat Hari lahir???',
               'Mongolian: ??????????????? ???????????? ???????????',
               'Nepali: ???Janmadinak?????',
               'Norwegian: ???Gratulerer med dagen???',
               'Polish: ???Wszystkiego najlepszego???',
               'Portuguese: ???Feliz Anivers??rio???',
               'Romanian: ???La multi ani???',
               'Russian: ???S dnem ??????rozhdeniya???',
               'Serbian: ???Srec??an ro??endan???', 'Slovenian: ???Vse najbolj??e???',
               'Somali: ???Dhalasho Wacan???',
               'Spanish: ???Feliz cumplea??os???',
               'Swahili: ???Siku ya kuzaliwa ya furaha???',
               'Swedish: ???Grattis p?? f??delsedagen???',
               'Tai: ???S??uk??hs?????nt?? w???n keid???',
               'Turkish: ???Do??um g??n??n kutlu olsun???',
               'Ukranian: ???Z Dnem narodzhennya???',
               'Vietnamese: ???Ch??c m???ng sinh nh???t???',
               'Welsh: Penblwydd hapus???',
               'Zulu: ???Usuku olumnandi lokuzalwa',
               'Spanish ??? ??Feliz cumplea??os!',
               'French ??? Bon anniversaire !',
               'German ??? Alles Gute zum Geburtstag!',
               'Italian ??? Buon compleanno!',
               'Portuguese ??? Feliz anivers??rio!',
               'Swedish ??? Grattis p?? f??delsedagen!',
               'Russian ??? ?? ???????? ????????????????!',
               'Indonesian ??? Selamat ulang tahun!',
               'Dutch ??? Gefeliciteerd met je verjaardag!',
               'Norwegian ??? Gratulerer med dagen!',
               'Polish ??? Wszystkiego najlepszego!',
               'Turkish ??? Do??um g??n??n kutlu olsun!',
               'Danish ??? Tillykke med f??dselsdagen!',
               'Afrikaans:- Gelukkige verjaarsdag!',
               'Albanian:- G??zuar dit??lindjen!',
               'Amharic:- melikami lideti!',
               'Arabic:- eid milad saeid!',
               'Armenian:- Tsnundd shnorhavor!',
               'Azerbaijani:- Ad g??n??n m??bar??k!',
               'Bangla:- ??ubha janmadina!',
               'Basque:- Zorionak!',
               'Belarusian:- Z Dniom Narad??ennia!',
               'Bosnian:- Sretan ro??endan!',
               'Bulgarian:- Chestit Rozhden den!',
               'Burmese:- pyawrwin hpwalrar mwaynae!',
               'Catalan:- Feli?? aniversari!',
               'Cebuano:- Malipayong adlawng natawhan!',
               'Chinese:- Sh??ngr?? ku??il??!',
               'Corsican:- Felice Anniversariu!',
               'Croatian:- Sretan ro??endan!',
               'Czech:- V??echno nejlep???? k narozenin??m!',
               'Danish:- Tillykke med f??dselsdagen!',
               'Dutch:- Gelukkige verjaardag!',
               'Esperanto:- Feli??an naski??tagon!',
               'Estonian:- Palju ??nne s??nnip??evaks!',
               'Filipino:- Maligayang kaarawan!',
               'Finnish:- Hyv???? syntym??p??iv????!',
               'French:- Joyeux anniversaire!',
               'Galician:- Feliz Aniversario!',
               'Georgian:- ???ilotsav dabadebis dghes!',
               'German:- Alles Gute zum Geburtstag!',
               'Greek:- Charo??mena gen??thlia!',
               'Gujarati:- Janmadivasa ni subhakamana!',
               'Haitian Creole:- B??n f??t!',
               'Hausa:- Barka da ranar haihuwa!',
               'Hawaiian:- Hau oli La Hanau!',
               'Hindi:- janmadin mubaarak!',
               'Hmong:- Zoo siab hnub yug!',
               'Hungarian:- Boldog sz??let??snapot!',
               'Icelandic:- Til hamingju me?? afm??li??!',
               'Igbo:- Ezi ncheta ???m???m???!',
               'Indonesian:- Selamat ulang tahun!',
               'Irish:- L?? breithe shona duit!',
               'Italian:- Buon compleanno!',
               'Japanese:- Otanj??biomedet??gozaimasu!',
               'Javanese:- Sugeng tanggap warsa!',
               'Kannada:- Janmadinada subhasayagalu!',
               'Kazakh:- Tw??an k??ni?? qutt?? bols??n!',
               'Khmer:- rikreay\u200b thngai\u200b kamnaet!',
               'Kinyarwanda:- Isabukuru nziza!',
               'Korean:- saeng-il chugha haeyo!',
               'Kurdish:- Rojb??na te p??roz be!',
               'Kyrgyz:- Tuulgan kunu??uz menen kuttuktaym!',
               'Lao:- suk san van koed!',
               'Latvian:- Daudz laimes dzimsanas diena!',
               'Lithuanian:- Su gimtadieniu!',
               'Luxembourgish:- Alles Guddes fir de Gebuertsdag!',
               'Macedonian:- Srek??en rodenden!',
               'Malagasy:- Tratry ny tsingerintaona nahaterahana!',
               'Malay:- Selamat Hari lahir!',
               'Malayalam:- janmadinasansakal!',
               'Maori:- Kia ra whanau!',
               'Marathi:- Vadhadivasacya hardika subheccha!',
               'Mongolian:- T??rs??n ??driin mend!',
               'Nepali:- Janmadinako subhakamana!',
               'Norwegian:- Gratulerer med dagen!',
               'Nyanja:- Tsiku labwino lobadwa!',
               'Persian:- ?????????? ??????????!',
               'Polish:- Wszystkiego najlepszego z okazji urodzin!',
               'Portugese:- Feliz Aniversario!',
               'Punjabi:- Janamadina mubaraka!',
               'Romanian:- La multi ani!',
               'Russian:- S dnem \u200b\u200brozhdeniya!',
               'Samoan:- Manuia le aso fanau!',
               'Scottish Gaelic:- Co-l??-breith math!',
               'Serbian:- Srec??an ro??endan!',
               'Shona:- Bhavhadhe rinofadza!',
               'Sinhala:- suba upandinayak vevz!',
               'Slovak:- ????astn?? narodeniny!',
               'Slovenian:- Vse najbolj??e!',
               'Somali:- Dhalasho Wacan!',
               'Southern Sotho:- Letsatsi le monate la tsoalo!',
               'Spanish:- ??Feliz cumplea??os!',
               'Sundanese:- Wilujeung tepang taun!',
               'Swahili:- Heri ya siku ya kuzaliwa!',
               'Swedish:- Grattis p?? f??delsedagen!',
               'Tagalog:- Maligayang kaarawan!',
               'Tajik:- Zodr??z mu??orak!',
               'Tatar:- ?????????? ?????? ??????????!',
               'Telugu:- Puttinaroju subhzkznk???alu!',
               'Thai:- S??uk??hs?????nt?? w???n keid!',
               'Turkish:- ??yi ki do??dun!',
               'Turkmen:- Doglan g??n???? bilen!',
               'Ukranian:- Z Dnem Narodzhennya!',
               "Uzbek:- Tug'ilgan kuning bilan!",
               'Vietnamese:- Ch??c m???ng sinh nh???t!',
               'Welsh:- Penblwydd hapus!',
               'Western Frisian:- Lokkige jierdei!',
               'Xhosa:- Usuku lokuzalwa olumnandi!',
               'Yiddish:- mzl deyn geburstog!',
               'Yoruba:- O ku ojo ibi!',
               'Zulu:- Usuku olumnandi lokuzalwa']


def passWordFunction():

    return password1  # replace with your login password


def login():

    try:

        userID = driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input')

        userID.send_keys(username1)  # replace with your login user id

        passWord = driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')

        myPassWord = passWordFunction()

        passWord.send_keys(myPassWord)

        nextBtn = driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div[1]/div[3]/button')

        nextBtn.click()

        saveInfoBtn = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/section/div/button')

        saveInfoBtn.click()

        notNowBtn = driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]')

        notNowBtn.click()

        print('Login Successful')

    except:

        print("error occured while login")

        driver.close()


def search(name):

    searchBox = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')

    searchBox.send_keys(name)

    clickSearchResult = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')

    clickSearchResult.click()

    print('Search Successful')


def openChat():

    messageBtn = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button')

    messageBtn.click()

    print('Chat opened Successfully')


def sendMessage(messageList):

    print("inside messageList")

    messageBox = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

    counter = 1

    for i in messageList:

        messageBox.send_keys(i)

        sendButton = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')

        sendButton.click()

        time.sleep(0.5)

        print(counter, i, 'sent successfully', sep=" ")

        counter += 1

    print('closing tab')


login()

search(reciever1)  # replace with reciever user id

openChat()

if(decider == "1"):

    sendMessage(messageList)

if(decider == "2"):

    temp = []

    for i in range(int(noOfTime1)):

        temp.append(messageToSend)

    sendMessage(temp)

driver.close()