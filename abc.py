#bibliotek
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time


URL = "https://www.nordnet.no/market/stocks?sortField=turnover&sortOrder=desc&exchangeCountry=NO"

# stock 1
equinor = "https://www.nordnet.no/market/stocks/16105420-equinor"
equinor_price_dict = {}
for _ in range (1, 4):
    result = requests.get(equinor).text
    doc = BeautifulSoup(result, "html.parser")
    tbody = doc.find_all("span",\
                         class_="Typography__Span-sc-10mju41-0 gaHPGY Typography__StyledTypography-sc-10mju41-1 epuleM StatsBox__StyledPriceText-sc-163f223-2 djnBAa")
#     print(tbody)
    equinor_price_dict[datetime.now().strftime("%d/%m/%Y %H:%M:%S")] = tbody[0].text
    sleep(15)
    
print(equinor_price_dict)

# stock 2
Telenor = {}







Telenor_price_dict = {}


# stock 3
Norsk_hydro = ""
Norsk_hydro_price_dict = {}

# stock 4
Kahoot = ""
Kahoot_price_dict = {}

# stock 5
Yara = ""
Yara_price_dict = {}
