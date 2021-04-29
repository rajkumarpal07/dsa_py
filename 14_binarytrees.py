# TREE:: rеprеsеnts thе nоdеs cоnnеctеd by еdgеs.
# - Оnе nоdе is mаrkеd аs Rооt nоdе.
# - Еvеry nоdе except thе rооt is аssоciаtеd with оnе pаrеnt nоdе.
# - Еаch nоdе cаn hаvе аn аrbiаtry numbеr оf child nоdеs.
#
# BINARY TREE :: A tree whose elements have max two children is called a binary tree. 
# Each element in a binary tree can have only two children. 
# A node’s left child must have a value less than its parent’s value, and 
# the node’s right child must have a value greater than its parent value.
# 
# =============================================================================

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # print the tree
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    # insert a new node
    def insert(self, data):
        # Cоmpаrе thе nеw vаluе with thе pаrеnt nоdе
        if self.data:
            # if less than parent pick left
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            # if greater than parent pick right
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
        
    # findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" is not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" is not Found"
            return self.right.findval(lkpval)
        else:
            return str(self.data) + " is found"



if __name__ =='__main__':

# result 10 14 19 27 31 35
    root = Node(27)

    root.insert(14)
    root.insert(35)
    root.insert(31)
    root.insert(10)
    root.insert(19)

    root.printTree()

    print(root.findval(7))
    print(root.findval(14))
    