def wine_appreciation(week):
    if len(week) <= 1:
        return 0
    lowest = week[0]
    highestsell = 0
    for day in range(1, len(week)):
        if week[day] < lowest:
            lowest = week[day]
        else:
            current = week[day] - lowest
            if current > highestsell:
                highestsell = current

    return highestsell

print(wine_appreciation([]))
#      enter values here ^