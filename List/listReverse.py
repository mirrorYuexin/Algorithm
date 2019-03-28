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


def reverse(head):
    if head == None or head.next == None:
        return

    tempList = []
    subNode = head

    while (subNode.next != None):
        tempList.append(subNode.next)
        subNode = subNode.next

    for i in range(1, tempList.__len__())[::-1]:
        j = i - 1
        tempList[i].next = tempList[j]

    tempList[0].next = None
    head.next = tempList[tempList.__len__() - 1]
    return head


def reverseV2(head):
    if head == None or head.next == None:
        return

    subNode = head.next
    head.next = None

    while (subNode != None):
        temp = subNode
        subNode = subNode.next
        temp.next = head.next
        head.next = temp

    return head

def reverseV3(head):
    if head is None or head.next is None:
        return
    pre, rear = subReverseV3(head.next)
    head.next = pre
    return head

def subReverseV3(head):
    rear = head
    pre = head
    if head.next is not None:
        pre, rear = subReverseV3(head.next)
    rear.next = head
    head.next = None
    return pre, head

def reverseV4(head):
    if head is None or head.next is None:
        return
    pre = None
    cur = head.next
    next = cur.next

    while(cur.next is not None):
        cur.next = pre
        pre = cur
        cur = next
        next = next.next

    cur.next = pre
    head.next = cur
    return head



if __name__ == '__main__':
    head = initList([1, 2, 3, 4, 5, 6, 7])
    print('before reverse:')
    displayList(head)

    # head = reverse(head)
    head = reverseV4(head)
    print('after reverse:')
    displayList(head)
