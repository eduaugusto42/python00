def ft_count_harvest_recursive() -> None:
    i = int(input("Days until harvest: "))
    ft_count_harvest_recursive_helper(i)
    print("Harvest time!\n")


def ft_count_harvest_recursive_helper(i: int) -> None:
    if i > 1:
        ft_count_harvest_recursive_helper(i - 1)
    print(f"Day {i}\n")
