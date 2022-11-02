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
bomb_count_list=[]
def left_click(event):
    event.widget.configure(relief="ridge",bd="2")
    print(event.widget.num)
    except_num=event.widget.num

    if not bomb_list:
        while len(bomb_list)<=square/5:
            bomb_num=random.randint(0,square-1)
            if bomb_num!=except_num and (bomb_num in bomb_list)==False:
                bomb_list.append(bomb_num)
        for i in range(square):
            bomb_count=search_bomb(bomb_list,i)
            bomb_count_list.append(bomb_count)
    ct=bomb_count_list[event.widget.num]
    # print(ct)
    if ct==9:
        print("地雷を踏みました")
        for i in bomb_list:
            frame_list[i].configure(bg="red")
        for i in frame_list:
            i.bind("<Button-1>",stop)
        for i in frag_list:
            i.place_forget()
    else:
        # print(ct)
        open_neighbor(event.widget.num)


def stop():
    pass


frag_list=[]
def right_click(event):
    if frag_list:
        frag_num=frag_list[-1].num
    else:
        frag_num=0

    frag_label=Label(event.widget,text="F",fg="red",bg="LightGray")
    frag_label.place(width=20,height=20)
    frag_label.num=frag_num
    frag_label.bind("<Button-3>",delete_frag)
    frag_list.append(frag_label)
    # event.widget.bind("<Button-3>",stop)


def delete_frag(event):
    frag_list.remove(event.widget)
    event.widget.place_forget()
    # event.widget.bind("<Button-3>",right_click)


def open_neighbor(num):
    
    if frame_list_frag[num]!=1:
        frame_list[num].configure(relief="ridge",bd="2")
        bomb_count_label=Label(frame_list[num],text=bomb_count_list[num],bg="LightGray")
        bomb_count_label.place(width=26,height=26)
        frame_list[num].bind("<Button-1>",stop)
        frame_list_frag[num]=1
        if bomb_count_list[num]==0:
            print(num)
            if num % width==0: #左端
                open_neighbor(num-width)
                open_neighbor(num-width+1)
                open_neighbor(num+1)
                open_neighbor(num+width)
                open_neighbor(num+width+1)
            elif num % width==width-1: #右端
                open_neighbor(num-width-1)
                open_neighbor(num-width)
                open_neighbor(num-1)
                open_neighbor(num+width-1)
                open_neighbor(num+width)
            elif num < width: #上端
                open_neighbor(num-1)
                open_neighbor(num+1)
                open_neighbor(num+width-1)
                open_neighbor(num+width)
                open_neighbor(num+width+1)
            elif num > (square-width): #下端
                open_neighbor(num-width-1)
                open_neighbor(num-width)
                open_neighbor(num-width+1)
                open_neighbor(num-1)
                open_neighbor(num+1)
            else: #周りに8マスある
                open_neighbor(num-width-1)
                open_neighbor(num-width)
                open_neighbor(num-width+1)
                open_neighbor(num-1)
                open_neighbor(num+1)
                open_neighbor(num+width-1)
                open_neighbor(num+width)
                open_neighbor(num+width+1)


i=0
frame_list=[]
frame_list_frag=[]
height=10
width=20
square=height*width #マスの総数
for x in range(height):
    for y in range(width):
        frame=Frame(game_frame,width=30,height=30,bd="5",relief="raised",bg="LightGray")
        frame.bind("<Button-1>",left_click)
        frame.bind("<Button-3>",right_click)
        frame.num=i
        frame_list.append(frame)
        frame_list_frag.append(0)
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
    elif num > (square-width): #下端
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

