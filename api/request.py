import requests
import cfscrape


header = {'Referer': 'https://google.com.br'}

url = "https://www.megaloterias.com.br/mega-sena/resultados"
session = requests.Session()
sc = cfscrape.create_scraper(sess=session)

f = open('resultados.txt', 'w')
f.write(sc.get(url).text)
f.close

print (sc.get(url).text)