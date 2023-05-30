import requests
import csv
from time import sleep
from random import randint
from bs4 import BeautifulSoup

url = 'https://www.thewhiskyexchange.com/c/32/irish-whiskey?'
payloads = {
    'pg': 1
}

file = open('data.csv', 'w', newline='\n')
obj = csv.writer(file)
obj.writerow(['NAME', 'ALC_PERCENTAGE', 'PRICE', 'LINK'])

whiskeys = []

while payloads['pg'] < 6:
    response = requests.get(url, payloads)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    grid = soup.find('div', class_='product-grid')
    items = grid.find_all('li', class_='product-grid__item')

    for each in items:
        name = each.p.text.strip()
        alc_percentage = each.find('p', class_="product-card__meta").text.strip()
        price = each.find('p', class_="product-card__price").text.strip().replace('£', 'GBP ')

        product_url = each.a['href']
        base_url = 'https://www.thewhiskyexchange.com/'
        absolute_url = base_url + product_url

        # avoiding duplicate entries
        if name not in whiskeys:
            obj.writerow([name, alc_percentage, price, '=HYPERLINK("{}")'.format(absolute_url)])
            print(f"Whiskey name: '{name}'\nAlcohol percentage: {alc_percentage}\nPrice: {price}\nLink: {absolute_url}")
            print()
            whiskeys.append(name)

    payloads['pg'] += 1
    sleep(randint(5, 10))

