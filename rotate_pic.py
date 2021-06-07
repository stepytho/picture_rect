import tkinter as tk
import screen_yes
import _thread
import time
import keyboard


path_left = "test_anti_angle.png"
path_right = "test_angle.png"
path = "test.png"

def rec_left(delay):
    
    while True:
        time.sleep(delay)
        keyboard.wait("q")
        #print("左截屏")
        cut_left()
        

def rec_right(delay):
    
    while True:
        time.sleep(delay)
        keyboard.wait("w")
        #print("右截屏")
        cut_right()
        
def rec(delay):
    
    while True:
        time.sleep(delay)
        keyboard.wait("capslock")
        screen_yes.show_pic(path)
        
                
def cut():
    screen_yes.cut()

def cut_left():
    screen_yes.cut()
    screen_yes.show_pic(path_left)
def cut_right():
    screen_yes.cut()
    screen_yes.show_pic(path_right)

def key_function(event):
    #print("type = ", type(event))
    #print("event.char = ", event.char)
    #print("event.keycode = ", event.keycode)
    #print("event = ", event)
    if event.keycode == 32:
        cut()
    elif event.keycode == 81:
        cut_left()
    elif event.keycode == 87:
        cut_right()


#tkinter初始化 
root = tk.Tk()
root.title("截图旋转")
root.geometry("300x300")
root.attributes('-topmost', True)

root.bind("<Key>", key_function)

_thread.start_new_thread(rec_left, (0.1,))
_thread.start_new_thread(rec_right, (0.1,))
_thread.start_new_thread(rec, (0.1,))

#button1=tk.Button(root,text="截图",font=('微软雅黑', 44),command=cut, bg="OliveDrab")
#button1.pack()
button1=tk.Button(root,text="左旋",font=('微软雅黑', 44),command=cut_left, bg="Khaki")
button1.pack()
button2=tk.Button(root,text="右旋",font=('微软雅黑', 44),command=cut_right, bg="PowderBlue")
button2.pack()

root.mainloop()