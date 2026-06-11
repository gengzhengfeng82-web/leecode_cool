#计算交集首先想集合
class HashTable349:
    def inesrectElements(self,set1,set2):
        return list(set1 & set2)
# 集合是可以自动去重的，故直接定义的时候就已经完成去重操作
#一些使用详解
# 1- in 和 in not运算符适用于python所有数据结构，即可用于判断元素是否在里面，又可以用于for i in s
# 2- & | 取并集和取交集一般只适用于set

#  采用数组操作
from numpy import *
class HashTable349_2:
    def inesrectElements(self,arr1,arr2):
        # 第一步：哈希映射 --映射是先对应位置然后再变化
        result = []
        count1 = zeros(1000)
        count2 = zeros(1000)
        for i in arr1:
            count1[i] +=1 # 下标本身从0开始，这里找到元素则对应加
        for i in arr2:
            count2[i] +=1
        for i in range(len(arr1)):
            if count1[i] * count2[i] !=0:
                result.append(i) # 这里就实现了找到元素
        return result
ht1 = HashTable349()
set1 = {1, 2, 2, 3, 4}
set2 = {2, 3, 3, 5}
print(ht1.inesrectElements(set1, set2))  # [2, 3]

# 法2：数组/哈希映射方式
ht2 = HashTable349_2()
arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 3, 3, 5]
print(ht2.inesrectElements(arr1, arr2))  # [2, 3]