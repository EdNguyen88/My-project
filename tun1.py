from bs4 import BeautifulSoup
import requests

url = 'https://portal.vietcombank.com.vn/Personal/TG/Pages/ty-gia.aspx?devicechannel=default'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

usd_rate = soup.find('td', {'data-ccy':
                            'USD'}).dind_next_sibling('td').text
usd_rate = float(usd_rate.replace(',', ''))

money_convention = input("Hay nhap so tien ban muon doi: ")
money = int(money_convention[:-3])
i_convention = money_convention[-3:]

result = int(0)
o_convention = ""
if i_convention.upper() == "USD":
    result = int(money * usd_rate)
    o_convention = "VND"
elif i_convention.upper() == "VND":
    result = int(round(money / usd_rate))
    o_convention = "USD"
else:
    print("Hay nhap dung gia tri.")
    quit()

formatted_result = "{:,}".format(result)
print(f"So tien ma ban nhan duoc la: {formatted_result} {o_convention}")
