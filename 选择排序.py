# -*- coding: utf-8 -*-
def select_sort(item):
    """
    选择排序:
        最优时间复杂度: O(n²)
        最坏时间复杂度: O(n²)
        稳定性: 不稳定

    """
    n = len(item)
    for j in range(n-1):
        # 设置最小元素下标
        min_index = j
        for i in range(j+1, n):
            # 遍历取得最小元素下标
            if item[min_index] > item[i]:
                # 当前最小元素下标
                min_index = i
        # 小的放前面
        item[j], item[min_index] = item[min_index], item[j]

if __name__ == '__main__':
    li = [22, 58, 17, 5, 20, 9, 89, 66]
    print(li)
    select_sort(li)
    print(li)