import tkinter as tk
import screen_yes
import cong_pic
import time
import keyboard
import pyperclip
import web
import _thread

search_sw = False
#截图函数
def cut():
    screen_yes.cut()
    recognize()

#识别函数
def recognize():
    
    words = cong_pic.main()
    
    text1.delete('1.0', tk.END)
    #for i in nunbers:
    text1.insert("insert", words)

#复制文本到粘贴板
def copy_words():
    text_content = (text1.get("0.0","end").replace(" ","")).split("\n")
    text_content.pop()
    text = "".join(text_content)
    pyperclip.copy(text) 
    print("--复制成功!--")

#搜索函数
def search():
    try:
        text_content = (text1.get("0.0","end").replace(" ","")).split("\n")
        text_content.pop()
        text = "".join(text_content)
        web.search(text)
        print("搜索完成")
    except:
        print("搜索中止")
def do_search():
    global search_sw
    search_sw = True
    print("开始搜索")


#快捷键
def rect(delay,key,name):
    global search_sw
    while True:
        time.sleep(delay)
        if search_sw == True:
            search_sw = False            
            print("来！")
            search()


'''        
if name == "search":
    keyboard.wait("Ctrl+"+key)
    search()
'''
#清空函数
def clear(text):
    text.delete('1.0', tk.END)


#鼠标事件
def callback(event):
    #print("at", event.x, event.y)
    if event.y > 200 and event.y < 300:
        clear(text1)

        print("清空") 

#键盘事件
def key_function(event):
    #print("type = ", type(event))
    #print("event.char = ", event.char)
    #print("event.keycode = ", event.keycode)
    #print("event = ", event)
    if event.keycode == 112:
        cut()

#获取text部件数据
def get_resluts(text,list_):
    text_content = (text.get("0.0","end").replace(" ","")).split("\n")
    text_content.pop()#列表最后一个元素是空删除它
    list_.clear()
    for i in text_content:
        if i != "":
            list_.append(i)
    #print("获取到text框里的列表为",list_)
    return list_


#tkinter初始化 
root = tk.Tk()
root.title(" ")
root.geometry("190x110")
root.attributes('-topmost', True)

root.bind("<Key>", key_function)
root.bind("<Button-1>", callback)

#快捷键识别线程
_thread.start_new_thread(rect,(0.1, "s", "search"))

text1 = tk.Text(root, width=22, height=4)

button1=tk.Button(root,text="截图",font=('微软雅黑', 10),command=cut)

button2=tk.Button(root,text="搜索",font=('微软雅黑', 10),command=do_search)

button3=tk.Button(root,text="复制",font=('微软雅黑', 10),command=copy_words)

button4=tk.Button(root,text="清空",font=('微软雅黑', 10),command=lambda:clear(text1))
#控件布局
text1.place(x=20, y=10)
button1.place(x=20, y=70)
button2.place(x=60, y=70)
button3.place(x=100, y=70)
button4.place(x=140,y=70)

root.mainloop()