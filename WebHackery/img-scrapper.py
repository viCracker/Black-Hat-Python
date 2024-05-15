from bs4 import BeautifulSoup as bs
import requests

url = "https://student.must.ac.ke"
r = requests.get(url)
tree = bs(r.text, 'html.parser')
for pic in tree.find_all('img'):
    print(pic.get('src'))
