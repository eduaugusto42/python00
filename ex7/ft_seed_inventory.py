# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_seed_inventory.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: eduaaugu <eduaaugu@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/24 22:29:54 by eduaaugu         #+#    #+#              #
#    Updated: 2026/08/25 10:05:20 by eduaaugu        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available\n")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total\n")
    elif unit == "area":
        print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters\n")
    else:
        print("Unknown unit type\n")
