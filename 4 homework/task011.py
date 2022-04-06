def amount_of_newborn_people_prediction(number_of_women: int, average_age: int, country_wellbeing_coef: float) -> int:
    rest_of_fertility_period: int # local
    rest_of_fertility_period = 55 - average_age

    def max_amount_of_children() -> float:
        children_per_woman: float # enclosed
        if country_wellbeing_coef > 7:
            children_per_woman = 6 / country_wellbeing_coef
        else:
            children_per_woman = 18 / country_wellbeing_coef
        return children_per_woman
    return int(number_of_women * max_amount_of_children() * (rest_of_fertility_period / 15))


print('Type the number of woman in this country below')
this_number_of_women = int(input()) # global
print('Type the average age of woman here below')
this_average_age = int(input()) # global
print('Type the life expectancy of woman in this country below')
this_country_wellbeing_coef = float(input()) # global

print(amount_of_newborn_people_prediction(this_number_of_women, this_average_age, this_country_wellbeing_coef))
