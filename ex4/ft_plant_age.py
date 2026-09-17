def ft_plant_age() -> None:
    days = int(input("Enter plant age in days: "))
    if days > 60:
        print("Plant is ready to harvest!\n")
    else:
        print("Plant needs more time to grow.\n")
