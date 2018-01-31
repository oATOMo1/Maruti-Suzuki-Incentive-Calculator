import pandas
import datetime
Incentives = {1: 400, 2: 500, 3: 700, 4: 900, 5: 1100, 6: 1300, 7: 1500, 8: 1800, 9: 2100, 10: 2400}


def Calculate_Car_Incentive(cars):
    df = pandas.read_csv("E:\\000\\Cars.csv")

    Incentives = {1: df.loc[0, 'first'], 2: df.loc[0, 'second'], 3: df.loc[0, 'third'], 4: df.loc[0, 'fourth'],
                  5: df.loc[0, 'fifth'], 6: df.loc[0, 'sixth'], 7: df.loc[0, 'seventh'], 8: df.loc[0, 'eighth'],
                  9: df.loc[0, 'ninth'], 10: df.loc[0, 'tenth']}

    Car_Amount = 0
    if cars > 10:
        Car_Amount = (cars - 10) * 2400
    for i in Incentives:
        if i > cars:
            break
        Car_Amount += Incentives[i]
    del df
    return Car_Amount


def Calculate_MGA_Incentive(mga):
    df1 = pandas.read_csv("E:\\000\\Ranges.csv")
    highest = df1.loc[0, 'Highest']
    second = df1.loc[0, 'Second']
    third = df1.loc[0, 'Third']
    fourth = df1.loc[0, 'Fourth']
    fifth = df1.loc[0, 'Fifth']
    sixth = df1.loc[0, 'Sixth']
    seventh = df1.loc[0, 'Seventh']
    eighth = df1.loc[0, 'Eighth']
    ninth = df1.loc[0, 'Nineth']
    tenth = df1.loc[0, 'Tenth']
    lowest = df1.loc[0, 'Lowest']

    Mga_Amount = 0
    if mga >= highest:
        Mga_Amount = (8/100) * mga
    elif third <= mga <= second:
        Mga_Amount = (7/100) * mga
    elif fifth <= mga <= fourth:
        Mga_Amount = (6/100) * mga
    elif seventh <= mga <= sixth:
        Mga_Amount = (5/100) * mga
    elif ninth <= mga <= eighth:
        Mga_Amount = (4/100) * mga
    elif lowest <= mga <= tenth:
        Mga_Amount = (3/100) * mga
    elif mga < 30000:
        return 0

    return Mga_Amount


def Calculate_Warranty_Incentive(warranty):
    df1 = pandas.read_csv("E:\\000\\Data.csv")
    Warranty_Amount = warranty * df1.loc[0, 'Warranty']
    del df1
    return Warranty_Amount


def Brezza_set(new):
    df1 = pandas.read_csv("E:\\000\\Data.csv")
    df1['Brezza'] = new
    df1.to_csv('E:\\000\\Data.csv', sep=',', mode='w')
    del df1


def Dzire_set(new):
    df1 = pandas.read_csv("E:\\000\\Data.csv")
    df1['Dzire'] = new
    df1.to_csv('E:\\000\\Data.csv', sep=',', mode='w')
    del df1


def Dzire_get():
    df1 = pandas.read_csv("E:\\000\\Data.csv")
    dzire = df1.loc[0, 'Dzire']
    del df1
    return dzire


def Brezza_get():
    df1 = pandas.read_csv ( "E:\\000\\Data.csv" )
    brezza = df1.loc[0, 'Brezza']
    del df1
    return brezza


def Spot_set(new):
    df1 = pandas.read_csv("E:\\000\\Data.csv")
    df1['Spot'] = new
    df1.to_csv('E:\\000\\Data.csv', sep=',', mode='w')
    del df1


def Spot_get():
    df1 = pandas.read_csv("E:\\000\\Data.csv")
    dzire = df1.loc[0, 'Spot']
    del df1
    return dzire


def Warranty_get():
    df1 = pandas.read_csv("E:\\000\\Data.csv")
    warrant = df1.loc[0, 'Warranty']
    del df1
    return warrant


def login(user, passw):
    df1 = pandas.read_csv ( "E:\\000\\Data.csv" )
    pre_user = df1.loc[0, 'UserName']
    pre_passw = df1.loc[0, 'Password']

    if user == pre_user:
        if passw == pre_passw:
            return True
        else:
            return False
    else:
        return False


def Updating_Other(warranty, spot, brezza, dzire):
    df1 = pandas.read_csv("E:\\000\\Data.csv")
    df1['Warranty'] = warranty
    df1['Spot'] = spot
    df1['Brezza'] = brezza
    df1['Dzire'] = dzire
    df1.to_csv('E:\\000\\Data.csv', sep=',', mode='w')


def Updating_MGA(highest, second, third, fourth, fifth, sixth, seventh, eight, ninth, tenth, lowest):
    df1 = pandas.read_csv("E:\\000\\Ranges.csv")
    df1['Highest'] = highest
    df1['Second'] = second
    df1['Third'] = third
    df1['Fourth'] = fourth
    df1['Fifth'] = fifth
    df1['Sixth'] = sixth
    df1['Seventh'] = seventh
    df1['Eighth'] = eight
    df1['Nineth'] = ninth
    df1['Tenth'] = tenth
    df1['Lowest'] = lowest

    df1.to_csv('E:\\000\\Ranges.csv', sep=',', mode='w')
    del df1


