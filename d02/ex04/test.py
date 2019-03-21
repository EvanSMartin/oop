# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/31 09:45:47 by ispirido          #+#    #+#              #
#    Updated: 2018/07/31 11:27:07 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from merge import LinkedList
from random import randint

def train(size, party):
    out = LinkedList()
    if party == 0:
        size = 2 * int(size/2)
    elif size % 2 == 0:
        size -= 1
    for x in range(size, 0, -2):
        out.add_tail(out.head, x)
    return out

llist_a = train(10, 0)
llist_b = train(10, 1)
print('Merge:')
train = LinkedList.merge(llist_a.head, llist_b.head)
llist_a.print_list(train)
