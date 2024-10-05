
import requests
import lxml
from bs4 import BeautifulSoup
#아마존 사이트에서 울버린 피규어 가격 가져오기

url = 'https://www.amazon.com/HiPlay-Wolverine-Collectible-Action-Figures/dp/B0DCVK35QK/ref=sr_1_1?crid=159WCTN902YXZ&dib=eyJ2IjoiMSJ9.G_DlXZZQwZwSOr6-1Jz5ywniGJXavF33sxfZL0hFGzXxsG0cXceHsCf9kwMxvbRBqbieXVxIYAYK5Vr1DnXx4R1tndwq2MesGUAknW9b3N1J02ROlJDOzjSDBW1waz2nFi3V7i0hYyldFSi9CHSGmNNHiNizn4f0W_7rn05swR73Vho2jlde75TpBKoPKKmTSRnzLgPzER46d2tChzRShiW8qGxhaRX5NR1Gaf4UIB-qOJBlgQ9pJXtBtwhalmisU5QFV4TP3lGXKTtW0u26aRQ6OsG6YmGufEg8hkuVluo.Dq6F_U-V19goZCm0Ft7nhpYknAfMmNE9JO4YGfnQgQA&dib_tag=se&keywords=figure&qid=1727954060&sprefix=figur%2Caps%2C335&sr=8-1&th=1'
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url=url, headers=header)
data = response.content
soup = BeautifulSoup(data, 'lxml')

price = soup.find(class_='a-price-whole')
decimal = soup.find(class_='a-price-fraction')
#정수자리 + 소수점자리
full_price = float(price.getText() + decimal.getText())

title = soup.find(id="productTitle").get_text().strip()
print(f'상품명 : {title}')
print(full_price)