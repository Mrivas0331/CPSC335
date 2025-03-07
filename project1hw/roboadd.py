# Project 1 - CPSC 335
# Max Rivas and Marco Macias

class Node:
    # Basic Node class
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    #Basic linkedlist class with defined functionality for inserting at front and back (for remainder)
    def __init__(self):
        self.head = None
        self.last = None
    def insertReverse(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.last = new
        else:
            self.last.next = new
            self.last = new
    def size(self):
        size = 0
        now_node = self.head
        while now_node:
            size += 1
            now_node = now_node.next
        return size
    def printList(self):
        size = 0
        print("Start")
        print("-----")
        now_node = self.head
        while now_node:
            print(now_node.value)
            now_node = now_node.next
        print("-----")
        print("End")

def add_battery(list1, list2):
    remainder = 0
    now_node = list1.head
    now_node2 = list2.head
    while now_node and now_node2:
        now_node.value += now_node2.value + remainder
        remainder = now_node.value // 10
        now_node.value %= 10
        if now_node.next is None and remainder > 0:
            now_node.next = Node(remainder)
            break
        now_node = now_node.next
        now_node2 = now_node2.next

def main():
    list1 = LinkedList()
    list2 = LinkedList()
    listsize = int(input("How many energy values are there: "))
    i = 0
    while i < listsize:
        inp = int(input("Enter an energy value for Robot 1 (0-9): "))
        if inp > 9 or inp < 0:
            print("Only values between 0-9")
            return
        i+=1
        list1.insertReverse(inp)
    i = 0
    print("Now for Robot 2")
    while i < listsize:
        inp = int(input("Enter an energy value for Robot 2 (0-9): "))
        if inp > 9 or inp < 0:
            print("Only values between 0-9")
            return
        i+=1
        list2.insertReverse(inp)
    if list1.size() != list2.size():
        print("Robots have different lengths of energy values!")
        return
    else:
        add_battery(list1, list2)
    list1.printList()
    #list2.printList()

if __name__ == "__main__":
    main()