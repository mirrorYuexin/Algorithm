from List import baseOperation as BO #some base operation on list

def subSwitch(rear, pre, k):
    """
    recursively and dividually switch k nodes
    :param head:
    :return:
    """
    if k < 2:
        return pre

    if k == 2:
        mid = rear.next
        rear.next = pre
        mid.next = pre.next
        pre.next = mid
        return mid

    if k % 2 == 0:
        i = 1
        firstPre = rear.next
        while i < k / 2:
            i = i + 1
            firstPre = firstPre.next # the first half
        firstRear = rear

        firstPre = subSwitch(firstRear, firstPre, k/2)
        lastRear = firstPre
        lastPre = pre
        lastPre = subSwitch(lastRear, lastPre, k / 2)

        temp = firstRear.next
        rear.next = firstPre.next
        firstPre.next = lastPre.next
        lastPre.next = temp

        return firstPre

    if k % 2 == 1:
        i = 1
        firstPre = rear.next
        while i < (k / 2 - 1):
            i = i + 1
            firstPre = firstPre.next # the first half
        firstRear = rear
        lastPre = pre
        mid = firstPre.next
        lastRear = mid

        firstPre = subSwitch(firstRear, firstPre, (k-1) / 2)
        lastPre = subSwitch(lastRear, lastPre, (k-1) / 2)

        temp = rear.next
        rear.next = mid.next
        firstPre.next = lastPre.next
        lastPre.next = mid
        mid.next = temp

        return firstPre





def switchKNeighbors(head, k=2):
    """
    inner switch the k near by nodes
    :param head:
    :param k: length k
    :return:
    """
    if head == None or head.next == None:
        return

    rear = head
    pre = rear
    while pre.next != None:
        pre = rear.next
        i = 1
        while i < k and pre.next != None:
            i = i + 1
            pre = pre.next

        if i < k:
            pre = subSwitch(rear, pre, i)
        else:
            pre = subSwitch(rear, pre, k)
        rear = pre



if __name__ == '__main__':

    head = BO.initList([1, 2, 3, 4, 5, 6, 7, 8])
    BO.displayList(head)

    switchKNeighbors(head, 2)
    BO.displayList(head)