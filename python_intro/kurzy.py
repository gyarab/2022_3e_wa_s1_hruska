import urllib.request
#import httpx

link = urllib.request.urlopen("https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=23.01.2023")
#link = httpx.get("https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=23.01.2023")

f = str(link.read()).split("\\n")
for i in range(len(f)):
    if "euro" in f[i]:
        print(f[i].split("|").pop())
