# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    print_list.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/06 14:49:55 by ispirido          #+#    #+#              #
#    Updated: 2018/07/06 15:01:25 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node: {self.value}"

def print_list(list_head):
    current = list_head
    while current.next:
        current = current.next

if __name__ == "__main__":
    alice = Node("Alice")
    bob = Node("Bob")
    alice.next = bob

    print_list(alice)
    
    current = alice
    while current:
        print(current.value)
        current = current.next
