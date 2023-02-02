class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    new_head = None
    while (head != None):
        tmp = head.next
        head.next = new_head
        new_head = head
        head = tmp

    return new_head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4, None)


new_head = reverseList(head)

while new_head is not None:
    print(new_head.val)
    new_head = new_head.next