# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sort_asc.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/31 14:57:02 by ispirido          #+#    #+#              #
#    Updated: 2018/07/31 15:25:26 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from node import Node

class LinkedList(object):
    def __init__(self):
        self.h = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    @property
    def head(self):
        return self.h

    @head.setter
    def head(self, val):
        self.h = val

    def isEmpty(self):
        return self.head == None

    def add_head(self, node):
        if self.isEmpty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
   
    def print_list(self, list_head):
        if list_head:
            print(list_head.content)
            if list_head.next:
                self.print_list(list_head.next)

    def add_tail(self, list_head, val):
        if list_head is None:
            self.add_head(Node(val))
        else:
            while list_head.next:
                list_head = list_head.next
                list_head.next = Node(val)

    def sort_asc(self):
        lst = sorted([node.content for node in self], reverse=True)
        self.h = None
        for data in lst:
            self.add_tail(self.h, data)
