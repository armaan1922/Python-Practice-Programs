class Node:
    def __init__(self, data):
        self.data = data
        self.nlink = None
        self.plink = None


class DoublyLL:
    def __init__(self):
        self.head = None

    def add_beg(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nlink = self.head
            self.head.plink = new_node
            self.head = new_node

    def add_end(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            n = self.head
            while n.nlink is not None:
                n = n.nlink
            new_node = Node(data)
            n.nlink = new_node
            new_node.plink = n

    def add_after(self, x, data):
        if self.head is None:
            print("Linked list is empty")
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.nlink
        if n is None:
            print("item not found in list !")
        else:
            new_node = Node(data)
            new_node.nlink = n.nlink
            new_node.plink = n

            if n.nlink is not None:
                n.nlink.plink = new_node
            n.nlink = new_node








    def print(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.nlink






ll1 = DoublyLL()
ll1.add_beg(1)
ll1.add_after(1,4)
ll1.add_after(4,6)
ll1.add_beg(0)
ll1.add_end(12)

ll1.print()