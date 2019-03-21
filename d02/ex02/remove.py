# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    add_tail.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/06 12:32:26 by ispirido          #+#    #+#              #
#    Updated: 2018/07/06 14:42:53 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from add_tail import add_tail

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node: {self.value}"

def remove(list_head, val):
    current = list_head
    prev = None
    while current.next:
        prev = current
        current = current.next
        if current.value == val:
            prev.next = current.next
            break
   

def print_items(head):
    current = head
    while current:
        print(current.value)
        current = current.next

if __name__ == "__main__":
    alice = Node("Alice")
    bob = Node("Bob")
    alice.next = bob

    add_tail(alice, "Chad")
    print_items(alice)
    remove(alice, "Chad")
    print("removing ..........")
    print_items(alice)
