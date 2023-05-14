from time import sleep
from threading import Thread
import sys
import random
import socket
p1=0
p2=0
p3=0
p4=0
plyr=[p1,p2,p3,p4]

s=socket.socket()
s.bind(("192.168.30.73",6000))
s.listen(3)
plyr[0],addr1=s.accept()
plyr[1],addr2=s.accept()
plyr[2],addr3=s.accept()


plyr[0].send(b"3")
plyr[1].send(b"2")
plyr[2].send(b"1")
chns=0

chrc=["c","p","k","m"]
plrscr=["0","0","0","0"]


print("SUCCCESFULLUy STABLE YOUR CONNECTION WITH PLAYERS")


class clss(Thread):
    def run(self):
         while True:
             pass






m=clss()
m.start()


def check(chrc,plrscr):
    if(chrc[0]=="c"):
        plrscr[0]="0000"
        chor=0
    elif(chrc[0]=="p"):
        plrscr[0]="0030"
        police=0
    elif(chrc[0]=="m"):
        plrscr[0]="0050"
        mantri=0
    else:plrscr[0]="0100"

    if (chrc[1] == "c"):
        plrscr[1] = "0000"
        chor=1
    elif (chrc[1] == "p"):
        plrscr[1] = "0030"
        police=1
    elif (chrc[1] == "m"):
        plrscr[1] = "0050"
        mantri=1
    else:
        plrscr[1] = "0100"

    if (chrc[2] == "c"):
        plrscr[2] = "0000"
        chor=2
    elif (chrc[2] == "p"):
        plrscr[2] = "0030"
        police=2
    elif (chrc[2] == "m"):
        plrscr[2] = "0050"
        mantri=2
    else:
        plrscr[2] = "0100"

    if (chrc[3] == "c"):
        plrscr[3] = "0000"
        chor=3
    elif (chrc[3] == "p"):
        plrscr[3] = "0030"
        police=3
    elif (chrc[3] == "m"):
        plrscr[3] = "0050"
        mantri=3
    else:
        plrscr[3] = "0100"

    xy=str(chor)+str(police)
    if(mantri==3):
        print("who is chor",xy[0], "or",  xy[1])
        z=input("::::::::")
        z=int(z)
    else:
        plyr[mantri].send(xy.encode())
        z=plyr[mantri].recv(2048)
        z=int(z)
    if(z==chor):
        return plrscr
    else:
        swap=plrscr[mantri]
        plrscr[mantri]=plrscr[chor]
        plrscr[chor]=swap
        return plrscr








while(True):
    if(chns==0):
        input("ENTER BRO ITS YOUR TURN")
        random.shuffle(chrc)
        plyr[0].send(chrc[0].encode())
        plyr[1].send(chrc[1].encode())
        plyr[2].send(chrc[2].encode())
        I=chrc[3]
        plrscr = check(chrc, plrscr)
        score = plrscr[0] + plrscr[1] + plrscr[2] + plrscr[3]
        print(score)

        for v in range(0, 3):
            plyr[v].send(score.encode())

        chns=1

    else:
        for i in range(0,3):
               if(i==0):
                 pst=plyr[0].recv(4096)
                 pst=pst.decode()
                 chrc=[pst[0],pst[1],pst[2],pst[3]]
               elif(i==1):
                   pst=plyr[1].recv(4096)
                   pst=pst.decode()
                   chrc = [pst[0], pst[1], pst[2], pst[3]]
               elif(i==2):
                   pst=plyr[2].recv(4096)
                   pst=pst.decode()
                   chrc = [pst[0], pst[1], pst[2], pst[3]]
               else:pass
               plyr[0].send(chrc[0].encode())
               plyr[1].send(chrc[1].encode())
               plyr[2].send(chrc[2].encode())
               I = chrc[3]
               plrscr= check(chrc,plrscr)
               score=plrscr[0]+plrscr[1]+plrscr[2]+plrscr[3]
               for v in range(0,3):
                   plyr[v].send(score.encode())
        chns=0









