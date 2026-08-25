# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_count_harvest_iterative.py                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: eduaaugu <eduaaugu@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/25 15:41:24 by eduaaugu         #+#    #+#              #
#    Updated: 2026/08/25 15:49:29 by eduaaugu        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_iterative():
    i = int(input("Days until harvest: "))
    for y in range(1, i + 1):
        print(f"Day {y}\n")
    print(f"Harvest time!\n")
