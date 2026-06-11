# 204——利用数组或者map实现字母异位词判断（个数和种类同）
from mmap import ALLOCATIONGRANULARITY

#数组
import numpy as np
class HashTable204_array:
    # 对于数组---第一步实现数组映射 ,第二步：实现相应的操作
    def isANA(self,arr1:str,arr2:str) -> str:
        results = np.zeros(26)#记录映射结果
        for i in arr1:
            results[ord(i)-ord('a')] +=1 #映射字符串1对应的数组
        for i in arr2:
            results[ord(i)-ord('a')] -=1 #映射字符串2对应的数组

        #展示1:只输出True False
#        return all(x==0 for x in results)
        #展示2：输出对应字母位置
        re = [] # 采用列表输出
        for idx,val in enumerate(results):
            if val != 0:
                re.append([chr(ord('a')+idx),val])
        return re
arr1 = 'asdfgh'
arr2 = 'qasdfg'
S1 = HashTable204_array()
print(S1.isANA(arr1,arr2))

class HashTable204_map:
    def isANA(self,arr1:str,arr2:str) -> str:
        result ={}# 定义字典
        # 开始字典映射--KEY存值，Value存下标(次数）
        for i in arr1:
            result[ord(i)-ord('a')] =result.get(ord(i)-ord('a'),0)+1
        for i in arr2:
            result[ord(i) - ord('a')] = result.get(ord(i) - ord('a'), 0) - 1
        return all(result[x] == 0 for x in result)
S12 = HashTable204_map()
print(S12.isANA(arr1,arr2))


##############################################################################################

#383_赎金信
# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，
# 判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。
# 如果可以构成，返回 true ；否则返回 false。

# 同样的数据量小的直接数组，map 数据大的set
class HashTable383_array:
    def isransom(self,ransom,magnize):
        result = np.zeros(26)
        for i in ransom: #数组映射
            result[ord(i)-ord('a')] +=1
        for i in magnize:
            result[ord(i)-ord('a')] -=1
        return all(x<=0 for x in result) #<=0说明magnize里面元素都是足够的
s = HashTable383_array()
ransomNote = "aabbccccc"
magazine = "aaaaaaabbbbbbccccccccdddd"
print(s.isransom(ransomNote, magazine))  # True

class HashTable383_map:
    def isransom(self,ransom,magnize):
        result = {}
        for i in ransom:
            result[i] = result.get(i,0)+1
        for i in magazine:
            result[i] = result.get(i,0)-1
        re = []
        for i in result:
            if result[i] > 0:# 元素不够
                re.append([chr(ord(i)),result[i]])  #result[i]]代表少几个
        return re
s = HashTable383_map()
ransomNote = "aabbcccccee"
magazine = "aaaaaaabbbbbbccccccccdddd"
print(s.isransom(ransomNote, magazine))

#################################################################################
#349 给定两数组计算他们的交集
#计算交集一般采用set和数组
class HashTable349_set:
    def inserectElements(self,num1,num2):
        return list(num1 & num2)


class HashTable349_array:
    def inserectElement(self,arr1,arr2):
        result = np.zeros(1000)
        for i in arr1: #数组映射
            result[i] +=1
        for i in arr2:
            result[i] +=1
        re = []
        for idx, val in enumerate(result):
            if val >1:
                re.append([idx,val])
        return re

ht1 = HashTable349_set()
set1 = {1, 2, 2, 3, 4}
set2 = {2, 3, 3, 5}
print(ht1.inserectElements(set1, set2))  # [2, 3]


ht2 = HashTable349_array()
arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 3, 3, 5]
arr1 = np.array(arr1, dtype=int)
arr2 = np.array(arr2, dtype=int)
print(ht2.inserectElement(arr1, arr2))  # [2, 3]





