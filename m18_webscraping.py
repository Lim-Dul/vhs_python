"""
_summary_
"""
import locale
import requests

locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")

url1 = "https://www.amazon.de/LEGO-75288-Action-Set-kreatives-Spielerlebnis/dp/B0813Q5JKX"
url2 = "https://www.amazon.de/vanva-Zocken-Schild-Bielefeld-Ortsschild/dp/B08JSG25H5"
urls = [url1, url2]

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

prices = {}
for url in urls:
    res = requests.get(url=url, headers=headers, timeout=10)
    txt = res.text

    price_key = "displayPrice"
    pos_start = txt.index(price_key)
    pos_end = txt.index("€", pos_start)
    price_txt = txt[pos_start + len(price_key) + 3:pos_end - 1]
    price = locale.atof(price_txt)
    prices[url] = price

print(prices)
