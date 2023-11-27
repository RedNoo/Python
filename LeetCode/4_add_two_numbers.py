class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def list_to_linked_list(self,lst):
        head = None
        current = None

        for item in lst:
            new_node = ListNode(item)
            if head is None:
                head = new_node
                current = head
            else:
                current.next = new_node
                current = new_node

        return head  # Bağlı listenin başını döndür

    def addTwoNumbers(self, ll1, ll2) :

        l1 = []
        l2 = []

        while ll1 is not None:
            l1.append(ll1.val)
            ll1 = ll1.next

        while ll2 is not None:
            l2.append(ll2.val)
            ll2 = ll2.next


        result = []

        l1Count = len(l1)
        l2Count = len(l2)

        if l1Count > l2Count:
            for i in range(l1Count - l2Count):
                l2.append(0)
        elif l2Count > l1Count:
            for i in range(l2Count - l1Count):
                l1.append(0)

        tempVal = 0

        for i in range(len(l1)):
            val = l1[i] + l2[i]

            if (val + tempVal) >= 10:
                result.append(tempVal + (val - 10))
                tempVal = 1
            else:
                result.append(val + tempVal)
                tempVal = 0

        if tempVal > 0:
            result.append(tempVal)

        return self.list_to_linked_list(result)







node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)

node4.next = node5
node5.next = node6




s = Solution()
print(s.addTwoNumbers(node1, node4))
