class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def deleteDuplicates(head):
    if(head == None):
        return None
        
    porerta = head.next
    cur = head

    while(porerta != None):
        if(head.val == porerta.val):
            porerta = porerta.next
            head.next = porerta

        else:
            head = head.next
            porerta = porerta.next
    return cur


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)

new_head = deleteDuplicates(head)
#head = deleteDuplicates*head.next 

while new_head is not None:
    print(new_head.val)
    new_head = new_head.next
