# -*- coding: utf-8 -*-
def shell_sort(item):
    """
    希尔排序:
        最优时间复杂度: 根据步长序列的不同而不同
        最坏时间复杂度: O(n²)
        稳定性: 不稳定

    """
    n = len(item)
    gap = n // 2
    # gap变化到0之前 插入算法执行的次数
    while gap > 0:
        for i in range(gap, n):
            while i > 0:
                if item[i] < item[i-gap]:
                    item[i], item[i-gap] = item[i-gap], item[i]
                    i -= gap
                else:
                    break
        # 缩短步长
        gap //= 2

if __name__ == '__main__':
        li = [22, 58, 17, 5, 20, 9, 89, 66]
        print(li)
        shell_sort(li)
        print(li)