# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        self.mid=self.middle(head)
        midnext=self.mid.next
        head2=self.reverse(midnext)
        head1=head
        return self.check(head1,head2)
        
    def middle(self,head):
        slow=head
        fast=head
        while fast.next !=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow

    def reverse(self,head):
        prev=None
        curr=head
        while curr!=None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            
        return prev
     
        
    def check(self,head1,head2):
       
        while head2!=None:
            if head1.val!=head2.val:
                return False
            head1=head1.next
            head2=head2.next
        
        return True
            
