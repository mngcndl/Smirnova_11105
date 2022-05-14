def amount_of_newborn_people_prediction(number_of_women: int, average_age: int,
                                        country_wellbeing_coef: (int, float)) -> int:
    if not isinstance(number_of_women, int):
        raise TypeError
    if not isinstance(average_age, int):
        raise TypeError
    if not isinstance(country_wellbeing_coef, (int, float)):
        raise TypeError

    rest_of_fertility_period: int  # local
    if average_age > 50:
        rest_of_fertility_period = abs(50 - average_age) * 2
    elif average_age == 50:
        rest_of_fertility_period = 7
    else:
        rest_of_fertility_period = 50 - average_age

    def max_amount_of_children() -> float:
        children_per_woman: float  # enclosed
        if country_wellbeing_coef >= 6:
            children_per_woman = 3 / country_wellbeing_coef
        else:
            children_per_woman = 6 / country_wellbeing_coef
        return children_per_woman

    return int(number_of_women * max_amount_of_children() * (rest_of_fertility_period / 15))
