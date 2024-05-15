import urllib.parse
import urllib.request

url = "http://boodelyboo.com"

with urllib.request.urlopen(url) as resp: # GET
    content = resp.read()

print(content)