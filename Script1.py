###############################################   Importing    ########################################################
import tkinter as tk
import Backend
###############################################----Importing----#######################################################


###############################################  Setting Size  ########################################################
window = tk.Tk()

w = 600
h = 520

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))

################################################--Setting Size--######################################################


################################################ DESIGNING FUNC #######################################################

def Final_Data():
    global window_place
    window_place = 'Adding_Final_Data'

    global frame8
    frame8 = tk.Frame(window)

    global aaa
    global bbb
    global ccc
    global ddd
    global eee

    aaa = tk.StringVar()
    bbb = tk.StringVar()
    ccc = tk.StringVar()
    ddd = tk.StringVar()
    eee = tk.StringVar()

    tk.Label(frame7, text="Incentive Calculator", font=("Helvetica", 50), bg="cyan")\
        .grid(row=0, column=0, columnspan=4)

    tk.Button(frame7, text='Save', width=12, command=updateCars, border=7, bg='blue', fg='white')\
        .grid(row=12, column=2, columnspan=2)
    tk.Button(frame7, text='Close', width=12, command=window.destroy, border=7, bg='blue', fg='white')\


def Car_values():
    global window_place
    window_place = 'Changing_Car'

    global frame7
    frame7 = tk.Frame(window)

    global aa
    global bb
    global cc
    global dd
    global ee
    global ff
    global gg
    global hh
    global ii
    global jj

    aa = tk.StringVar()
    bb = tk.StringVar()
    cc = tk.StringVar()
    dd = tk.StringVar()
    ee = tk.StringVar()
    ff = tk.StringVar()
    gg = tk.StringVar()
    hh = tk.StringVar()
    ii = tk.StringVar()
    jj = tk.StringVar()

    tk.Button(frame7, text='Save', width=12, command=updateCars, border=7, bg='blue', fg='white')\
        .grid(row=12, column=2, columnspan=2)
    tk.Button(frame7, text='Close', width=12, command=window.destroy, border=7, bg='blue', fg='white')\
        .grid(row=12, column=1, columnspan=2)
    tk.Button(frame7, text='Other', width=12, command=Other_decision, border=7, bg='blue', fg='white')\
        .grid(row=1, column=1)
    tk.Button(frame7, text='MGA', width=12, command=Mga_values_decision, border=7, bg='blue', fg='white')\
        .grid(row=1, column=2)
    tk.Button(frame7, text='Cars', width=12, command=Car_values_decision, border=7, bg='blue', fg='white')\
        .grid(row=1, column=3)

    tk.Label(frame7, text="Incentive Calculator", font=("Helvetica", 50), bg="cyan")\
        .grid(row=0, column=0, columnspan=4)

    tk.Label(frame7, text='First')\
        .grid(row=2, column=1)
    tk.Label(frame7, text='Second')\
        .grid(row=3, column=1)
    tk.Label(frame7, text='Third')\
        .grid(row=4, column=1)
    tk.Label(frame7, text='Fourth')\
        .grid(row=5, column=1)
    tk.Label(frame7, text='Fifth')\
        .grid(row=6, column=1)
    tk.Label(frame7, text='Sixth')\
        .grid(row=7, column=1)
    tk.Label(frame7, text='Seventh')\
        .grid(row=8, column=1)
    tk.Label(frame7, text='Eighth')\
        .grid(row=9, column=1)
    tk.Label(frame7, text='Ninth')\
        .grid(row=10, column=1)
    tk.Label(frame7, text='Tenth')\
        .grid(row=11, column=1)

    e1111111 = tk.Entry(frame7, textvariable=aa, bd=7, justify='center')
    e2222222 = tk.Entry(frame7, textvariable=bb, bd=7, justify='center')
    e3333333 = tk.Entry(frame7, textvariable=cc, bd=7, justify='center')
    e4444444 = tk.Entry(frame7, textvariable=dd, bd=7, justify='center')
    e5555555 = tk.Entry(frame7, textvariable=ee, bd=7, justify='center')
    e6666666 = tk.Entry(frame7, textvariable=ff, bd=7, justify='center')
    e7777777 = tk.Entry(frame7, textvariable=gg, bd=7, justify='center')
    e8888888 = tk.Entry(frame7, textvariable=hh, bd=7, justify='center')
    e9999999 = tk.Entry(frame7, textvariable=ii, bd=7, justify='center')
    e0000000 = tk.Entry(frame7, textvariable=jj, bd=7, justify='center')

    e1111111.grid(row=2, column=2)
    e2222222.grid(row=3, column=2)
    e3333333.grid(row=4, column=2)
    e4444444.grid(row=5, column=2)
    e5555555.grid(row=6, column=2)
    e6666666.grid(row=7, column=2)
    e7777777.grid(row=8, column=2)
    e8888888.grid(row=9, column=2)
    e9999999.grid(row=10, column=2)
    e0000000.grid(row=11, column=2)

    frame7.pack()

    temp = Backend.Give_Car_List()

    e1111111.insert(tk.END, temp[0])
    e2222222.insert(tk.END, temp[1])
    e3333333.insert(tk.END, temp[2])
    e4444444.insert(tk.END, temp[3])
    e5555555.insert(tk.END, temp[4])
    e6666666.insert(tk.END, temp[5])
    e7777777.insert(tk.END, temp[6])
    e8888888.insert(tk.END, temp[7])
    e9999999.insert(tk.END, temp[8])
    e0000000.insert(tk.END, temp[9])


