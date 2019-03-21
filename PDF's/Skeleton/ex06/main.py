# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wto <marvin@42.fr>                         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/24 05:42:48 by wto               #+#    #+#              #
#    Updated: 2018/03/24 05:54:26 by wto              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from classroom import Classroom

if __name__ == "__main__":
    classroom1 = Classroom("Wesley")
    classroom2 = Classroom("Anand")
    classroom1.add_student("Alice")
    classroom2.add_student("Bob")
    classroom1.add_student("Carol")
    classroom2.add_student("Dave")
    classroom1.add_student("Eve")
    classroom1.status()
    classroom2.status()
    classroom1.begin_class()
    classroom2.begin_class()
