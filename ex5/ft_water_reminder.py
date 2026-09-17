def ft_water_reminder() -> None:
    i = int(input("Days since last watering: "))
    if i > 2:
        print("Water the plants!\n")
    else:
        print("Plants are fine\n")
