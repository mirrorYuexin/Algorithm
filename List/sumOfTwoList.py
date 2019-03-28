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
        subNode = Node(nodeData)
        pre.next = subNode
        pre = subNode

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

def sumTwoLists(headA, headB):
    if headA is None or headB is None or headA.next is None or headB.next is None:
        return

    subNodeA = headA.next
    subNodeB = headB.next
    resHead = Node()
    resPre = resHead
    isCarry = 0

    while subNodeA != None and subNodeB != None:
        newNode = Node()
        newNode.data = subNodeA.data + subNodeB.data
        if isCarry == 1:
            newNode.data = newNode.data + 1
            isCarry = 0
        if newNode.data >= 10:
            isCarry = 1
            newNode.data = newNode.data % 10
        subNodeA = subNodeA.next
        subNodeB = subNodeB.next
        resPre.next = newNode
        resPre = newNode

    while subNodeA != None:
        newNode = Node()
        newNode.data = subNodeA.data + isCarry
        if newNode.data >= 10:
            isCarry = 1
            newNode.data = newNode.data % 10
        subNodeA = subNodeA.next
        resPre.next = newNode
        resPre = newNode

    while subNodeB != None:
        newNode = Node()
        newNode.data = subNodeB.data + isCarry
        isCarry = 0
        if newNode.data >= 10:
            isCarry = 1
            newNode.data = newNode.data % 10
        subNodeB = subNodeB.next
        resPre.next = newNode
        resPre = newNode

    if isCarry == 1:
        newNode = Node(1)
        resPre.next = newNode
        resPre = newNode
    resPre.next = None
    return resHead

def displayNum(head):
    if head is None or head.next is None:
        print(None)
        return

    firstNode = head.next
    temp = []
    while firstNode is not None:
        temp.append(firstNode.data)
        firstNode = firstNode.next

    flag = 0 # remove the needless zero
    for num in temp[::-1]:
        if num != 0:
            flag = 1
        if flag == 1:
            print(num, end=' ')
    if flag == 0:
        print(0)
    else:
        print('\n')


headA = initList([0, 5, 1])
headB = initList([7, 0, 1])
# displayList(headA)
# displayList(headB)
displayNum(headA)
displayNum(headB)

res = sumTwoLists(headA, headB)
# displayList(res)
displayNum(res)
