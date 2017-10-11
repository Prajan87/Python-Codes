import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
url = "https://www.nrb.org.np/fxmexchangerate.php"
uclient = uReq(url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("table",{"align":"center", "width":450})
rows = containers[0].findAll("tr")

filename = "nrb.csv"
f = open(filename, "w")
headers = "currency, Unit, buying rate, selling rate"
f.write(headers+"\n")
for i in range(9):
	col = rows[i+2].findAll("td");
	currency = col[0].text.strip()
	unit = col[1].text.strip()
	buy = col[2].text.strip()
	sell = col[3].text.strip()
	f.write(currency + ","+unit+","+buy+","+sell+"\n")