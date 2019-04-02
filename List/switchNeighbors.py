from List import baseOperation as BO #some base operation on list

def switchNeighbors(head):
    """
    switch two elements one pair by one pair
    :param head:
    :return:
    """
    if head == None or head.next == None or head.next.next == None:
        return

    rear = head
    mid = head.next
    pre = head.next.next

    while pre!= None:
        rear.next = pre
        mid.next = pre.next
        pre.next = mid
        temp = mid
        mid = pre
        pre = temp
        # go to the next pair of nodes
        if pre.next == None:
            return
        pre = pre.next.next
        mid = mid.next.next
        rear = rear.next.next

if __name__ == '__main__':

    head = BO.initList([1, 2, 3])
    BO.displayList(head)

    switchNeighbors(head)
    BO.displayList(head)