# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    add_tail.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/06 12:32:26 by ispirido          #+#    #+#              #
#    Updated: 2018/07/06 14:31:56 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node: {self.value}"

def add_tail(list_head, val):
    current = list_head
    while current.next:
        current = current.next
    current.next = Node(val)

if __name__ == "__main__":
    alice = Node("Alice")
    bob = Node("Bob")
    alice.next = bob

    add_tail(alice, "Chad")

    current = alice
    while current:
        print(current.value)
        current = current.next