def Mga_values():
    global window_place
    window_place = 'Changing_MGA'

    global frame6
    global hig
    global sec
    global thi
    global fou
    global fif
    global six
    global sev
    global eig
    global nin
    global ten
    global low

    frame6 = tk.Frame(window)

    hig = tk.StringVar()
    sec = tk.StringVar()
    thi = tk.StringVar()
    fou = tk.StringVar()
    fif = tk.StringVar()
    six = tk.StringVar()
    sev = tk.StringVar()
    eig = tk.StringVar()
    nin = tk.StringVar()
    ten = tk.StringVar()
    low = tk.StringVar()

    tk.Label(frame6, text="Incentive Calculator" , font=("Helvetica", 50), bg="cyan")\
        .grid(row=0, column=0, columnspan=4)
    tk.Label(frame6, text="To")\
        .grid(row=4, column=2)
    tk.Label(frame6, text="To")\
        .grid(row=5, column=2)
    tk.Label(frame6, text="To")\
        .grid(row=6, column=2)
    tk.Label(frame6, text="To")\
        .grid(row=7, column=2)
    tk.Label(frame6, text="To")\
        .grid(row=8, column=2)

    e111111 = tk.Entry(frame6, textvariable=hig, bd=10, justify='center', font=("Helvetica", 10))
    e222222 = tk.Entry(frame6, textvariable=sec, bd=10, justify='center', font=("Helvetica", 10))
    e333333 = tk.Entry(frame6, textvariable=thi, bd=10, justify='center', font=("Helvetica", 10))
    e444444 = tk.Entry(frame6, textvariable=fou, bd=10, justify='center', font=("Helvetica", 10))
    e555555 = tk.Entry(frame6, textvariable=fif, bd=10, justify='center', font=("Helvetica", 10))
    e666666 = tk.Entry(frame6, textvariable=six, bd=10, justify='center', font=("Helvetica", 10))
    e777777 = tk.Entry(frame6, textvariable=sev, bd=10, justify='center', font=("Helvetica", 10))
    e888888 = tk.Entry(frame6, textvariable=eig, bd=10, justify='center', font=("Helvetica", 10))
    e999999 = tk.Entry(frame6, textvariable=nin, bd=10, justify='center', font=("Helvetica", 10))
    e1000000 = tk.Entry(frame6, textvariable=ten, bd=10, justify='center', font=("Helvetica", 10))
    e1011111 = tk.Entry(frame6, textvariable=low, bd=10, justify='center', font=("Helvetica", 10))

    tk.Button(frame6, text='Save', width=15, border=7, bg="blue", font=("Helvetica", 8), fg='white', command=updateMGA)\
        .grid(row=9, column=2, columnspan=2)
    tk.Button(frame6, text='Close', width=15, border=7, bg="blue", font=("Helvetica", 8), fg='white', command=window.destroy)\
        .grid(row=9, column=1, columnspan=2)
    tk.Button(frame6, text='Other', width=15, border=7, bg="blue", font=("Helvetica", 8), fg='white', command=Other_decision)\
        .grid(row=1, column=1)
    tk.Button(frame6, text='MGA', width=15, border=7, bg="blue", font=("Helvetica", 8), fg='white', command=Mga_values_decision)\
        .grid(row=1, column=2)
    tk.Button(frame6, text='Cars', width=15, border=7, bg="blue", font=("Helvetica", 8), fg='white', command=Car_values_decision)\
        .grid(row=1, column=3)

    e111111.grid ( row=3 , column=2 )
    e222222.grid ( row=4 , column=1 )
    e333333.grid ( row=4 , column=3 )
    e444444.grid ( row=5 , column=1 )
    e555555.grid ( row=5 , column=3 )
    e666666.grid ( row=6 , column=1 )
    e777777.grid ( row=6 , column=3 )
    e888888.grid ( row=7 , column=1 )
    e999999.grid ( row=7 , column=3 )
    e1000000.grid ( row=8 , column=1 )
    e1011111.grid ( row=8 , column=3 )

    temp0 = Backend.Give_List()

    e111111.insert(tk.END, temp0[0])
    e333333.insert(tk.END, temp0[1])
    e222222.insert(tk.END, temp0[2])
    e555555.insert(tk.END, temp0[3])
    e444444.insert(tk.END, temp0[4])
    e777777.insert(tk.END, temp0[5])
    e666666.insert(tk.END, temp0[6])
    e999999.insert(tk.END, temp0[7])
    e888888.insert(tk.END, temp0[8])
    e1011111.insert(tk.END, temp0[9])
    e1000000.insert(tk.END, temp0[10])

    frame6.pack()


