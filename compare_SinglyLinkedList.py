#!/bin/python3

import os
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def compare_lists(llist1, llist2):
    ll1 = SinglyLinkedList()
    ll2 = SinglyLinkedList()
    ll1.head = llist1
    ll2.head = llist2

    list1 = []
    itr1 = ll1.head
    while itr1:
        list1.append(itr1.data)
        itr1 = itr1.next

    list2 = []
    itr2 = ll2.head
    while itr2:
        list2.append(itr2.data)
        itr2 = itr2.next

    len_list1 = len(list1)
    len_list2 = len(list2)

    equal = 1
    if(len_list1 == len_list2):
        for i in range(len_list1):
            if not list1[i] == list2[i]:
                equal = 0
    else:
        equal = 0

    return equal


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()
