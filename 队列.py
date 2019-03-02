# -*- coding: utf-8 -*-
class Queue(object):
    """队列"""
    def __init__(self):
        self.__list = []

    def is_empty(self):
        """判断是否为空队列"""
        return self.__list ==[]

    def size(self):
        """返回队列的大小"""
        return len(self.__list)

    def enqueue(self, item):
        """添加元素"""
        self.__list.append(item)
        # self.__list.insert(0, item)

    def dequeue(self):
        """头部删除一个元素"""
        return self.__list.pop(0)
        # self.__list.pop()

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.size(), q.is_empty())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.size(), q.is_empty())
