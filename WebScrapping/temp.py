
import requests
import csv
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/2019%E2%80%9320_Manchester_United_F.C._season'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')

# h2 = soup.find(lambda elm: elm.name == "h2" and "Squad statistics" in elm.text)

span = soup.find(id = "Squad_statistics")

table = span.find_next('table')

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)

with open('output.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


print(table)