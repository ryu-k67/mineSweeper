from tkinter import *
import random

#画面の生成
root=Tk()
root.title("mineSweeper")
root.resizable(1,1) #画面サイズの変更　0:変更不可、1:変更可


status_frame=Frame(root,width=300,height=50,relief="sunken",borderwidth=5,bg="LightGray") #reliefは「flat」「sunken」「groove」「ridge」「raised」が選択できる
game_frame=Frame(root,width=300,height=300,relief="sunken",borderwidth=5,bg="LightGray")

status_frame.pack(pady=5,padx=5)
game_frame.pack(pady=5,padx=5)

bomb_list=[]

def left_click(event):
    event.widget.configure(relief="ridge",bd="2")
    print(event.widget.num)
    except_num=event.widget.num

    if not bomb_list:
        while len(bomb_list)!=square/8:
            bomb_num=random.randint(0,square-1)
            if bomb_num!=except_num and (bomb_num in bomb_list)==False:
                bomb_list.append(bomb_num)
    bomb_count=search_bomb(bomb_list,event.widget.num)
    if bomb_count==9:
        print("地雷を踏みました")
        for i in bomb_list:
            frame_list[i].configure(bg="red")
        for i in frame_list:
            i.bind("<Button-1>",stop)
    else:
        print(bomb_count)
        bomb_count_label=Label(event.widget,text=bomb_count,bg="LightGray")
        bomb_count_label.place(width=26,height=26)
        event.widget.bind("<Button-1>",stop)


def right_click(event):
    frag_label=Label(event.widget,text="F",bg="LightGray")
    frag_label.place(width=20,height=20)
    


def stop(event):
    pass


i=0
frame_list=[]
height=9
width=16
square=height*width #マスの総数
for x in range(height):
    for y in range(width):
        frame=Frame(game_frame,width=30,height=30,bd="5",relief="raised",bg="LightGray")
        frame.bind("<Button-1>",left_click)
        frame.bind("<Button-3>",right_click)
        frame.num=i
        frame_list.append(frame)
        frame.grid(row=x,column=y)
        i+=1


def search_bomb(list,num):
    around_list=[]
    bomb_count=0
    if num in list:
        return 9
    if num % width==0: #左端
        around_list.append(num-width)
        around_list.append(num-width+1)
        around_list.append(num+1)
        around_list.append(num+width)
        around_list.append(num+width+1)
    elif num % width==width-1: #右端
        around_list.append(num-width-1)
        around_list.append(num-width)
        around_list.append(num-1)
        around_list.append(num+width-1)
        around_list.append(num+width)
    elif num < width: #上端
        around_list.append(num-1)
        around_list.append(num+1)
        around_list.append(num+width-1)
        around_list.append(num+width)
        around_list.append(num+width+1)
    elif num > height*(width-1): #下端
        around_list.append(num-width-1)
        around_list.append(num-width)
        around_list.append(num-width+1)
        around_list.append(num-1)
        around_list.append(num+1)
    else: #周りに8マスある
        around_list.append(num-width-1)
        around_list.append(num-width)
        around_list.append(num-width+1)
        around_list.append(num-1)
        around_list.append(num+1)
        around_list.append(num+width-1)
        around_list.append(num+width)
        around_list.append(num+width+1)

    for i in around_list:
        if i in list:
            bomb_count+=1

    return bomb_count



root.mainloop()

