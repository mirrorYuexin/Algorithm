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
    :param data: a sequence of data belong to nodes in the list
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

