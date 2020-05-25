# source -- https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

one_a_tag = soup.find_all('a')[36]

link = one_a_tag['href']

download_url = 'http://web.mta.info/developers/' + link

urllib.request.urlretrieve(download_url)

urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])

time.sleep(1)

# source -- https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