def Others_values():

    global frame4
    global Warranty_Condition
    global Dzire_Condition
    global Brezza_Condition
    global Spot_Condition
    global window_place

    window_place = "Admin_Setting"

    Warranty_Condition = tk.StringVar()
    Brezza_Condition = tk.StringVar()
    Dzire_Condition = tk.StringVar()
    Spot_Condition = tk.StringVar()

    frame4 = tk.Frame(window)
    frame4.pack()

    tk.Label ( frame4 , text="Incentive Calculator" , font=("Helvetica" , 50) , bg="cyan" )\
        .grid(row=1, column=0, columnspan=3)
    tk.Label(frame4, text='Admin', fg='Red', font=('Helvetica', 15))\
        .grid(row=3, column=1)
    tk.Label(frame4, text='Warranty', font=('Helvetica', 20))\
        .grid(row=4, column=0, columnspan=2)
    tk.Label(frame4, text='AGS Retails', font=('Helvetica', 20))\
        .grid(row=5, column=0, columnspan=2)
    tk.Label(frame4, text='Dzire Booking', font=('Helvetica', 20))\
        .grid(row=6, column=0, columnspan=2)
    tk.Label(frame4, text='Brezza Booking', font=('Helvetica', 20))\
        .grid(row=7, column=0, columnspan=2)

    e1111 = tk.Entry(frame4, textvariable=Warranty_Condition, font=('Helvetica', 11), bd=10, justify='center')
    e2222 = tk.Entry(frame4, textvariable=Spot_Condition, font=('Helvetica', 11), bd=10, justify='center')
    e3333 = tk.Entry(frame4, textvariable=Dzire_Condition, font=('Helvetica', 11), bd=10, justify='center')
    e4444 = tk.Entry(frame4, textvariable=Brezza_Condition, font=('Helvetica', 11), bd=10, justify='center')

    tk.Button(frame4, text='Save', width=12, command=updateOther, border=7, bg='blue', fg='white')\
        .grid(row=8, column=1, columnspan=2)
    tk.Button(frame4, text='Close', width=12, command=window.destroy, border=7, bg='blue', fg='white')\
        .grid(row=8, column=0, columnspan=2)
    tk.Button(frame4, text='Other', width=12, command=Other_decision, border=7, bg='blue', fg='white')\
        .grid(row=2, column=0)
    tk.Button(frame4, text='MGA', width=12, command=Mga_values_decision, border=7, bg='blue', fg='white')\
        .grid(row=2, column=1)
    tk.Button(frame4, text='Cars', width=12, command=Car_values_decision, border=7, bg='blue', fg='white')\
        .grid(row=2, column=2)

    tem1 = Backend.Warranty_get()
    tem2 = Backend.Spot_get()
    tem3 = Backend.Brezza_get()
    tem4 = Backend.Dzire_get()

    e1111.insert(tk.END, tem1)
    e2222.insert(tk.END, tem2)
    e3333.insert(tk.END, tem3)
    e4444.insert(tk.END, tem4)

    e1111.grid(row=4, column=1, columnspan=2)
    e2222.grid(row=5, column=1, columnspan=2)
    e3333.grid(row=6, column=1, columnspan=2)
    e4444.grid(row=7, column=1, columnspan=2)


