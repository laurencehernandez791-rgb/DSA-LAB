class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        
        
def insertNodeAtTheBeginning(data):
    global head
    newNode = Node(data)

    if(head == None):
        head = newNode
    else:
        newNode.next = head
        head = newNode 


def insertNodeAtTheEnd(data):
    global head 
    newNode = Node(data)

    if(head == None):
        head= newNode
    else:
        current = head
        while(current.next):
            current = current.next
        current.next = newNode

def traverseLinked():
    current = head
    while(current):
        print(current.data, end=" ->")
        current = current.next
        
        
def insertAfterGivennode(data, node):
    global head
    newNode = Node(data)

    if(head == None):
        head = newNode
    else:
        current = head
        prev = head

    while(prev.data != node):
        prev = current
        current = current.next

        if(current == None):
            print('The node does not exist')
            return
        
    newNode.next = current 
    prev.next = newNode
  
node1 = Node('Risk It All by brunomars')
head = node1
insertNodeAtTheBeginning('Makaluma by Wilbert Ross')
insertNodeAtTheBeginning('To The Bone by PAMUNGKAS')
insertNodeAtTheBeginning('Pagsamo by ARTHUR')

insertNodeAtTheEnd('Palayo sa Mundo by Moira DELA TORRE')
insertNodeAtTheEnd('Paalam,Leonora by Sugarcane')

insertAfterGivennode('count on me by bruno mars', 'just the way you are by brunomars')
traverseLinked()