class node:
    def __new__(cls, x):
        return object.__new__(cls)

    def __init__(self, x):
        self.data = x
        self.next = None


def initList():
    head = node(None)
    temp = head
    for i in range(1, 8):
        subNode = node(i)
        temp.next = subNode
        temp = subNode
    temp.next = None
    return head


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


def printList(head):
    if head == None or head.next == None:
        print('null')
        return
    temp = head
    while (temp.next != None):
        temp = temp.next
        print(temp.data, end=' ')


if __name__ == '__main__':
    head = initList()
    print('before reverse:')
    printList(head)

    # head = reverse(head)
    head = reverseV4(head)
    print('\nafter reverse:')
    printList(head)
