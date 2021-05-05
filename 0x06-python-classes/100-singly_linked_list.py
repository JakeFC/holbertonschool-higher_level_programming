#!/usr/bin/python3
"""Module that defines classes SinglyLinkedList and Node"""


class Node:
    """A member of a singly linked list defined by:
    instance attributes: __data - int value stored
                         __next_node - pointer to next node
    """
    def __init__(self, data, next_node=None):
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError('data must be an integer')
        if next_node is None or isinstance(next_node, Node):
            self.__next_node = next_node
        else:
            raise TypeError('next_node must be a Node object')

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        self.__init__(value)

    @next_node.setter
    def next_node(self, value):
        self.__init__(self.__data, value)


class SinglyLinkedList:
    """A class defined by:
    instance attribute: __head - pointer to first Node in list
    instance method: sorted_insert(self, value) - inserts a new Node into
    correct sorted position in the list (increasing order)
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value, None)
        elif self.__head.data > value:
            self.__head = Node(value, self.__head)
        else:
            tmp = self.__head
            while tmp.next_node:
                if value <= tmp.next_node.data:
                    tmp.next_node = Node(value, tmp.next_node)
                    break
                tmp = tmp.next_node
            else:
                tmp.next_node = Node(value, None)
            del tmp

    def __repr__(self):
        l = ""
        tmp = self.__head
        while tmp:
            l += str(tmp.data) + '\n'
            tmp = tmp.next_node
        del tmp
        return l[:len(l) - 1]
