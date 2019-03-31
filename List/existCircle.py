class Node():
    """
    define the data structure of single node
    """
    def __init__(self, x=None):
        self.data = x
        self.next = None


def initList(data=[]):
    """
    init a List according to the input sequence: data
    :param data: a sequence of data belong to each node in the list
    :return: the head of the list
    """
    if data.__len__() == 0:
        return Node() #return an empty list

    head = Node
    pre = head

    for x in data:
        subNode = Node(x)
        pre.next = subNode
        pre = subNode
        subNode.next = None

    return head

def creatCircle(head):
    """
    let the last node point to the first node
    :param head: head of the list
    :return:
    """
    if head == None or head.next == None:
        return

    front = head.next
    while front.next != None:
        front = front.next

    front.next = head.next # create a circle with list.len elements

def displayListWithCircle(head=None, limit=20):
    """
    display a list
    :param head: the head of the list
    :param limit: total nodes to display
    :return: True:circle exists / False:circle not exists
    """
    if head == None or head.next == None:
        print('empty list')
        return

    subNode = head.next
    i = 0

    while subNode != None and i < limit:
        print(subNode.data, end=' ')
        subNode = subNode.next
        i = i + 1

    print('\n')

def detectCircle(head):
    """
    if circle exits, return the enter node  of the circle
    :param head:
    :return:
    """
    if head == None or head.next == None:
        return

    faster = head.next
    slower = head.next
    meetPoint = None
    while faster.next != None and faster.next.next != None:
        faster = faster.next.next
        slower = slower.next
        if(faster == slower):
            meetPoint = faster # two pointer meet, so circle exists
            break

    if meetPoint == None:
        return Node()

    front = meetPoint
    behind = head.next

    while front != behind:
        front = front.next
        behind = behind.next
    return front

head = initList([1, 2, 3, 4, 5])
displayListWithCircle(head)
print('data of circle beginning node: ', detectCircle(head).data)

creatCircle(head)

displayListWithCircle(head)
print('data of circle beginning node: ', detectCircle(head).data)