from bs4 import BeautifulSoup
import pandas as pd
import lxml
import requests

header = {
    'USER-AGENT':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

url = 'https://hh.ru/search/vacancy'
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'lxml')

vacancys = soup.find_all(class_='resume-search-item__name')

for vacancy in vacancys:
    print(vacancy.text)

vacancies_info = ['https://hh.ru/'+i['href'] for i in soup.select('span a')]
print(vacancies_info)

all_hh = []
for num, i in enumerate(vacancys):
    all_hh.append({
        'title': i.text,
        'url': vacancies_info[num]
    })
print(all_hh)

pd.DataFrame(all_hh).to_csv('hh1.csv')