from tkinter import *
from turtle import width

#画面の生成
root=Tk()
root.title("mineSweeper")
root.resizable(1,1) #画面サイズの変更　0:変更不可、1:変更可


status_frame=Frame(root,width=300,height=50,relief="sunken",borderwidth=5,bg="LightGray") #reliefは「flat」「sunken」「groove」「ridge」「raised」が選択できる
game_frame=Frame(root,width=300,height=300,relief="sunken",borderwidth=5,bg="LightGray")

status_frame.pack(pady=5,padx=5)
game_frame.pack(pady=5,padx=5)


def left_click(event):
    event.widget.configure(relief="ridge",bd="2")
    print(event.widget.num)

i=0
frame_list=[]
width=9
height=16
for x in range(width):
    for y in range(height):
        frame=Frame(game_frame,width=30,height=30,bd="5",relief="raised",bg="LightGray")
        frame.bind("<1>",left_click)
        frame.num=i
        frame_list.append(frame)
        frame.grid(row=x,column=y)
        i+=1






root.mainloop()

