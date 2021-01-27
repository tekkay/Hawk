import requests
from bs4 import BeautifulSoup
url = 'https://veja.abril.com.br/ultimas-noticias/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html')
print("List of all the h2 :")
for heading in soup.find_all(["h2"]):
    print(heading.name + ' ' + heading.text.strip())
