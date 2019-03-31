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

def findKthEleFromTheBottom(head=None,k=0):
    """
    find the kth element from a bottom from a list
    :param head: list head
    :param k: position
    :return: node
    """
    if head == None or head.next == None:
        return Node()

    if k <= 0:
        return Node()

    front = head.next
    behind = head.next#k steps behind pointer front

    for i in range(k-1):
        if front.next != None:
            front = front.next
        else:
            print('wrong k!')
            return Node()

    while front.next != None:
        front = front.next
        behind = behind.next

    return behind

if __name__ == '__main__':
    head = initList([1, 2, 3, 4, 5, 6])
    print(findKthEleFromTheBottom(head, 3).data)