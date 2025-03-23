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
        #Used to insert in reverse order
    def insertReverse(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.last = new
        else:
            self.last.next = new
            self.last = new
        #Used for the user input
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
    #Iterate until the node doesnt exist anymore
    while now_node and now_node2:
        #adds the value of LL2 to LL1 and any remainder
        now_node.value += now_node2.value + remainder
        # remainder should always be 1
        remainder = now_node.value // 10
        now_node.value %= 10
        if now_node.next is None and remainder > 0:
            # Append new node is remainder exist on last node
            now_node.next = Node(remainder)
            break
        # Iterates to the next node
        now_node = now_node.next
        now_node2 = now_node2.next

def main():
    list1 = LinkedList()
    list2 = LinkedList()
    # Takes user input for the length of robot linked list
    listsize = int(input("How many energy values are there: "))
    i = 0
    while i < listsize:
        # Takes user input for linked list
        inp = int(input("Enter an energy value for Robot 1 (0-9): "))
        if inp > 9 or inp < 0:
            print("Only values between 0-9")
            return
        i+=1
        # Iterates and appends to end
        list1.insertReverse(inp)
    i = 0
    print("Now for Robot 2")
    while i < listsize:
        # Everything here is the same as above, but for the second robot
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
    # Prints final result here
    list1.printList()
    #list2.printList()

if __name__ == "__main__":
    main()