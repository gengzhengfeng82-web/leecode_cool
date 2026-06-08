# 反转链表
# 定义节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 本质是双指针！！！！
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        prevent = None
        while current:
            temp = current.next #存B
            current.next = prevent #让current指向prev 反转！！！！！！
            prevent = current # prev 指向A
            current = temp #当前指向    B
            # 更新prev 和current这步不可互换！！！！
        return prevent #！！！容易错
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
head = node1 # 定义链表
s1 = Solution()
print("初始链表：",end="")
while head:#可以思考为什么这写head就可以 就会明白反转的遍历条件
    print(head.val, end=" -> ")
    head = head.next
print("none")
head = node1#还原回去
print()
print("反转链表：",end="")
prev = s1.reverseList(head)
while prev:
    print(prev.val, end=" -> ")
    prev = prev.next
print("none")


class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head, None)
    def reverse(self, cur: ListNode, pre: ListNode) -> ListNode:
        if cur == None:
            return pre
        temp = cur.next
        cur.next = pre #反转
        return self.reverse(temp, cur)