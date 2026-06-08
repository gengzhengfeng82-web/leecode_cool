# 在这里实现链表的一个力扣复盘
from encodings.punycode import selective_find
from operator import length_hint


class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


# 203_移除节点元素==val的节点------移除元素用虚拟节点---且移除B必须知道A和C
class ListNode203:
    def deleteNode(self,head,val):
        dummy_head = ListNode(next=head)
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next # 更新位置
            else:
                current = current.next # 思考为何放在else里面
        return dummy_head.next
# 19_删除倒数第n个节点
#思路1--先获取链表全部长度，然后找到对应的三个位置直接删除(采用虚拟头节点）
class ListNode19:
    def length(self,head):
        length = 0
        while head:
            length +=1
            head = head.next
        return length
    def deleteNode(self,head,tar):
        dummy_head = ListNode(next=head)
        current = dummy_head
        length = self.length(head)
        len = length -tar #这里容易错
        while len:
            current = current.next
            len-=1
        current.next = current.next.next
        return dummy_head.next
#思路2--直接双指针法：快指针和慢指针之前存在一定的位置关系--加虚拟节点
#快指针先走n+1步，慢指针再走。这样当fast走到null，慢指针刚好走到目标前一个位置
#要求：可以根据这样的一句话提迅速写出代码
class  ListNode19_2:
    def deleteNode(self,head,tar):
        dummy_head = ListNode(next=head)
        fast = dummy_head
        slow = dummy_head
        n = tar+1
# 到这里均为模板
        while n:
            fast = fast.next
            n -=1
        current = fast #遍历统一current
        while current:
            current = current.next
            slow = slow.next
        slow.next = slow.next.next # 删除节点
        return dummy_head.next

# 24交换相邻节点--虚拟节点加标准步骤A--B--C
#这里避免none.next 以及none.val出现
#采用虚拟节点 虚拟-B,在B--A,最后A--C

class ListNode206:
    def reverseNode(self,head):
        dummy_head = ListNode(next=head)
        current = dummy_head
        while current.next and current.next.next:#不判断虚拟节点，故为current.next但是由于又要指向第三个存在
            #存值
            tp1 = current.next
            tp2 = current.next.next
            tp3 = current.next.next.next
            current.next = tp2 #cur指向B
            current.next.next = tp1#B指向A
            current.next.next.next = tp3 #A指向C
        return dummy_head.next

# 206反转链表---标准模板直接背4步
class ListNode206:
    def reverseNode(self,head):
        current = head
        prev = None
        while current:
            tp1 = current.next #存B
            current.next = prev #反转
            prev = current #赋值A
            current = tp1  #赋值B
        return prev

#142 环形链表---双指针法--不加虚拟节点
#步骤：fast每次走两步，slow每次走一步 当fast = slow的时候，找到环形
# 找到环起点，slow=head 然后fast不变继续走，都是一步当相遇时候slow即为起始点
#开始写
class ListNode142:
    def circleNode(self,head):
        fast = head
        slow = head
        while fast:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:  # 节点相等，找的是内存地址
                print("成功找到节点，现在开始寻找起始位置")
                slow = head
                while slow !=fast:
                    slow = slow.next
                    fast = fast.next
                return slow # 起点位置
#0207面试题  找到单链表相交节点的起始位置
# 获取两链表的长度然后让他们的末尾位置对齐，接下来从短的一方作为起始位置找相等节点
class ListNode0207:

    def length(self, head): #获取长度
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    def moveForward(self, head, steps):  #获取短链表的起始位置
        while steps > 0:
            head = head.next
            steps -= 1
        return head
    def inserectNode(self,head1,head2):
        len1 = self.length(head1)
        len2 = self.length(head2)
        if len1 > len2:
            head1 = self.moveForward(head1, len1-len2)
        else:
            head2 = self.moveForward(head2, len2-len1)
        while head1:
            if head1 == head2:
                return head1
            else: #这里加不加else都对 由于上面直接返回
                head1 = head1.next
                head2 = head2.next
        return 0











