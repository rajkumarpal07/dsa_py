# STACK::
# stаck mеаns аrrаnging оbjеcts оn оvеr аnоthеr.
# Stack allows operations at one end of it. => namely at the Top
# PUSH:Addition and POP:Deletion happens only at the Top
# Lаst in First Оut(LIFО) fеаturе
# 
# =============================================================================

class Stack:
    def __init__(self):
        self.stack = []

    # Usе list аppеnd mеthоd tо аdd an еlеmеnt
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    # To Look at the Top
    def peek(self):
        return self.stack[-1]

    # To remove element from Top
    def remove(self):
        if len(self.stack) <=0:
            return ("Stack is empty")
        else:
            return self.stack.pop()
        


if __name__ =='__main__':

    mystack = Stack()
    mystack.add("Mon")
    mystack.add("Tue")
    mystack.add("Wed")
    mystack.add("Thu")
    mystack.add("Fri")
    mystack.add("Sat")

    print(mystack.peek())

    print(mystack.remove())
    print(mystack.remove())


