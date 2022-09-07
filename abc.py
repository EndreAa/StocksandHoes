import re
from unittest import result
import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.nordnet.no/market/stocks?sortField=turnover&sortOrder=desc&exchangeCountry=NO"
result = requests.get(URL).text
doc = bs(result, "html.parser")

tbody = doc.find_all("tbody") #blir blokkert (?) spør Adi
print(tbody)
