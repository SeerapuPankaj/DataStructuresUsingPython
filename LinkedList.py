class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Linked List Class Creation

class LinkedList:
    def __init__(self):
        self.head = None
#The Method Append is used to add New Node to the End of the Linked List
    def Append(self,data):
        NewNode = Node(data)
        if self.head == None: #if Head is None Make Head as New Node
            self.head = NewNode
        else:
            temp = self.head
            while temp.next:    #Traverse till the end of the Linked List and Add New Node
                temp = temp.next

            temp.next = NewNode

#The Method Push is used to add New Node to the Beginning of the Linked List
    def Push(self,data):
        NewNode = Node(data)
        if self.head == None:  #if Head is None Make Head as New Node
            self.head = NewNode
        else:
            NewNode.next = self.head
            self.head = NewNode

#The Method InsertAfter is used to add New Node after a Node with Given Data is Found
    def InsertAfter(self, NodeData , Data):
        prevNode = self.head
        nextNode = self.head
        NewNode = Node(Data)
        if self.head == None:
            print("This Method cannot be used if the Given Linked List is Empty")
            return
        else:
            while prevNode != None:
                if prevNode.data == NodeData:
                    nextNode = prevNode.next
                    NewNode.next = nextNode
                    prevNode.next = NewNode
                    return
                else:
                    prevNode = prevNode.next
            if prevNode == None:
                print("The Node with the Given Data was not Found")
        return
#The Method DeleteNode is used to delete a Node with the Given Data of the Linked List Object
    def DeleteNode(self,data):
        currNode = self.head
        prevNode = None
        if self.head != None:
            if self.head.data == data:
                self.head = self.head.next
                currNode = None
            else:
                while currNode.next != None and currNode.next.data != data :
                    currNode = currNode.next
                if currNode.next != None:
                    prevNode = currNode;
                    prevNode.next = prevNode.next.next
                    currNode = None
                else:
                    print("The Node with the Given Data is Not Found in the Linked List")
        else:
            print("This Function cannot be used if the Given Linked List is Empty")

#The Method DeleteNodeN is used to delete the Nth Node in the Linked List
    def DeleteNodeN(self,Position):
        currNode = self.head
        prevNode = self.head
        if self.head != None: #check if the Linked List is empty
            if Position == 0:
                self.head = currNode.next
                currNode = None
            else:
                while currNode != None and Position != 0:
                    prevNode = currNode
                    currNode = currNode.next
                    Position = Position - 1
                if Position == 0:
                    prevNode.next = currNode.next
                    currNode = None
                else:
                    print("Given Position is not found in the Linked List")
        else:
            print("This Function cannot be used if the Given Linked List is Empty")

#Delete the Linked List of the Given Linked List Object
    def DeleteList(self):
        currentNode = nextNode = self.head
        while currentNode != None:
            nextNode = nextNode.next
            currentNode = None
            currentNode = nextNode
        self.head = None
#The Method Display is used to Display the Created Linked List
    def Display(self):
        temp = self.head
        while temp:
            print("{0}->".format(temp.data),end='')
            temp = temp.next


if __name__ == '__main__':
    L1 = LinkedList()
    L1.InsertAfter(10,6)
    L1.Append(5)
    L1.Append(10)
    L1.Append(12)
    L1.Push(14);
    L1.Push(20);
    L1.InsertAfter(12,24)
    L1.InsertAfter(20,18)
    L1.InsertAfter(5,9)
    L1.InsertAfter(78,16)
    L1.Display()
    L1.DeleteNode(24)
    L1.DeleteNode(20)
    L1.DeleteNode(70)
    L1.DeleteNode(5)
    L1.Display()
    L1.DeleteNodeN(0)
    L1.DeleteNodeN(5)
    L1.DeleteNodeN(3)
    L1.DeleteNodeN(1)
    L1.Display()
    L1.DeleteList()
    L1.Display()




