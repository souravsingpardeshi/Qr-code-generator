from tkinter import *
import pyqrcode
#window is parent
window = Tk()
#title of gui
window.title("QR Creator by rohit kharve")
#size of window
window.geometry('350x200')
lb  = Label(window, text="Enter URL/Message :-")
lb.grid(column=0 , row=0)
lbl = Label(window, text="")

lbl.grid(column=0, row=3)

txt = Entry(window,width=55)

txt.grid(column=0, row=1)
#when button is clicked this code will run
def clicked():
    res = ""+txt.get()
    url=pyqrcode.create(res)
    url.svg('qr.svg',scale=8)
    res="QR code created successfully for (saved in root diarectory):-"+res
    lbl.configure(text=res)
#button initialised and clicked function is called
btn = Button(window, text="Create", command=clicked)

btn.grid(column=0, row=5)
#exit loop
window.mainloop()
