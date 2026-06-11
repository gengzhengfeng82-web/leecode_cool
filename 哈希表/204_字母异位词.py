# 利用数组操作实现字母异位词判断（个数和种类同）

from numpy import *
class HashTable242:
    def isANA(self,arr1:str,arr2:str) -> array:
        # 第一步：哈希映射 --映射是先对应位置然后再变化
        result = zeros(26)
        re1=[]
        for i in  arr1:
            result[ord(i)-ord('a')] +=1 # 下标从零开始映射
        for i in arr2:
            result[ord(i)-ord('a')] -=1  #从0开始映射，一个加一个减
        #第二步：直接判断
        #for i in result: 只收集元素！！！
        for idx, val in enumerate(result):
            if idx != 0:
                re1.append((idx, val))
        return re1
arr1 = "asdfgh"
arr2 = "ahgfdqs"
S1 = HashTable242()
print(S1.isANA(arr1,arr2))
sa = S1.isANA(arr1,arr2)
if len(sa) == 0:
    print("为字母异位词")
else:
    print("不为字母异位词")
 #zeros(26) 生成的是 numpy 的 float64 数组，所以比较结果也是 numpy 类型。
 #len(sa) == 0 是检查列表里有没有元素  检查集合类数据结构（list、array 等）是否为空，一般用 len() 或者直接判断布尔值
 #sa == 0 比较的是整个列表和数字 0     == 0 通常用于比较具体的数值
