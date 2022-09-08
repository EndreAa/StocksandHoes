import re
from unittest import result
import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.nordnet.no/market/stocks?sortField=turnover&sortOrder=desc&exchangeCountry=NO"
result = requests.get(URL).text
doc = bs(result, "html.parser")

tbody = doc.find_all("tbody") #blir blokkert (?) spør Adi
print(tbody)


#################################################################

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep

URL = "https://www.nordnet.no/market/stocks?sortField=turnover&sortOrder=desc&exchangeCountry=NO"
equinor = "https://www.nordnet.no/market/stocks/16105420-equinor"
equinor_price_dict = {}
for _ in range (1, 3):
    result = requests.get(equinor).text
    doc = BeautifulSoup(result, "html.parser")
    tbody = doc.find_all("span",\
                         class_="Typography__Span-sc-10mju41-0 gaHPGY Typography__StyledTypography-sc-10mju41-1 epuleM StatsBox__StyledPriceText-sc-163f223-2 djnBAa")
#     print(tbody)
    equinor_price_dict[datetime.now().strftime("%d/%m/%Y %H:%M:%S")] = tbody[0].text
    sleep(15)
    
 print(equinor_price_dict)
 print()