def About():
    global window_place
    global frame5
    window_place = "About"
    window.title('About')

    frame5 = tk.Frame(window)
    frame5.pack()

    tk.Label(frame5, text='Incentive Calculator For Maruti Suzuki Karnal Motors', font=('Helvetica', 12))\
        .grid(row=1, column=0, columnspan=2)
    tk.Label(frame5, text='Created By: Aryan Bakshi', font=('Helvetica', 12))\
        .grid(row=2, column=0, columnspan=2)
    tk.Label(frame5, text=' © 2017 Invenico Inc. All rights reserved.', font=('Helvetica', 12))\
        .grid(row=3, column=0, columnspan=2)
    tk.Label(frame5, text="", font=('Helvetica', 120))\
        .grid(row=0, column=0)


def Admin_Permission():
    global window_place
    global frame3
    global a
    global b

    frame3 = tk.Frame(window)

    window_place = "Admin"

    window.title("Admin")

    a = tk.StringVar()
    b = tk.StringVar()

    tk.Label(frame3, text=' ', font=('Helvetica', 100))\
        .grid(row=0, column=5)
    tk.Label(frame3, text='    Username   ', font=('Helvetica', 15))\
        .grid(row=5, column=5)
    tk.Label(frame3, text='    Password   ', font=('Helvetica', 15))\
        .grid(row=6, column=5)
    tk.Entry(frame3, textvariable=a, bd=10, justify='center')\
        .grid(row=5, column=6)
    tk.Entry(frame3, show='*', textvariable=b, bd=10, justify='center')\
        .grid(row=6, column=6)
    tk.Button(frame3, text="Login", width=15, command=logging_in, font=('Helvetica', 11), fg='red', bd=5)\
        .grid(row=7, column=6)
    tk.Button(frame3, text="Close", width=15, command=window.destroy, border=7, font=('Helvetica', 11), fg='red', bd=5)\
        .grid(row=7, column=5)

    frame3.pack()


def Incentive_Window(Name, Cars_Incentive, MGA_Incentive, Warranty_Incentive, Spot_Incentive, Brezza_Incentive,
                     Dzire_Incentive, Total_Incentive):
    global window_place

    window_place = "Incentive"

    global frame2
    frame2 = tk.Frame(window)
    frame2.pack()

    window.title(Name + "'s Incentive")

    tk.Label ( frame2 , text="Incentive Calculator", font=("Helvetica", 50), bg="cyan")\
        .grid(row=0, column=0, columnspan=2)
    tk.Label(frame2, text="Car Incentive", font=("Helvetica", 20), fg="red")\
        .grid(row=1, column=0)
    tk.Label(frame2, text="   MGA Incentive  ", font=("Helvetica", 20), fg="red")\
        .grid(row=1, column=1)
    tk.Label(frame2, text="   Warranty Incentive   ", font=("Helvetica", 20), fg="red")\
        .grid(row=3, column=0)
    tk.Label(frame2, text="  Total Incentive   ", font=("Helvetica", 20), fg="red")\
        .grid(row=7, column=0, columnspan=2)

    tk.Label(frame2, text="  AGS Incentive   ", font=("Helvetica", 20), fg="red")\
        .grid(row=3, column=1)
    tk.Label(frame2, text="  Brezza Incentive   ", font=("Helvetica", 20), fg="red")\
        .grid(row=5, column=0)
    tk.Label(frame2, text="  Dzire Incentive   ", font=("Helvetica", 20), fg="red")\
        .grid(row=5, column=1)
    tk.Label(frame2, text=Cars_Incentive.__str__(), font=("Helvetica", 15))\
        .grid(row=2, column=0)
    tk.Label(frame2, text=MGA_Incentive.__str__(), font=("Helvetica", 15))\
        .grid(row=2, column=1)
    tk.Label(frame2, text=Warranty_Incentive.__str__(), font=("Helvetica", 15))\
        .grid(row=4, column=0)
    tk.Label(frame2, text=Total_Incentive.__str__ (), font=("Helvetica", 15))\
        .grid(row=8, column=0, columnspan=2 )
    tk.Label(frame2, text=Spot_Incentive.__str__(), font=("Helvetica", 15))\
        .grid(row=4, column=1)
    tk.Label(frame2, text=Brezza_Incentive.__str__(), font=("Helvetica", 15))\
        .grid(row=6, column=0)
    tk.Label(frame2, text=Dzire_Incentive.__str__(), font=("Helvetica", 15))\
        .grid(row=6, column=1)
    tk.Label(frame2, text=" ", font=("Helvetica", 24))\
        .grid(row=9, column=0)

    if MGA_Incentive == 0:
        tk.Label ( frame2 , text="(20% Deducted)", font=("Helvetica", 11)).grid ( row=8 , column=1, columnspan=2)
    else:
        pass

    tk.Button(frame2, text="Ok", width=12, fg="Red", command=ButtonOk, border=10, font=("Helvetica", 15))\
        .grid(row=10, column=0, columnspan=2)


