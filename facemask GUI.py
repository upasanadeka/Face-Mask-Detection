from tkinter import *
from tkinter import Canvas
root = Tk()
root.geometry("400x280")
root.title(" Face Mask Detector")
root.resizable(False, False)
 
frm1 = Frame(root, highlightbackground="black" , highlightcolor="black",
             highlightthickness=2, width=400,height=300, bd=0)
frm1.pack()
frm1.pack_propagate(False)
lblfrstrow = Label(root, text ="Username", )
lblfrstrow.place(x = 100, y = 20)
 
Username = Entry(root, width = 55)
Username.place(x = 190, y = 20, width = 110)
  
lblsecrow = Label(root, text ="Password")
lblsecrow.place(x = 100, y = 50)
 
password = Entry(root, width = 55)
password.place(x = 190, y = 50, width = 110)


loginbtn = Button(root, text ="Admin Login")
loginbtn.place(x = 100, y = 100, width = 200)


line= Canvas(root,width=300,height=1, bg="black")
line.place(x=50,y=150)


launchbtn = Button(root, text="Launch Camera", bg="red", height=3)
launchbtn.place(x=100,y=170, width=200)



root.mainloop()


