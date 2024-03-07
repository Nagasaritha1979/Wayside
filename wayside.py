from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

win=Tk()
win.title('WAYSIDE')
win.geometry('300x150')

win.config(bg='green')



label1=Label(win,text='WAYSIDE', font=("Arial",20),bg='green',fg='black')
label1.place(x=20,y=20)

label2=Label(win,text='SCHOOL',font=("Arial",20),bg='green',fg='black')
label2.place(x=800,y=20)

sep=ttk.Separator(win, orient='horizontal')
sep.place(x=0,y=60, relwidth=1,relheight=0.0)

wayside1_=Image.open('wayside1.jpg')
wayside1=wayside1_.resize((500,500))
wayside1_img=ImageTk.PhotoImage(wayside1,master=win)

wayside2_=Image.open('wayside2.jpg')
wayside2=wayside2_.resize((500,500))
wayside2_img=ImageTk.PhotoImage(wayside2,master=win)

wayside3_=Image.open('wayside3.jpg')
wayside3=wayside3_.resize((500,500))
wayside3_img=ImageTk.PhotoImage(wayside3,master=win)

wayside4_=Image.open('wayside4.jpg')
wayside4=wayside4_.resize((500,500))
wayside4_img=ImageTk.PhotoImage(wayside4,master=win)

images=[wayside1_img,wayside2_img,wayside3_img,wayside4_img]

label4=Label(win,bg='green')
label4.pack(side=TOP,fill=X,expand=True)

def update(i):
    if i<=3:
        
        label4.config(image=images[i])
        i+=1
        win.after(1000,update,i)
        win.update()
    else:
        i=0
        win.after(1000,update,i)
        

update(0)

win.mainloop()
