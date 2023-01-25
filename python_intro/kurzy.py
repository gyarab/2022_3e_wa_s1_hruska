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

czk_user_input = float(input("zadej částku v czk: ").replace(",", "."))
print("možnosti výběru: ")
s = ""
for i in a.items():
    s += i[0] + ", "
print(f"možnosti výběru: {s}")

curr_input = input("zadej část, na kterou chceš konvertovat: ")
print(f"{czk_user_input} czk převedeno na danou měnu: {czk_user_input *  a[curr_input][1] / a[curr_input][0]}")