class Node():
    def __init__(self, x=None):
        self.data = x
        self.next = None

def initList(data=[]):
    if data.__len__() == 0:
        return Node()

    head = Node()
    pre = head
    for nodeData in data:
        node = Node(nodeData)
        pre.next = node
        pre = node
    pre.next = None
    return head

def displayList(head):
    if head is None or head.next is None:
        print(None)
        return

    firstNode = head.next
    while(firstNode != None):
        print(firstNode.data, end=' ')
        firstNode = firstNode.next
    print('\n')

def removeRepeatedNode(head):
    if head is None or head.next is None:
        return head

    existNode = []
    pre = head
    subNode = head.next
    while(subNode != None):
        if subNode.data in existNode:
            pre.next = subNode.next
            subNode = subNode.next
        else:
            existNode.append(subNode.data)
            pre = subNode
            subNode = subNode.next
    return head

head = initList([1, 3, 4, 1, 1, 2, 2, 3, 2, 2, 2])
displayList(head)
head = removeRepeatedNode(head)
displayList(head)


