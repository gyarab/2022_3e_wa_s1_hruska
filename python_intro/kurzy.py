import urllib.request

link = urllib.request.urlopen("https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt;jsessionid=034B7D5C9C0D6A4CE2ED6786D5B6B5D6?date=17.01.2023")
f = str(link.read()).split("\\n")
for i in range(len(f)):
    if "euro" in f[i]:
        print(f[i].split("|").pop())
