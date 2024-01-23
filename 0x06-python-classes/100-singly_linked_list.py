#!/usr/bin/python3
"""
This module contains two classes that implements singly-linked-list data
structure.
"""


class Node:

    """"
    This class implements a node of a linked list.
    Args:
        data(int): data to insert to node.
        next_node (Node or none): pointer to next node
    """

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """this fuction retrieves the data from node instance.its setter
        must make sure the data to be assgined to this node if of only
        int type.
        Returns:
                node's data(int) always.
        """
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """
        THis propety retrieves pointer to next node of Node class instance.
        It's property's setter assignes pointer to next
        node to private attr __next_node.
        Returns:
                address of next node object
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class is responsible for combining nodes into a linked list sorted
    in increasing order in reference to value enter in sorted_insert method.
    """

    def __init__(self):
        self.__head = None

    def __str__(self):
        res = ""
        if not self.__head:
            return ret
        head = self.__head
        while (head.next_node):
            res += format(head.data, 'd')
            res += '\n'
            head = head.next_node
        res += format(head.data, 'd')
        return res

    def sorted_insert(self, value):
        """
        This method inserts node to existing linked list in increasing
        order in accordance with value's of the nodes.If no linked list exists
        it creates  new linked list with the new node created with value.
        args:
            value (int): data to be stored to linked list node.
        """
        new_node = Node(value)
        tmp = self.__head
        if not self.__head:
            self.__head = Node(value)
            return
        else:
            if value < self.__head.data:
                new_node.next_node = self.__head
                self.__head = new_node
                return
            while (tmp.next_node):
                if (value < tmp.next_node.data):
                    new_node.next_node = tmp.next_node
                    tmp.next_node = new_node
                    return
                tmp = tmp.next_node
            tmp.next_node = new_node
