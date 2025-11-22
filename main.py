import requests
import smtplib
from bs4 import BeautifulSoup
from email.message import EmailMessage

app_password_person_shidhu = " Your app passwodr"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
Url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
response = requests.get( Url,headers=header)
soup = BeautifulSoup(response.text,"html.parser")
price_tag = soup.find(name =  "span", class_="a-price-fraction" )
price = price_tag.get_text()
price = int(price)

if price<100:
    msg = EmailMessage()
    msg['Subject'] = f"product Deal Alert: Price:{price}"
    msg['From'] = "shidhu@gmaill.com"
    msg['To'] = "pshidhu@gmail.com"
    msg.set_content(f"Product price droped to  at just {price}")

    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.starttls()
        smtp.login("personshidhu@gmail.com",app_password_person_shidhu)
        smtp.send_message(msg)
    print("done")
else:
    pass
