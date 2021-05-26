import currencycmds
from tkinter import *

root=Tk()

root.title("MemeBot Bot")

root.geometry('500x350')

header=Label(root, text ="A bot to farm currency in Dank Memer",font="20")
header.grid()

space=Label(root, text =" ",font="20")
space.grid()

body=Label(root, text ="Pick the cmds below based on items in inventory. \n If user has shovel -- enable dig \n Hunting has instances that can kill the user, enabling it is not advised \n After hitting run click on the mssg input area on discord \n To stop the program close the python program that pops up")
body.grid()

checkbutton1 = IntVar()  
checkbutton2 = IntVar()  
checkbutton3 = IntVar()
checkbutton4 = IntVar()
  
button1 = Checkbutton(root, text = "Postmeme", 
                      variable = checkbutton1,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)
  
button2 = Checkbutton(root, text = "Hunt",
                      variable = checkbutton2,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)
  
button3 = Checkbutton(root, text = "Fish",
                      variable = checkbutton3,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)

button4 = Checkbutton(root, text = "Dig",
                      variable = checkbutton4,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)

exebutton = Button(root, text = "Run !" , bd="5", command = root.destroy)
    
button1.grid()  
button2.grid()  
button3.grid()
button4.grid()
exebutton.grid()
root.mainloop()

currencycmds.farm(checkbutton1.get(),checkbutton2.get(),checkbutton3.get(),checkbutton4.get())
