#一般哈希表都是用来快速判断一个元素是否出现集合里。
# 给定一个整数数组 nums 和一个目标值 target，
# 请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标
# 我们不仅要知道元素有没有遍历过，还要知道这个元素对应的下标，
# 需要使用 key value结构来存放，key来存元素，value来存下标，那么使用map正合适。
# map在python里面对应的正好是字典
class HashTable:
    def two_Sum(self,nums,target):
        records= dict()#用字典来存储
        for index, value in enumerate(nums):  # 枚举类型得到索引加元素
            if target - value in records:  # 遍历当前元素，并在map中寻找是否有匹配的key
                return [records[target - value], index]  # 字典通过键名来访问
            records[value] = index  # 如果没找到匹配对，就把访问过的元素和下标加入到map中
        return []
# 需要返回下标。因此让值等于下标
    # 第一次遍历2  record为空，则就是record={2:0}
    # 第二次遍历3  得到record{3:1，2:0}
    # 第三次遍历4    7-4=3  找到返（1，2）
S1 = HashTable()
print(S1.two_Sum([2, 3, 4, 15], 7))