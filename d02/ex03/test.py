# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/31 09:45:47 by ispirido          #+#    #+#              #
#    Updated: 2018/07/31 10:27:31 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from has_cycle import LinkedList

llist = LinkedList()
print('Cycle? ', end='')
print('yes' if llist.has_cycle(llist.head) else 'no')
tail = llist.head
while tail:
    tail = tail.next
    tail.next = llist.head
print('Cycle? ', end='')
print('yes' if llist.has_cycle(llist.head) else 'no')
tail.next = None
