def Reverse(head):

    prev_node = None
    next_node = head
    
    while next_node:
        copy_prev_node = prev_node
        copy_next_next_node = next_node.next
        
        prev_node = next_node
        next_node.next = copy_prev_node
        next_node = copy_next_next_node
    
    head = prev_node
    return head

    if (( head == None ) or ( head.next == None )):
        return head

    current_node = head.next
    prev_node = head
    next_node = head.next.next

    current_node.next = prev_node
    prev_node.next = None
    