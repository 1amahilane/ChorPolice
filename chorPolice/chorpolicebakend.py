from time import sleep
from threading import Thread
import sys
import random
import socket
s=socket.socket()
s.connect(("192.168.30.73",6000))
chns=int(s.recv(1024))

player1=0
player2=0
playerser=0
player3=0

char=["c","p","k","m"]


def des(de):
    x=int(de[0])
    y=int(de[1])
    print("who is chor",x, "or",   y)
    who=input("::::::::")

    s.send(who.encode())










class clss(Thread):
    def run(self):
         while True:
           pass
m=clss()

m.chh=0



I=0
chrctr=["king","chor","police","mantri"]

while(True):
    if (chns == 0):
        input("ENTER ITS YOUR TURN")
        random.shuffle(char)
        pst = (char[0] + char[1] + char[2] + char[3])
        s.send(pst.encode())
        r = s.recv(1024)
        r = r.decode()
        I = r
        if (chns == 3):
            chns = 0
        else:
            chns = chns + 1

    else:
        r = s.recv(1024)
        r = r.decode()
        I = r
        if (chns == 3):
           chns = 0
        else:
            chns = chns + 1



    if(I=="c"):
        print("chor")
    elif(I=="p"):
        print("police")
    elif(I=="k"):
        print("king")
    elif(I=="m"):
        print("minister")
        r = s.recv(1024)
        de = r.decode()
        des(de)

    scr=s.recv(4096)
    scr=scr.decode()

    print(scr)
    player1 =int(scr[0]+scr[1]+scr[2]+scr[3])
    player2 =int(scr[4]+scr[5]+scr[6]+scr[7])
    player3 =int(scr[8]+scr[9]+scr[10]+scr[11])
    playerser = int(scr[12]+scr[13]+scr[14]+scr[15])

    scr=0
    r=0
    I=0