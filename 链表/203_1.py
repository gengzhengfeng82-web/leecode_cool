# 题意：删除链表中等于给定值 val 的所有节点。
# 示例 1： 输入：head = [1,2,6,3,4,5,6], val = 6 输出：[1,2,3,4,5]
# 示例 2： 输入：head = [], val = 1 输出：[]
# 示例 3： 输入：head = [7,7,7,7], val = 7 输出：[]


# 定义节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 移除元素--法1: 虚拟节点
class Solution1:
    def reverseElements(self, head: ListNode,val) -> ListNode:
        dummy_head = ListNode(next=head) # 注意函数的调用写法
        current = dummy_head #当前指针
        while current.next:#这里虚拟节点不需要判别
            if current.next.val == val:
                current.next = current.next.next # 直接让A指向C即可 指针指向节点
            else:
                current = current.next  # 更新位置 这里必须明确为什么加else！！
        return dummy_head.next # 再次注意，这里没有修改原始head，只是修改加了虚拟节点以后的链表，因此返回dummy_head.next
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4 # 这里定义时候默认为none所以不用管
head = node1 #定义链表成功！！！直接采用头节点
print("原始链表为：")
while   head:  # 这里为head原因：1-没有虚拟节点 2-没有none.val none.next出现
    print(head.val, end="->")
    head = head.next
print("none")
head = node1 # 遍历完成还原回去
S1 = Solution1()
head = S1.reverseElements(head,val=3)
print("修改链表为：")
while   head:  # 这里为head原因：1-没有虚拟节点 2-没有none.val none.next出现
    print(head.val, end="->")
    head = head.next
print("none")


#法2：原始链表移除
# 单链表删除节点需要修改前节点的next指针，但头节点没有前驱。  需要单独判断
class Solution2:
    def reverseElement(self, head: ListNode, val: int) -> ListNode:
        # 判断头节点，一定注意是否存在none.val none.next出现
        while head and head.val == val:  #这里顺序不可变！！不然出现none.val
            head = head.next  #写if的话只会判断一次
        current = head  # 定义当前位置
        while current and current.next: #和虚拟节点类似
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head #这里直接修改原链表