# 链表操作：交换两两相邻节点
# 交换节点需要同时对三个节点进行操作
#A--B--C--D
# 遍历不需要虚拟节点

# 定义节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 交换节点---同时对三个节点操作---加入虚拟节点
class Solution:
    def exchangeNodes(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(next=head)
        current = dummy_head
        # 遍历条件：三个节点都存在，又由于虚拟不用看
        while current.next and current.next.next:
            # 开始交换 ---比原版更容易区分
            tp1 = current.next #存A
            tp2 = current.next.next # 存B
            tp3 = current.next.next.next #存C
            current.next = tp2 # cur 指向B
            current.next.next = tp1 # B指向A
            #上面已经修改为B实际上是B.next = A
            current.next.next.next = tp3 #A指向C
            #没有更新current！！！！
            current = current.next.next # 更新位置这里不可写tp2！！！！！！
        return dummy_head.next
    #有虚拟节点返回虚拟 无虚拟返回head
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
head = node1
print("原始链表为：")
while head:
    print(head.val,end="->")
    head = head.next
print("none")

head = node1
S1 = Solution() #定义对象要加括号 定义类不加括号加冒号
head = S1.exchangeNodes(head)
print("修改链表为：")
while head:
    print(head.val,end="->")
    head = head.next
print("none")

#递归算法 ----不用写while循环
class Solution2:
    def swapPairs(self, head) :
        if head is None or head.next is None:
            return head
        # 待翻转的两个node分别是pre和cur
        pre = head
        cur = head.next
        next = head.next.next
        cur.next = pre  # 交换B--A
        pre.next = self.swapPairs(next)   # A接C
        # 将以next为head的后续链表两两交换
        return cur 
