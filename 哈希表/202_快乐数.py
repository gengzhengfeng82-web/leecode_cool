# 快乐数定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果可以变为1，那么这个数就是快乐数。
class HashTable202:
    def ishappy(self,val):
        record = [] #存储每一次结果
        while n not in record: #判断n是否在结果里面
            record.append(n)
            new_num = 0
            temp = n
            #  计算各个位置平方和
            while temp:  # 用 divmod 逐位取
                temp, r = divmod(temp, 10)  # r 就是个位数字
# #temp 的作用是保护 n 不被破坏。
#内层循环会把 temp 一步步除到 0，如果直接用 n，n 就被改成了 0，外层循环的逻辑就全乱了
                new_num += r ** 2  # 放进去while正好选出来每个位置平方和
            if new_num == 1:
                return True
            else:
                n = new_num
        return record
class HashTable202_2:
    def ishappy(self,n):
        record = []
        while True:
            n = self.get_sum(n) #得到每一次的求和
            if n not in record:
                record.append(n)
            elif n ==1:
                print("是快乐数",record)
                return True
            else:
                print("不是快乐数", record)
                return False
    def get_sum(self,n):
        sum = 0
        while n:
            n,r = divmod(n,10)
            sum += r ** 2
        return sum
val = 102
S1 = HashTable202_2()
S1.ishappy(val)