# -*- coding: utf-8 -*-
def insert_sort(item):
    """
    插入排序:
        最优时间复杂度: O(n)
        最坏时间复杂度: O(n²)
        稳定性: 稳定

    """
    n = len(item)
    # 从第二个位置即下标为1的元素开始向前插入
    for i in range(1, n):
        while i > 0:
            # 从第i个元素开始比较 小于前面个元素则交换位置
            if item[i] < item[i-1]:
                item[i], item[i-1] = item[i-1], item[i]
                i -= 1
            else:
                # 相等或大于则直接退出 避免重复比较
                break

if __name__ == '__main__':
        li = [22, 58, 17, 5, 20, 9, 89, 66]
        print(li)
        insert_sort(li)
        print(li)