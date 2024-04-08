# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head):
    
    previous = None
    current = head
    nextt = None
    while(current != None):
        nextt = current.next
        current.next = previous
        previous = current
        current = nextt
    return previous


# Solution
# Consider a 1 element linked list. [1, None]. 1->Null
# This is already reversed. Therefore this is the base case. If head->next is None, LL is reversed.
# Consider a 3 element linked list. [1, [2, [3, None]]]. 1->2->3->Null
# Here if out goal is: Null<-1<-2<-3
# So we start by assigning head->next to Null. But if we do that we will lose access to 2 and rest of LL.
# So we introduce a value called previous which is initially None.
# we need to do the following:
# 1->previous current->2->3. Current to make sure we dont lose the link to the rest of LL/
# We need to introduce a temporary variable that will store the temporary link to the next of current. 
# This is requried because current is going to be assigned to previous link. basically like swapping element.
# Temp  = swap_a. swap_a = swap_b. swap_b = temp 

# So the logic is.
# Temp = current.next 
# current.next = previous
# previous = current
# current = Temp