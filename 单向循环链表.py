# -*- coding: utf-8 -*-
class Node(object):
    """节点"""
    def __init__(self, elemt):
        self.next = None
        self.elemt = elemt

class Single_cycle_link_list(object):
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elemt, end=" ")
            cur = cur.next
        # 退出循环cur指向尾节点 但尾节点的元素未打印 所以要打印
        print(cur.elemt)

    def add(self, item):
        """头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环 cur指向尾节点
            # 此时添加新节点
            node.next = self.__head
            self.__head = node
            cur.next = self.__head

    def append(self, item):
        """尾部添加元素"""
        # 创建一个新节点
        node = Node(item)
        if self.is_empty():
            # 如果为空链表 则直接指向新节点
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 最后一个节点指向新节点
            cur.next = node
            # 指向头节点
            node.next = self.__head

    def insert(self, index, item):
        """指定位置插入元素"""
        # pos小于0处理为头部添加
        if index <= 0:
            self.add(item)
        #pos大于链表长度处理为尾部添加
        elif index > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count != (index-1):
                count += 1
                cur = cur.next
            # 循环结束后cur指向pos-1位置
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elemt == item:
                if cur == self.__head:
                    # 如果是头节点
                    # 找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    # 删除头节点
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间节点
                    pre.next = cur.next
                #break 改用return
                return
            else:
                # 必须先移动pre游标
                pre = cur
                cur = cur.next
        # 退出循环 cur指向尾节点
        if cur.elemt == item:
            if cur == self.__head:
                # 链表只有一个节点
                self.__head = None
            else:
                # pre.next = cur.next
                pre.next = self.__head

    def search(self, item):
        """查找元素是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elemt == item:
                return True
            else:
                cur = cur.next
        # 退出循环cur指向尾节点
        if cur.elemt == item:
            return True
        return False

def main():
    li = Single_cycle_link_list()
    li.add(1)
    li.append(2)
    li.remove(1)
    li.travel()
    print(li.length())
    print(li.search(3))

if __name__ == '__main__':
    main()