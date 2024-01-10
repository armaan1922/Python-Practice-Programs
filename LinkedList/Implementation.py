class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_beginning(self, data):
        new_node = Node(data)
        new_node.link = self.head
        self.head = new_node

    def add_ending(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                n = n.link
            n.link = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.link
        if n is None:
            print("Element does not exist in linked list")
        else:
            new_node = Node(data)
            new_node.link = n.link
            n.link = new_node

    def delete_first(self):
        if self.head is None:
            print("Linked list is empty! cant delete nodes")
        else:
            self.head = self.head.link

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty! cant delete nodes")
        elif self.head.link is None:
            self.head = None
        else:
            n = self.head
            while n.link.link is not None:
                n = n.link
            n.link = None

    def print(self):
        if self.head is None:
            print("Empty LinkedList")
        else:
            n = self.head
            while n is not None:
                print(n.data, " --> ", end=" ")
                n = n.link


ll = LinkedList()

ll.add_beginning(5)
ll.add_beginning(7)
ll.add_beginning(12)
ll.add_beginning(3)
ll.add_after(4, 12)
print("Linked list is : ")
ll.print()
ll.delete_first()
print("\n\nAfter deleting first element:")
ll.print()
ll.delete_end()
print("\n\nAfter deleting last element:")
ll.print()
