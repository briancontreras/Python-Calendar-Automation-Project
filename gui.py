from tkinter import *



#creating the root window
root = Tk()
root.geometry("800x500")
root.title("Calendar Automation App")
root.configure(bg="#83a6eb")

#creating the title label for this GUI
myLabel = Label(root, text="Python Calendar Automation")
myLabel.place(relx=0.5,rely=0.025,anchor=CENTER)

myLabel.grid(row=0,column=0, padx=300, pady=50)

def clicked():
    functionLabel = Label(root,text="The button was clicked")
    functionLabel.grid(row=1,column=1)

def openNewWindow():
    appWindow = Tk()
    appWindow.geometry("800x500")
    appWindow.title("Application")
    val = True
    if val:
        appWindowLabel = Label(appWindow, text="Credentails recgonized going to next screen")
        appWindowLabel.pack()
        appWindow.destroy()
        calendarWindow = Tk()
        calendarWindow.geometry("800x500")
        calendarWindow.title("This should be your calendar ")

    else:
        appWindowLabel = Label(appWindow,text="Please give credentials to continue")
        appWindowLabel.pack()
    appWindow.mainloop()
    
def destroyWindow():
    root.destroy()

myButtonStart = Button(root, text="Start Application",height=5,width=25,command=openNewWindow).grid(row=1,column=0, pady=10)
myButtonExit = Button(root, text="Exit Application",height=5,width=25,command=destroyWindow).grid(row=2,column=0, pady=10)
myButtonAbout = Button(root, text="About Application",height=5,width=25).grid(row=3,column=0, pady=10)



root.mainloop()