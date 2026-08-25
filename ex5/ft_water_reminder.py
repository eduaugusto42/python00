# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_water_reminder.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: eduaaugu <eduaaugu@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/24 22:23:23 by eduaaugu         #+#    #+#              #
#    Updated: 2026/08/24 22:29:19 by eduaaugu        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_water_reminder():
    i = int(input("Days since last watering: "))
    if i > 2:
        print("Water the plants!\n")
    else:
        print("Plants are fine\n")
