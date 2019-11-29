#wemake.py

import ssl
context = ssl._create_unverified_context()

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()
result = urlopen("https://front.wemakeprice.com/category/division/2100132", context=context)
bsObj = BeautifulSoup(result.read(), "html.parser")

for tag in bsObj.findAll("a"):
    if "href" in tag.attrs:
        print(tag.attrs["href"])

