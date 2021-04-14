from tkinter import *
import pandas as pd
import pickle
from datetime import timedelta, datetime

root = Tk()
root.geometry("2000x1000")
root.title("Tasks to be Completed")
checklist = []
curTime = datetime.now()

# Load in all photos
photo0 = PhotoImage(file="img1.PNG")
photo1 = PhotoImage(file="img2.PNG")
photo2 = PhotoImage(file="img3.PNG")
photo3 = PhotoImage(file="img4.PNG")
photo4 = PhotoImage(file="img5.PNG")
photo5 = PhotoImage(file="img6.PNG")
photo6 = PhotoImage(file="img7.PNG")
photo7 = PhotoImage(file="img8.PNG")
photo8 = PhotoImage(file="img_final.PNG")

label = [Label(root, image = photo0), Label(root, image = photo1), Label(root, image = photo2), Label(root, image = photo3), Label(root, image = photo4), Label(root, image = photo5), Label(root, image = photo6), Label(root, image = photo7), Label(root, image = photo8)]

# Function to be called when task is completed: label[i].grid(column=10, row=10)
# Function to remove previous image: label[i].grid_remove


# it SHOULD delete everything that was checked...not yet working right
def removeAll(warning):
    global checklist

    numRemoved = 0
    for i in range(len(checklist)):
        if i - numRemoved > len(checklist) - 1:
            break
        if checklist[i - numRemoved].var.get() == 1:
            checklist[i - numRemoved].c.destroy()
            checklist.pop(i - numRemoved)
            for j in range(len(checklist)):
                checklist[j].c.grid(row=j + 1, column=0)
                checklist[j].dateLabel.grid(row=j + 1, column=1)
                checklist[j].alertLabel.grid(row=j + 1, column=2)
    warning.destroy()


# A warning pops up before deletion
def removeEntry():
    warning = Tk()
    l = Label(warning, text="Are you sure you want to remove the selected entry(s)?").grid(row=0, column=1)
    no = Button(warning, text="No", padx=100, command=warning.destroy).grid(row=1, column=2)
    yes = Button(warning, text="Yes", padx=100, command=lambda: removeAll(warning)).grid(row=1, column=0)


def editEntry():
    editWindow = Tk()
    editWindow.geometry("200x200")
    indices = []
    numChecked = 0
    for i in checklist:
        if i.var.get() == 1:
            l = Label(editWindow, text=i.c.cget("text")).grid(row=numChecked, column=0)
            e = Entry(editWindow).grid(row=numChecked, column=1)
            numChecked += 1


# This allows the user to push the edit button
# ONLY when there is a box checked
def enableEdit():
    for i in checklist:
        if i.var.get() == 1:
            editButton.config(state=NORMAL)
            removeButton.config(state=NORMAL)
            break
        editButton.config(state=DISABLED)
        removeButton.config(state=DISABLED)


class dateTime():
    def __init__(self, month, day, year, hour, minute, ampm):
        self.month = month
        self.day = day
        self.year = year
        self.hour = hour
        self.minute = minute
        self.ampm = ampm


# Currently stores an individual checkbox, will later store dates
class entry():

    def __init__(self, item, date, alert):
        self.var = IntVar()
        self.textStr = item
        self.dateTime = date
        self.dateLabel = Label(text=str(self.dateTime.month) + "/" + str(self.dateTime.day) + "/" +
                                    str(self.dateTime.year) + " " + str(self.dateTime.hour) + ":" +
                                    str(self.dateTime.minute))
        self.alertLabel = alert
        self.c = Checkbutton(root, variable=self.var, text=item, command=enableEdit)


