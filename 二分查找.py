# -*- coding: utf-8 -*-
def binary_search(list, item):
    """二分查找 递归"""
    n = len(list)
    if n > 0:
        mid = n // 2
        if list[mid] == item:
            return  True
        elif item < list[mid]:
            return binary_search(list[:mid], item)
        else:
            return binary_search(list[mid+1:], item)
    return False

def binary_search_2(list, item):
    """二分查找 非递归"""
    n = len(list)
    first = 0
    last = n - 1
    while first < last:
        mid = (first + last) // 2
        if list[mid] == item:
            return True
        elif item < list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False

if __name__ == '__main__':
        li = [5, 9, 17, 20, 22, 58, 66, 89]
        print(li)
        print(binary_search(li, 66))
        print(binary_search(li, 100))
        print(binary_search_2(li, 66))
        print(binary_search_2(li, 100))