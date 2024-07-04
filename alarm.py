#importing the necessary librares for alarm clock
from tkinter import * 
import datetime 
import time
import winsound 


# Defining the alarm Function
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is : ", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake Up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break


# Defining the function to get user input
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)



clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x200")
# time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",fg="blue",font=("times new roman",15)).place(x = 110,y=10)
setYourAlarm = Label(clock,text = "Set Your Alarm",fg="tomato",relief = "solid",font=("times new roman",8,"bold")).place(x=10, y=50)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 20).place(x=110,y=50)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=50)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=50)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="green",bg="light gray",width = 10,command = actual_time).place(x =150,y=100)

clock.mainloop()
#Execution of the window.