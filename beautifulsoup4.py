#!pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

def getcontent(url:str):
    content = ''
    response = requests.get(url)
    if (response.status_code) ==200:
        BeautifulSoup(response.content, "html.parser")
        soup = BeautifulSoup(response.content, "html.parser")
        results = soup.find_all("p")
        for result in results:
            content = content+str(result)
        return content
    else:
        return False

html = ''
for i in range(2,19):
    content = getcontent('https://m.meiwen.org/article/93308_{}.html'.format(i))
    if content:
      html = html + content
    else:
        print('The last page is ',i-1)
        break

print('html length: ',len(html))
with open('luo.html','w') as f:
  f.write(html)