a = []

with open("RestaurantList.rtf") as infile:
    for line in infile:
        a.append(line.split(","))



RestaurantNames=[]
DaysAndTimesRaw=[]

for i in a:
    i[0] = i[0].replace('"', '') #clearName
    RestaurantNames.append(i[0])

#print(RestaurantNames)

b=[]
with open("RestaurantList.rtf") as infile:
    for line in infile:
        b.append(line.split('"'))


for i in b:
    DaysAndTimesRaw.append(i[-2:-1])

test = ""
original = a[0]
test = DaysAndTimesRaw[0][0]
test2 = RestaurantNames[0]
test = test.replace(",", "")

def gapDetecter(sentence):

    weekDays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    newSentence = []
    timesRaw= []
    daysRaw = []
    for i in sentence.split(" "):
        if i.__contains__("-") and len(i) > 1:
            i = i.split("-")
            startDay = i[0]
            endDay = i[1]
            extendedDays = weekDays[weekDays.index(startDay):weekDays.index(endDay)+1]
            i = " ".join(extendedDays)

        newSentence.append(i)
    sentence = " ".join(newSentence)

    xx = (sentence.split("/"))
    for i in xx:
        for jj in i.split(" "):
            if jj in weekDays:
                daysRaw.append(jj)
        daysRaw.append("||")

    for i in sentence.split(" "):
        if i.__contains__(":") or i.isdigit() == True :
            timesRaw.append(i)

    print("originalLine: ",original)
    print("RestaurantName: ",test2)
    print("DaysWorking: ",daysRaw)
    print("TimesWorking: ", timesRaw)


gapDetecter(test)

for i in range(0,len(a),1):
    original = a[i]
    test = DaysAndTimesRaw[i][0]
    test2 = RestaurantNames[i]
    test = test.replace(",", "")

    gapDetecter(test)

