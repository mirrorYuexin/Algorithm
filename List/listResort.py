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

def displayList(head=None):
    """
    display a list
    :param head: the head of the list
    :return: None
    """
    if head == None or head.next == None:
        print('empty list')
        return

    subNode = head.next

    while subNode != None:
        print(subNode.data, end=' ')
        subNode = subNode.next

    print('\n')

def resortList(head=None):
    """
    resort the list in form node1 -> node2 ->...-> nodeN
    to
    node1 -> nodeN -> node2 -> nodeN-1...
    :param head: head of the original list
    :return: None
    """
    if head == None or head.next == None or head.next.next == None or head.next.next.next is None:
        return

    # find the middle node of the list
    faster = head.next
    slower = head.next
    while faster.next != None and faster.next.next != None:
        faster = faster.next.next
        slower = slower.next
    lastHalfHead = slower.next
    slower.next = None

    #reverse the last half list
    pre = None
    cur = lastHalfHead
    next = lastHalfHead.next
    while next != None:
        cur.next = pre
        pre = cur
        cur = next
        next = next.next
    cur.next = pre
    lastHalfHead = cur

    #combine two lists one node for first half list by one node from last half list
    firstHalfHead = head.next
    resListHead = head
    while firstHalfHead != None and lastHalfHead != None:
        resListHead.next = firstHalfHead
        resListHead = firstHalfHead
        firstHalfHead = firstHalfHead.next

        resListHead.next = lastHalfHead
        resListHead = lastHalfHead
        lastHalfHead = lastHalfHead.next

    while firstHalfHead != None:
        resListHead.next = firstHalfHead
        resListHead = firstHalfHead
        firstHalfHead = firstHalfHead.next

    while lastHalfHead != None:
        resListHead.next = lastHalfHead
        resListHead = lastHalfHead
        lastHalfHead = lastHalfHead.next

    resListHead.next = None


if __name__ == '__main__':
    # head = initList(['>', '$', '<', '@', '&']) # char is ok
    head = initList([1, 2, 3, 4, 5])
    resortList(head)
    displayList(head)