def Designing():
    global window_place

    window_place = "User"

    global frame
    global window
    window.title("Calculator")
    frame = tk.Frame(window)
    frame.pack()

    menu = tk.Menu(window)
    window.config(menu=menu)

    modeMenu = tk.Menu(menu, tearoff=0)

    menu.add_cascade(label='Mode', menu=modeMenu)

    modeMenu.add_command(label="Admin", command=Admin_Decision)
    modeMenu.add_command(label="User", command=User)
    modeMenu.add_command(label="Final Data", command=logging_in)
    modeMenu.add_separator()

    modeMenu.add_command(label="Exit", command=window.destroy)

    helpMenu = tk.Menu(menu, tearoff=0)

    menu.add_cascade(label="Help", menu=helpMenu)
    helpMenu.add_command(label="About", command=About_Decision)

    tk.Label(frame, text="Name", font=("Helvetica", 20))\
        .grid(row=1, column=0)
    tk.Label(frame, text="Incentive Calculator", font=("Helvetica", 50), bg="cyan")\
        .grid(row=0, column=0, columnspan=2)
    tk.Label(frame, text="No. Of Cars", font=("Helvetica", 20))\
        .grid(row=2, column=0)
    tk.Label(frame, text="MGA Sold", font=("Helvetica", 20))\
        .grid(row=3, column=0)
    tk.Label(frame, text="Warranty Sold", font=("Helvetica", 20))\
        .grid(row=4, column=0)
    tk.Label(frame, text="-------------------------------------------------------------", fg='Blue', font=("Helvetica", 20))\
        .grid(row=5, column=0, columnspan=2)

    tk.Label(frame, text="AGS Cars", font=("Helvetica", 20))\
        .grid(row=6, column=0)
    tk.Label(frame, text="Dzire Booking", font=("Helvetica", 20))\
        .grid(row=7, column=0)
    tk.Label(frame, text="Brezza Booking", font=("Helvetica", 20))\
        .grid(row=8, column=0)

    ##############################################################################

    global Name
    Name = tk.StringVar()

    global No_Of_Cars_Sold
    No_Of_Cars_Sold = tk.StringVar()

    global No_Of_MGA_Sold
    No_Of_MGA_Sold = tk.StringVar()

    global No_Of_Warranty_Sold
    No_Of_Warranty_Sold = tk.StringVar()

    global Spot
    Spot = tk.StringVar()

    global Dzire
    Dzire = tk.StringVar()

    global Brezza
    Brezza = tk.StringVar()

    global e1, e2, e3, e4, e5, e6
    tk.Entry(frame, textvariable=Name, border=10, font=("Helvetica", 15), justify='center')\
        .grid(row=1, column=1)
    e1 = tk.Entry(frame, textvariable=No_Of_Cars_Sold, border=10, font=("Helvetica", 15), justify='center')
    e2 = tk.Entry(frame, textvariable=No_Of_MGA_Sold, border=10, font=("Helvetica", 15), justify='center')
    e3 = tk.Entry(frame, textvariable=No_Of_Warranty_Sold, border=10, font=("Helvetica", 15), justify='center')
    e4 = tk.Entry(frame, textvariable=Spot, border=10, font=("Helvetica", 15), justify='center')
    e5 = tk.Entry(frame, textvariable=Dzire, border=10, font=("Helvetica", 15), justify='center')
    e6 = tk.Entry(frame, textvariable=Brezza, border=10, font=("Helvetica", 15), justify='center')

    e1.grid(row=2, column=1)
    e2.grid(row=3, column=1)
    e3.grid(row=4, column=1)
    e4.grid(row=6, column=1)
    e5.grid(row=7, column=1)
    e6.grid(row=8, column=1)

    ###############################################################################

    global b1, b2
    b1 = tk.Button(frame, text="Calculate", width=15, command=Calculate_Incentive, bg='cyan', border=7, font=("Helvetica", 20))\
        .grid(row=9, column=1)
    b2 = tk.Button(frame, text="Close", width=15, command=window.destroy, border=7, bg='cyan', font=("Helvetica", 20))\
        .grid(row=9, column=0)

    ###############################################################################