def Updating_Cars(first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth):
    df1 = pandas.read_csv("E:\\000\\Cars.csv")
    df1['first'] = first
    df1['second'] = second
    df1['third'] = third
    df1['fourth'] = fourth
    df1['fifth'] = fifth
    df1['sixth'] = sixth
    df1['seventh'] = seventh
    df1['eighth'] = eighth
    df1['ninth'] = ninth
    df1['tenth'] = tenth

    df1.to_csv('E:\\000\\Cars.csv', sep=',', mode='w')
    del df1


def Writig_Users(name, cars, mga, warranty, ags, dzire,  brezza):
    df = pandas.read_csv ( "E:\\000\\Temp.txt" )
    t = df.loc[0, 'Times']
    t = t + 1
    df['Times'] = t
    df.to_csv ( "E:\\000\\Temp.txt" , sep=',' , mode='w' )
    tmep = df.loc[0, 'Times']
    time = datetime.datetime.now()

    data = [[name , cars , mga , warranty , ags , dzire , brezza , time.strftime ( "%H:%M:%S" ) ,
             time.strftime ( "%d\%m\%Y" )]]

    if tmep == 1:
        df1 = pandas.DataFrame(data,
                               columns=['Name', 'Cars', 'MGA', 'Warranty', 'AGS', 'Dzire', 'Brezza', 'Time', 'Date'])
        df1.to_csv("E:\\000\\User.csv", mode='a', header=True)
    else:
        df1 = pandas.DataFrame(data,
                               columns=['Name', 'Cars', 'MGA', 'Warranty', 'AGS', 'Dzire', 'Brezza', 'Time', 'Date'])
        df1.to_csv("E:\\000\\User.csv", mode='a', header=False)


def Give_List():
    global temp
    df1 = pandas.read_csv ( "E:\\000\\Ranges.csv" )
    listt = []

    temp = df1.loc[0, 'Highest']
    listt.append(temp)

    temp = df1.loc[0, 'Second']
    listt.append(temp)

    temp = df1.loc[0, 'Third']
    listt.append(temp)

    temp = df1.loc[0, 'Fourth']
    listt.append(temp)

    temp = df1.loc[0, 'Fifth']
    listt.append(temp)

    temp = df1.loc[0, 'Sixth']
    listt.append(temp)

    temp = df1.loc[0, 'Seventh']
    listt.append(temp)

    temp = df1.loc[0, 'Eighth']
    listt.append(temp)

    temp = df1.loc[0, 'Nineth']
    listt.append(temp)

    temp = df1.loc[0, 'Tenth']
    listt.append(temp)

    temp = df1.loc[0, 'Lowest']
    listt.append(temp)

    del df1
    return listt


def Give_Car_List():
    global temp
    df1 = pandas.read_csv ( "E:\\000\\Cars.csv" )
    listt = []

    temp = df1.loc[0 , 'first']
    listt.append ( temp )

    temp = df1.loc[0 , 'second']
    listt.append ( temp )

    temp = df1.loc[0 , 'third']
    listt.append ( temp )

    temp = df1.loc[0 , 'fourth']
    listt.append ( temp )

    temp = df1.loc[0 , 'fifth']
    listt.append ( temp )

    temp = df1.loc[0 , 'sixth']
    listt.append ( temp )

    temp = df1.loc[0 , 'seventh']
    listt.append ( temp )

    temp = df1.loc[0 , 'eighth']
    listt.append ( temp )

    temp = df1.loc[0 , 'ninth']
    listt.append ( temp )

    temp = df1.loc[0 , 'tenth']
    listt.append ( temp )

    del df1
    return listt


def Final_Data(data = []):

    df = pandas.read_csv ( "E:\\000\\Temp.txt" )
    t = df.loc[0 , 'Time']
    t = t + 1
    df['Time'] = t
    df.to_csv ( "E:\\000\\Temp.txt" , sep=',' , mode='w' )
    temp = df.loc[0 , 'Time']

    temp1 = data[0]
    temp2 = data[1]
    temp3 = data[2]
    temp4 = data[3]
    temp5 = data[4]
    temp6 = data[5]
    temp7 = data[6]
    temp8 = data[7]
    dat = [[data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]]]

    if temp == 1:
        df1 = pandas.DataFrame(dat,
                               columns=['Name', 'Cars', 'MGA', 'Warranty', 'AGS', 'Dzire', 'Brezza',
                                        'Total Incentive'])
        df1.to_csv("E:\\000\\Final Data.csv", mode='a', header=True)
    else:
        df1 = pandas.DataFrame(dat,
                               columns=['Name', 'Cars', 'MGA', 'Warranty', 'AGS', 'Dzire', 'Brezza',
                                        'Total Incentive'])
        df1.to_csv("E:\\000\\Final Data.csv", mode='a', header=False)


def Making_Highest_Performer():
    df1 = pandas.read_csv ( "E:\\000\\Final Data.csv" )
    listt = []
    listt1 = []
    listt2 = []

    for i in range(len(df1.index)):
        listt1.append(df1.loc[i, 'Total Incentive'])
        listt2.append(df1.loc[i, 'Name'])

    for i,j in zip(listt1, listt2):
        listt.append([i, j])

    return listt


def Highest_Performer():
    listt = Making_Highest_Performer()
    temp = []
    listt.sort(key=lambda x: x[0])
    temp.append(listt[-1])
    del listt[-1]
    for j in listt:
        i = j[0]
        if i == temp[0][0]:
            temp.append([j])
    return temp
