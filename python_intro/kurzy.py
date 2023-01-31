import httpx

url = ("https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=23.01.2023")

a = dict()

f = httpx.get(url)
milan = f.text.split("\n")
for row in milan[2:-1]:
    curr = float(row.split("|")[4].replace(",", "."))
    amount = float(row.split("|")[2])
    name = row.split("|")[1]
    a[name] = amount, curr

czk_user_input = float(input("zadej částku: ").replace(",", ".")) #částka v czk
s = ""
for i in a.items():
    s += i[0] + ", "
print(f"možnosti výběru: {s}") #vypsání měn, na které umožňuje program převádět

curr_input = input("zadej měnu, na kterou chcete konvertovat: ") #měna na konvertování
print(f"{czk_user_input} {curr_input} převedeno na czk: {czk_user_input * a[curr_input][1] / a[curr_input][0]}") 
print(f"{czk_user_input} czk převedeno na {curr_input}: {czk_user_input / a[curr_input][1] * a[curr_input][0]}") 