class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper to check if there are at least k nodes remaining
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        
        if count < k:
            return head
        
        # Reverse the first k nodes
        prev = None
        curr = head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # Recursively reverse the remaining linked list and connect
        head.next = self.reverseKGroup(curr, k)
        
        return prev