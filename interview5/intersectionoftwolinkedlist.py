# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #assigning the len of a and b as 0 respectively
        lenA=0
        lenB=0
        
        #assigning the headA and headB values to pointers as we dont want to lose the head 
        pa=headA
        pb=headB
        
        #check until the head pointer is equal
        while pa!=None :
            #incrementing the lenght value by one
            lenA+=1
            #move the pointer one by one
            pa=pa.next
        #to find out the length of linked list
        while pb!=None:
            lenB+=1
            #incrementing the length by one and also  pointer to next
            pb=pb.next
            
        #assigning the head pointers to the variable 
        pa=headA
        pb=headB
        
        #ubtil the pointers are length are same move the pointer of large list
        while lenA>lenB:
            pa=pa.next
            #decrement the pointer value by one
            lenA-=1
        while lenB>lenA:
            #decrement the pointer by ine and also move the pointer b to next pointers4r
            pb=pb.next
            lenB-=1
            
        while pa!=pb:
            pa=pa.next
            pb=pb.next
        return pb
                