##########################################--DESIGNING FUNC--###########################################################



##########################################    LOGIC AREA    ###########################################################

def Calculate_Incentive():

    if len(Name.get()) == 0:
        window2 = tk.Tk()
        window2.title("Error!")
        w = 310
        h = 65

        ws = window.winfo_screenwidth ()
        hs = window.winfo_screenheight ()

        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        window2.geometry('%dx%d+%d+%d' % (w, h, x, y))

        tk.Label(window2, text="Please Enter Your Name.", font=('Helvetica', 20), fg='red')\
            .grid(row=0, column=0, columnspan=3)
        tk.Button(window2, text="OK", command=window2.destroy, width=12, fg='red')\
            .grid(row=1, column=1)
        return
    else:
        User_name = Name.get()

    if len(No_Of_Cars_Sold.get()) == 0:
        e1.insert(tk.END, "0")
    if len(No_Of_MGA_Sold.get()) == 0:
        e2.insert(tk.END, "0")
    if len(No_Of_Warranty_Sold.get()) == 0:
        e3.insert(tk.END, "0")
    if len(Spot.get()) == 0:
        e4.insert(tk.END, "0")
    if len(Dzire.get()) == 0:
        e5.insert(tk.END, "0")
    if len(Brezza.get()) == 0:
        e6.insert(tk.END, "0")

    Backend.Writig_Users(User_name, No_Of_Cars_Sold.get(), No_Of_MGA_Sold.get(), No_Of_Warranty_Sold.get(),
                         Spot.get(), Dzire.get(), Brezza.get())
    frame.destroy()

    C = Backend.Calculate_Car_Incentive(int(No_Of_Cars_Sold.get()))
    M = Backend.Calculate_MGA_Incentive(int(No_Of_MGA_Sold.get()))
    W = Backend.Calculate_Warranty_Incentive(int(No_Of_Warranty_Sold.get()))
    S = int(Spot.get()) * Backend.Spot_get()
    D = int(Dzire.get()) * Backend.Dzire_get()
    B = int(Brezza.get()) * Backend.Brezza_get()

    Incentive = C + M + W + S + D + B

    if M == 0:
        Incentive = Incentive - (Incentive * (20 / 100))
    else:
        pass

    Incentive_Window(User_name, C, M, W, S, D, B, Incentive)


def User():
    global window_place
    if window_place == "User":
        pass
    elif window_place == "Admin":
        window_place = 'User'
        window.title('Calculator')
        frame3.destroy()
        Designing()
    elif window_place == "About":
        window_place = 'User'
        window.title ( 'Calculator' )
        frame5.destroy()
        Designing()
    elif window_place == "Incentive":
        window_place = 'User'
        window.title('Calculator')
        frame2.destroy()
        Designing()
    elif window_place == "Admin_Setting":
        window_place = 'User'
        window.title('Calculator')
        frame4.destroy()
        Designing()
    elif window_place == 'Changing_MGA':
        window_place = 'User'
        window.title ( 'Calculator' )
        frame6.destroy ()
        Designing ()
    elif window_place == 'Changing_Car':
        window_place = 'User'
        window.title ( 'Calculator' )
        frame7.destroy ()
        Designing ()


def logging_in():
    boolean = Backend.login(a.get(), b.get())
    boolean2 = Backend.login(a.get(), b.get())
    if boolean:
        Other_decision()
    else:
        pass


def ButtonOk():
    frame2.destroy()
    Designing()


