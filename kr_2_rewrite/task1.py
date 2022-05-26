# variant no 4

import requests
from random import randint

print('Please, type the amount of houses:')
n = int(input())
n = n if n <= 444 else 444
url = 'https://anapioficeandfire.com/api/houses/'

file = open('houses.csv', 'w+')

regions = []
list_of_houses = []

for i in range(n):
    number = str(randint(1, 445))
    url_for_this_num = url + number
    response = requests.get(url_for_this_num).json()
    regions.append(response['region'])
    this_house = {'name': response['name'], 'region': response['region'], 'current lord':
                  (response['currentLord'] if response['currentLord'] != '' else 'no one')}
    list_of_houses.append(this_house)

regions.sort()
for reg in regions:
    for i in range(len(list_of_houses)):
        if list_of_houses[i]['region'] == reg:
            file.write(str(list_of_houses[i]) + '\n')
            