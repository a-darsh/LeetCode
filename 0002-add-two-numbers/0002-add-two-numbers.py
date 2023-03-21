# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       
        num1 = 0
        num2 = 0
        
        i = 0
        while (l1 != None):
          num1 += pow(10,i)*l1.val
          l1 = l1.next
          i += 1
          
        i = 0
        while (l2 != None):
          num2 += pow(10,i)*l2.val
          l2 = l2.next
          i+=1
          
        sum = num1 + num2
      
        first_node = ListNode(val = sum%10)
        temp_prev = first_node
        sum = sum//10
        
        while(sum !=0):
          temp = ListNode(val = sum%10)
          temp_prev.next = temp
          sum = sum//10
          temp_prev = temp
        
        return first_node
         