def pushToList(item, year, month, day, hour, minute, ampm):
    global checklist

    # prints new item to main window as long as something was typed in
    if item != "":
        
        #Convert to 24 hour time
        hour = int(hour)
        if ampm == "am":
            if hour == 12:
                hour = 00
        if ampm == "pm":
            if hour != 12:
                hour += 12

        date = datetime(int(year), int(month), int(day), hour, int(minute))
        
        difference = date - curTime
        seconds = difference.total_seconds()
        
        if seconds <= 0:
            alertLabel = Label(text="Past Due", fg="red")
        elif seconds <= 3600:
            alertLabel = Label(text="One hour before due", fg="orange")
        elif seconds <= 86400:
            alertLabel = Label(text="One day before due", fg="green")
        elif seconds <= 604800:
            alertLabel = Label(text="Due within a week", fg="blue")
        else:
            alertLabel = Label(text="")
        
        e = entry(item, date, alertLabel)
        checklist.append(e)
        checklist[len(checklist)-1].c.grid(row=len(checklist), column=0)
        checklist[len(checklist)-1].dateLabel.grid(row=len(checklist), column=1)
        checklist[len(checklist)-1].alertLabel.grid(row=len(checklist), column=2)
        
        


# Opens a new window for the user to input a task
def addItem():
    itemEntry = Tk()
    itemEntry.geometry("400x400")
    eLabel = Label(itemEntry, text="Task:").grid(row=0, column=0)
    e = Entry(itemEntry)
    e.grid(row=0, column=1)
    monthLabel = Label(itemEntry, text="Month:").grid(row=2, column=0)
    month = Entry(itemEntry)
    month.grid(row=2, column=1)
    dayLabel = Label(itemEntry, text="Day:").grid(row=3, column=0)
    day = Entry(itemEntry)
    day.grid(row=3, column=1)
    yearLabel = Label(itemEntry, text="Year:").grid(row=4, column=0)
    year = Entry(itemEntry)
    year.grid(row=4, column=1)
    hourLabel = Label(itemEntry, text="Hour:").grid(row=5, column=0)
    hour = Entry(itemEntry)
    hour.grid(row=5, column=1)
    minLabel = Label(itemEntry, text="Minute:").grid(row=6, column=0)
    minute = Entry(itemEntry)
    minute.grid(row=6, column=1)
    ampmLabel = Label(itemEntry, text="AM/PM:").grid(row=7, column=0)
    ampm = Entry(itemEntry)
    ampm.grid(row=7, column=1)
    confirm = Button(itemEntry, text='Add Item', command=lambda: pushToList(e.get(), year.get(),
                                                                            month.get(), day.get(), hour.get(),
                                                                            minute.get(), ampm.get())).grid(row=8, column=0)
    close = Button(itemEntry, text="Close", command=itemEntry.destroy).grid(row=8, column=1)


def loadTasks():
    try:
        df = pd.read_pickle('pickled.dat')
        if not df.empty:
            for i in range(len(df.axes[0])):
                print(df.iloc[i])
                item, month, day, year, hour, minute = df.iloc[i]

                pushToList(item, month, day, year, hour, minute)

    except:
        print("No saved data.")


def saveTasks():
    df = pd.DataFrame(columns=['task', 'month', 'day', 'year', 'hour', 'minute'])

    for i in checklist:
        df = df.append([{'task': i.textStr, 'month': i.dateTime.month, 'day': i.dateTime.day, 'year': i.dateTime.year,
                         'hour': i.dateTime.hour, 'minute': i.dateTime.minute}])

    df.to_pickle('pickled.dat')


loadTasks()

# If user pushes this button, they can add a new entry to the list
newEntry = Button(root, text="New Entry", padx=50, command=addItem)
newEntry.grid(row=0, column=3)

# This button allows you to edit an entry
editButton = Button(root, text="Edit Entry(s)", padx=50, state=DISABLED, command=editEntry)
editButton.grid(row=0, column=2)

removeButton = Button(root, text="Remove Entry(s)", padx=50, state=DISABLED, command=removeEntry)
removeButton.grid(row=0, column=1)

root.mainloop()

saveTasks()
