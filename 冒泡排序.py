# -*- coding: utf-8 -*-
def bubble_sort(item):
    """
    冒泡排序：
        最优时间复杂度: O(n)
        z最坏时间复杂度: O(n²)
        稳定性: 稳定

    """
    n = len(item)
    for j in range(n-1):
        count = 0
        for i in range(n-1-j):
            # 从头走到尾
            if item[i] > item[i+1]:
                item[i], item[i+1] = item[i+1], item[i]
                count += 1
        # 代表从来没有交换过
        if count == 0:
            return

if __name__ == '__main__':
    li = [22, 58, 17, 5, 20, 9, 89, 66]
    print(li)
    bubble_sort(li)
    print(li)
