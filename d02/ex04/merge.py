# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    merge.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/31 11:09:24 by ispirido          #+#    #+#              #
#    Updated: 2018/07/31 14:42:40 by ispirido         ###   ########.fr        #
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

    def merge(train1, train2):
        out = LinkedList()
        while train1 and train2:
            if train1.content > train2.content:
                out.add_tail(out.head, train1.content)
                train1 = train1.next
            else:
                out.add_tail(out.head, train2.content)
                train2 = train2.next
        while train1 or train2:
            if train1:
                out.add_tail(out.head, train1.content)
                train1 = train.next
            else:
                out.add_tail(out.head, train2.content)
                train2 = train2.next
        return out.head
