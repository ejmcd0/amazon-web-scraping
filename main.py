import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

my_email = MY_EMAIL
password= PASSWORD

amazon_url = "https://www.amazon.com/Keurig-K-Express-Coffee-Single-Brewer/dp/B09715G57M/ref=zg_bs_g_289913_d_sccl_1/136-3752427-1998925?psc=1"

headers= {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

response = requests.get(url=amazon_url, headers=headers)
site = response.text

soup = BeautifulSoup(site, 'lxml')
#print(soup)

cost = soup.find(name='span', class_='a-offscreen')
price = float(cost.getText().split('$')[1])
product_name = soup.find(id='productTitle').getText().strip()

if price < 70.00:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject: Low Price Alert!\n\n"
                                f"The current price of {product_name} is ${price}. "
                                f"Click here {amazon_url} to buy it!"
                            )
