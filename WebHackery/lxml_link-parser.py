from io import BytesIO
from lxml import etree
import requests

url = "https://student.must.ac.ke"
r = requests.get(url) # GET
content = r.content # content is of type 'bytes'

parser = etree.HTMLParser()
content = etree.parse(BytesIO(content), parser=parser)
for link in content.findall('//a'): # find all "a" anchor elements
    print(f"{link.get('href')} -> {link.text}")
    