# -*- coding: utf-8 -*-
class Node(object):
    """节点"""
    def __init__(self, elemt):
        self.next = None
        self.elemt = elemt

class Single_link_list(object):
    """单链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur!= None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历"""
        cur = self.__head
        while cur != None:
            print(cur.elemt, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """头部添加元素"""
        node = Node(item)
        # 先让新节点指向链表 再让head指向新节点 不然指向会丢失
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """尾部添加元素"""
        # 创建一个新节点
        node = Node(item)
        if self.is_empty():
            # 如果为空链表 则直接指向新节点
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            # 最后一个节点指向新节点
            cur.next = node

    def insert(self, pos, item):
        """指定位置插入元素"""
        # pos小于0处理为头部添加
        if pos <= 0:
            self.add(item)
        #pos大于链表长度处理为尾部添加
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count != (pos-1):
                count += 1
                cur = cur.next
            # 循环结束后cur指向pos-1位置
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elemt == item:
                # 判断此节点是否是头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                # 必须先移动pre游标
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找元素是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elemt == item:
                return True
            else:
                cur = cur.next
        return False

def main():
    li = Single_link_list()
    print(li.is_empty())
    li.add(1)
    li.append(2)
    li.append(3)
    li.append(4)
    li.insert(1,1.5)
    li.insert(0,-1)
    li.insert(10,999)
    li.insert(10,999)
    li.remove(999)
    li.travel()
    print(li.is_empty())
    len = li.length()
    print('length:%d'% len)

if __name__ == '__main__':
    main()