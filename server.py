import tkinter
import threading
import socket

users = {}

def run(ck,ca):
   userName = ck.recv(1024)
   users[userName.decode("utf-8")] = ck
   print(users)

   while True:
       rData = ck.recv(1024)
       dataStr = rData.decode("utf-8")
       infoList = dataStr.split(":")
       #xym:sunck is a good man
       users[infoList[0]].send(infoList[1].encode("utf-8"))


def start():
    ipStr = eip.get()
    portStr = eport.get()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ipStr, int(portStr)))
    server.listen(10)

    printStr = "服务器启动成功"
    text.insert(tkinter.INSERT, printStr)

    while True:
        ck, ca = server.accept()
        t = threading.Thread(target=run, args=(ck, ca))
        t.start()


def startServer():
    s = threading.Thread(target=start)
    s.start()





win = tkinter.Tk()
win.title("QQ服务器")
win.geometry("400x400+200+20")

labelIP = tkinter.Label(win,text= "ip").grid(row = 0,column = 0)
labelPort = tkinter.Label(win,text= "port").grid(row = 1,column = 0)

eip = tkinter.Variable()
eport = tkinter.Variable()

entryIP = tkinter.Entry(win,textvariable = eip).grid(row = 0,column = 1)
entryPort = tkinter.Entry(win,textvariable = eport).grid(row = 1,column = 1)

button = tkinter.Button(win,text = "启动",command = startServer).grid(row = 2,column = 0)

text = tkinter.Text(win,width = 30,height = 10)
text.grid(row = 3,column = 0)



win.mainloop()