# 二分查找
'''
首先，列表是升序排列，将要查找的数字与最中间的数字进行比较，如果相等，则返回，
否则，将列表以中间数字分为左右俩个列表，如果最中间的数字小于要查找的值，则在
右边列表查找，反之，在左边列表查找。一直循环，直到找个这个数字为止。或者，查询
不到此数字。

算法复杂度：O(log2 n)
算法要求：必须是顺序存储结构
          必须按关键字大小有序排列
'''
def binary_search(num_list,tar):
    low = 0
    high = len(num_list) - 1
    while low <= high:               # 对列表进行循环，知道查找到tar
        mid = int((low + high)/2)       # 中间数下标
        if num_list[mid] == tar :
            return mid
        elif num_list[mid] > tar:
            high = mid - 1
        else:
            low = mid + 1
    return -1                        #如果查找不到就返回-1

if __name__ == '__main__':
    num_list = [0,3,5,9,10]       # 所查找的列表（升序）
    tar = 10                                   # 要查找的值
    print(binary_search(num_list,tar))
