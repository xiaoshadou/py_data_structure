# -*- coding: utf-8 -*-
def quick_sort(item, start, end):
    """
    快速排序:
        最优时间复杂度: O(nlogn)
        最坏时间复杂度: O(n²)
        稳定性: 不稳定

    """
    if start >= end:
        return
    mid_value = item[start]
    left = start
    right = end
    while left < right:
        while left < right and item[right] >= mid_value:
            right -= 1
        # 右边有比中间值小的换到左边
        item[left] = item[right]

        while left < right and item[left] < mid_value:
            left += 1
        # 左边有比中间值大的换到右边
        item[right] = item[left]

    # 退出循环 left==right
    item[left] = mid_value
    # 对left左边进行递归快速排序
    quick_sort(item, start, left-1)
    # 对left右边进行递归快速排序
    quick_sort(item, left+1, end)

if __name__ == '__main__':
        li = [22, 58, 17, 5, 20, 9, 89, 66]
        print(li)
        quick_sort(li, 0, len(li)-1)
        print(li)