from threading import Thread
import time
kc=0

class ch(Thread):
    name=""
    count = 0
    def run(self) -> None:
        global kc
        while True:
            if kc <500:
                self.count+=1
                kc+=1
            print(self.name, "做了", self.count,)
class gk(Thread):
    name = ""
    q=0
    def run(self) -> None:
        global kc
        while True:
            if kc>0:
                kc-=1
                self.q+=1
            print(self.name,"抢购了",self.q)


c1=ch()
c2=ch()
c3=ch()
c1.name = "德莱文"
c2.name = "瑞文"
c3.name = "塔姆"
c1.start()
c2.start()
c3.start()

l1=gk()
l2=gk()
l3=gk()
l4=gk()
l5=gk()
l6=gk()
l1.name = "阿木木"
l2.name = "狼人"
l3.name = "吉格斯"
l4.name = "德莱厄斯"
l5.name = "卡特琳娜"
l6.name = "卡特林"
l1.start()
l2.start()
l3.start()
l4.start()
l5.start()
l6.start()