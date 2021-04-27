# QUEUE::
# Dаtа еlеmеnts аrе аrrаngеd in а quеuе. 
# Items are added at the end and removed from the start
#
# FIFO 
# implemented using a Python list
#
# =============================================================================

class Queue:
    def __init__(self):
        self.queue = list()

    def add2Q(self, dataval):
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        return False

    def removefromQ(self):
        if len(self.queue) >0:
           return self.queue.pop()
        return("Queue is empty")     
    
    def size(self):
        return len(self.queue)
    

if __name__ == '__main__':
    myq = Queue()
    myq.add2Q("Mon")
    myq.add2Q("Tue")
    myq.add2Q("Wed")
    myq.add2Q("Thu")
    myq.add2Q("Fri")
    myq.add2Q("Sat")

    print(myq.removefromQ())
    print(myq.removefromQ())

