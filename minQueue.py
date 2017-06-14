class minQueue(object):
    def __init__(self):
        self.queue = []
        self.minq = []
    def enqueue(self, x):
        self.queue.append(x)
        temp = []
        for n in self.minq:
            if x >= n:
                temp.append(n)
        temp.append(x)
        self.minq = temp
        print self.minq
    def dequeue(self):
        x = self.queue.pop(0)
        if self.minq[0] == x:
            self.minq.pop(0)
        return x
    def findmin(self):
        return self.minq[0]

def test():
    t = minQueue()
    for n in [5,1,4,7]:
        t.enqueue(n)
        print t.findmin()
    print t.dequeue(), t.findmin()
    print t.dequeue(), t.findmin()
    print t.dequeue(), t.findmin()
    print t.dequeue(), t.findmin()
    #print t.dequeue(), t.findmin()


test()
