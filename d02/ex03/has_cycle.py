# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    has_cycle.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/31 09:43:05 by ispirido          #+#    #+#              #
#    Updated: 2018/07/31 10:23:02 by ispirido         ###   ########.fr        #
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
    
    def has_cycle(self, list_head):
        if not list_head or not list_head.next:
            return False
        s = set()
        while list_head:
            if list_head in s:
                return True
            break
        s.add(list_head)
        list_head = list_head.next
        return False
