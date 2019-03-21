# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/31 09:45:47 by ispirido          #+#    #+#              #
#    Updated: 2018/07/31 15:25:22 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sort_asc import LinkedList
from random import randint

list_c = LinkedList()
[list_c.add_tail(list_c.head, randint(1,20)) for x in range(randint(7,13))]
list_c.sort_asc()
print("Random sorted list:")
list_c.print_list(list_c.h)
