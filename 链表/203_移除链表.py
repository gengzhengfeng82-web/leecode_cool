# 题意：删除链表中等于给定值 val 的所有节点。
# 示例 1： 输入：head = [1,2,6,3,4,5,6], val = 6 输出：[1,2,3,4,5]
# 示例 2： 输入：head = [], val = 1 输出：[]
# 示例 3： 输入：head = [7,7,7,7], val = 7 输出：[]
from email.feedparser import headerRE


# 节点定义---单链表
class ListNodeSignle:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next #一个节点对应一个数据一个指针
# 节点定义---双链表
class ListNodeDouble:
    def __init__(self,val=0,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next #一个节点对应两个指针，一个数据
# 单链表---虚拟节点---去除元素
# A--B--C 去除B
class S1ListNode:
    def replace1(self,head,val): #输入链表和目标值
        dummy_head = ListNodeSignle(0,next=head) # 定义虚拟头节点 指针指向头节点
        current = dummy_head #定义节点开始遍历
        while current.next:
            if current.next.val == val:# 找到current=A，next=B
                current.next = current.next.next # 让A指向C
            else:
                current = current.next
        print(head.val) # 此时经过current遍历 head不变（右侧赋值），
        #打印head为节点，对应python为对象  显示类名和内存地址
        # 因此返回链表写head 相当于没有变！！！
        return dummy_head.next  #这一步返回更新以后的链表
# 定义节点：
nodeA = ListNodeSignle(1)
nodeB = ListNodeSignle(2)
nodeC = ListNodeSignle(3)
nodeD = ListNodeSignle(4)
nodeE = ListNodeSignle(5)

#指针指向节点，连接起来就变链表：
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = None
# nodeE.next = nodeA 加这一步就变成循环链表
head = nodeA #定义单链表
print("初始链表为：",end="")
while head:
    print(head.val, end='->')
    head = head.next
# 这里我已经遍历完了head，在传参数的时候head已经指向none了所以=要改
print("none")
head = nodeA
print("********************************")


S1 = S1ListNode() # 定义对象
head = S1.replace1(head,3)
print("移除元素以后的链表为：",end="")
while head:
    print(head.val, end='->')
    head = head.next
print("none")


# 采用原始链表删除
class S2ListNode:
    def replace2(self,head,val):
        while head and head.val == val: # 防止none.val出现
            head = head.next #写if的话只会判断一次
        current = head #中间节点开始遍历
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head#这里直接修改原链表