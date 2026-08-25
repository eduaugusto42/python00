# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_count_harvest_recursive.py                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: eduaaugu <eduaaugu@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/25 15:49:33 by eduaaugu         #+#    #+#              #
#    Updated: 2026/08/25 15:56:27 by eduaaugu        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_recursive():
    i = int(input("Days until harvest: "))
    ft_count_harvest_recursive_helper(i)
    print("Harvest time!\n")

def ft_count_harvest_recursive_helper(i: int):
    if i > 1:
        ft_count_harvest_recursive_helper(i - 1)
    print(f"Day {i}\n")
