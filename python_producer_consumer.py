from threading import *
import time,random,queue

class Prod:
    def __init__(self):
        self.product=['jaya','ram','dood','soue']
        self.next=0

    def run(self):
        global q
        while(time.clock()<10):
            if(self.next<time.clock()):
                f=self.product[random.randrange(len(self.product))]
                g=self.product[random.randrange(len(self.product))]
                q.put(f)
                q.put(g)
                print("Added: {}".format(f),time.clock())
                self.next+=random.random()


class Comnsumer:
    def __init__(self):
        self.next =0

    def run(self):
        global q
        while(time.clock() < 10):
            if (self.next < time.clock() and not q.empty()):
                f=q.get()
                print("Remove: {}".format(f))
                self.next +=random.random()
            elif q.empty():
                print("consumer is waiting for product !",time.clock())


if __name__ == '__main__':
    q = queue.Queue()
    p = Prod()
    c = Comnsumer()

    pt = Thread(target=p.run, args = ())
    
    ct = Thread(target=c.run, args = ())
    ct1 = Thread(target=c.run, args = ())

    pt.start()
    time.sleep(0.05)
    ct.start()
    ct1.start()
    

    pt.join()
    ct.join()
    ct1.join()
    print("******* bye *******")
    
