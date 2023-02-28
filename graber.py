from bs4 import BeautifulSoup
import requests

URL = "https://stackoverflow.com/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all('p'))