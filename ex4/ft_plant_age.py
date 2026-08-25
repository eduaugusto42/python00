# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_age.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: eduaaugu <eduaaugu@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/24 22:17:54 by eduaaugu         #+#    #+#              #
#    Updated: 2026/08/24 22:22:54 by eduaaugu        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_plant_age():
    days = int(input("Enter plant age in days: "))
    if days > 60:
        print("Plant is ready to harvest!\n")
    else:
        print("Plant needs more time to grow.\n")
