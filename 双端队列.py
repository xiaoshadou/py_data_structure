# -*- coding: utf-8 -*-
class Deque(object):
    """队列"""
    def __init__(self):
        self.__list = []

    def is_empty(self):
        """判断是否为空队列"""
        return self.__list ==[]

    def size(self):
        """返回队列的大小"""
        return len(self.__list)

    def add_front(self, item):
        """头部添加元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """尾部添加元素"""
        self.__list.append(item)

    def pop_front(self):
        """头部删除一个元素"""
        return self.__list.pop(0)

    def pop_rear(self):
        """尾部删除一个元素"""
        return self.__list.pop()

if __name__ == '__main__':
    q = Deque()
    q.add_front(1)
    q.add_front(2)
    q.add_rear(3)
    q.add_rear(4)
    # 2 1 3 4
    print(q.size(), q.is_empty())
    print(q.pop_front())
    print(q.pop_front())
    print(q.pop_rear())
    print(q.pop_rear())
    print(q.size(), q.is_empty())
