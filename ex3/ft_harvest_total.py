# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_harvest_total.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: eduaaugu <eduaaugu@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/24 22:10:17 by eduaaugu         #+#    #+#              #
#    Updated: 2026/08/24 22:12:58 by eduaaugu        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_harvest_total():
    d1 = int(input("Day 1 harvest: "))
    d2 = int(input("Day 2 harvest: "))
    d3 = int(input("Day 3 harvest: "))
    print(f"Total harvest: {d1 + d2 + d3}\n")
