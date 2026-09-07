class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper to check if there are at least k nodes remaining
        def get_kth_node(curr, k_val):
            while curr and k_val > 0:
                curr = curr.next
                k_val -= 1
            return curr

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the k-th node from the current group's start
            kth = get_kth_node(group_prev, k)
            if not kth:
                break
            
            group_next = kth.next

            # Reverse the k nodes
            prev = kth.next
            curr = group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Connect the reversed group back to the main list
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp

        return dummy.next