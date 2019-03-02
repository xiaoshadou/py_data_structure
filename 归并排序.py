# -*- coding: utf-8 -*-
def merge_sort(item):
    """
    归并排序:
        最优时间复杂度: O(nlogn)
        最坏时间复杂度: O(nlogn)
        稳定性: 稳定
    """
    n = len(item)
    if n <= 1:
        return item
    mid = n // 2
    # left 采用归并排序后形成的有序的新序列
    left_list = merge_sort(item[:mid])
    # right 采用归并排序后形成的有序的新序列
    right_list = merge_sort(item[mid:])
    # 将两个序列合并成一个整体 两指针辅助比较元素大小
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_list) and right_pointer < len(right_list):
        # 两边元素作比较 小的放前面添加进新的列表
        if left_list[left_pointer] <= right_list[right_pointer]:
            result.append(left_list[left_pointer])
            # 移动指针
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1
    # 循环退出后添加剩下的一个元素
    result += left_list[left_pointer:]
    result += right_list[right_pointer:]
    return result

if __name__ == '__main__':
        li = [22, 58, 17, 5, 20, 9, 89, 66]
        print(li)
        print(merge_sort(li))