def updateMGA():
    window4 = tk.Tk ()
    window4.title ( "Successful!" )
    w = 310
    h = 69

    ws = window.winfo_screenwidth ()
    hs = window.winfo_screenheight ()

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    window4.geometry('%dx%d+%d+%d' % (w, h, x, y))

    tk.Label(window4, text="Data Saved Successfully.", font=('Helvetica', 20))\
        .grid(row=0, column=0, columnspan=3)
    tk.Button(window4, text="OK", command=window4.destroy, width=12, fg='red', bd=5)\
        .grid(row=1, column=1)

    Backend.Updating_MGA(hig.get(), thi.get(), sec.get(), fif.get(), fou.get(), sev.get(), six.get(), nin.get(),
                         eig.get(), low.get(), ten.get())


def updateOther():
    global window_place

    window5 = tk.Tk()
    window5.title("Successful!")
    w = 310
    h = 69

    ws = window.winfo_screenwidth ()
    hs = window.winfo_screenheight ()

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    window5.geometry('%dx%d+%d+%d' % (w, h, x, y))

    tk.Label(window5, text="Data Saved Successfully.", font=('Helvetica', 20))\
        .grid(row=0, column=0, columnspan=3)
    tk.Button(window5, text="OK", command=window5.destroy, width=12, fg='red', bd=5)\
        .grid(row=1, column=1)

    Backend.Updating_Other(Warranty_Condition.get(), Spot_Condition.get(), Brezza_Condition.get(), Dzire_Condition.get())


def updateCars():
    global window_place
    window3 = tk.Tk ()
    window3.title ( "Successful!" )
    w = 310
    h = 69

    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    window3.geometry ( '%dx%d+%d+%d' % (w , h , x , y) )

    tk.Label(window3, text="Data Saved Successfully.", font=('Helvetica', 20))\
        .grid(row=0, column=0, columnspan=3)
    tk.Button(window3, text="OK", command=window3.destroy, width=12, fg='red', bd=5)\
        .grid(row=1, column=1)

    Backend.Updating_Cars(aa.get(), bb.get(), cc.get(), dd.get(), ee.get(), ff.get(), gg.get(), hh.get()
                          , ii.get(), jj.get())


def Mga_values_decision():
    global window_place

    if window_place == 'Admin_Setting':
        frame4.destroy ()
        Mga_values ()
    elif window_place == 'Changing_MGA':
        pass
    elif window_place == 'Changing_Car':
        frame7.destroy ()
        Mga_values ()


def Car_values_decision():
    global window_place

    if window_place == 'Admin_Setting':
        frame4.destroy ()
        Car_values ()
    elif window_place == 'Changing_MGA':
        frame6.destroy()
        Car_values()
    elif window_place == 'Changing_Car':
        pass


def Other_decision():
    global window_place

    if window_place == 'Admin':
        frame3.destroy()
        Others_values()
    elif window_place == 'Changing_MGA':
        frame6.destroy()
        Others_values()
    elif window_place == 'Admin_Setting':
        pass
    elif window_place == 'Changing_Car':
        frame7.destroy()
        Others_values()


def Admin_Decision():
    global window_place

    if window_place == "Admin":
        pass
    elif window_place == "User":
        frame.destroy()
        Admin_Permission()
    elif window_place == "Incentive":
        frame2.destroy()
        Admin_Permission()
    elif window_place == "About":
        frame5.destroy()
        Admin_Permission()
    elif window_place == "Admin_Setting":
        frame4.destroy()
        Admin_Permission()
    elif window_place == "Changing_MGA":
        frame6.destroy()
        Admin_Permission()
    elif window_place == "Changing_Car":
        frame7.destroy()
        Admin_Permission()


def About_Decision():
    global window_place
    if window_place == "About":
        pass
    elif window_place == "Incentive":
        frame2.destroy()
        About()
    elif window_place == "User":
        frame.destroy()
        About()
    elif window_place == "Admin":
        frame3.destroy()
        About()
    elif window_place == "Admin_Setting":
        frame4.destroy()
        About()
    elif window_place == 'Changing_MGA':
        frame6.destroy()
        About()
    elif window_place == 'Changing_Car':
        frame7.destroy()
        About()


##########################################----LOGIC AREA----###########################################################


window.iconbitmap('E:\\000\\favicon.ico')

Designing()

window.mainloop()
