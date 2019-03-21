# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    add_tail.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/06 12:32:26 by ispirido          #+#    #+#              #
#    Updated: 2018/07/06 13:11:06 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = linked_list.head
        while node:
            yield node
            node = node.next

    def add_tail(self, node):
        if self.head:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node

linked_list = SinglyLinkedList()
linked_list.add_tail(Node('Alice'))
linked_list.add_tail(Node('Chad'))
linked_list.add_tail(Node('Debra'))

print ([node.value for node in linked_list])
