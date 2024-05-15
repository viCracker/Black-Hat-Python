import urllib.parse
import urllib.request

url = "https://website.com/login"
info = {"user": "vicracker", "pass" :  "123vi4"}
data = urllib.parse.urlencode(info).encode()  # data is type bytes

req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as resp: # POST
    content = resp.read()

print(content)