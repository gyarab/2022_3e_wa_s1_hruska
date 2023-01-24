import urllib.request
import httpx
from pprint import pprint

link = urllib.request.urlopen("https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=23.01.2023")
url = ("https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=23.01.2023")

a = dict()

f = httpx.get(url)
milan = f.text.split("\n")
for row in milan[2:-1]:
    curr = row.split("|")[4]
    name = row.split("|")[1]
    a[name] = curr

pprint(a)
############################################
"""
milan = str(input()).split(" ")
if len(milan) != 2:
    print("chyba u vstupu")
else:
    f = str(link.read()).split("\\n")
    for i in range(len(f)):
        if milan[0] in f[i]:
            print(float(f[i].split("|").pop().replace(",", ".")) * int(milan[1]))
"""