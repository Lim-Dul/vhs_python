"""
_summary_
"""
import locale
# import requests

locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")

url1 = "https://www.amazon.de/LEGO-75288-Action-Set-kreatives-Spielerlebnis/dp/B0813Q5JKX"
urls = [url1]

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

# # for url in urls:
# #     res = requests.get("https://www.amazon.de/LEGO-75288-Action-Set-kreatives-Spielerlebnis/dp/B0813Q5JKX",
# #                     headers=headers, timeout=10)
# #     txt = res.text
# #     with open(file="lego.html", mode="w", encoding="utf-8") as f:
# #         f.write(txt)
# #     print(txt)

prices = {}
with open(file="m17_lego.html", mode="r", encoding="utf-8") as f:
    txt = f.read()
    price_key = "displayPrice"
    pos_start = txt.index(price_key)
    pos_end = txt.index("€", pos_start)
    price_txt = txt[pos_start + len(price_key) + 3:pos_end - 1]
    print("\"" + price_txt + "\"")
    price = locale.atof(price_txt)
    prices["Lego"] = price

# print(prices)
