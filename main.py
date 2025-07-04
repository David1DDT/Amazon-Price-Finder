import requests
from bs4 import BeautifulSoup
import smtplib
import os

password = os.getenv("PASSWORD")
response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1", headers={"Accept-Language":"en-US"})
html_code = response.text

soup = BeautifulSoup(html_code, "html.parser")
price = int(soup.find("span", class_="a-price-whole").getText().replace(".", "")) # type: ignore

if price > 100:
    smtp = smtplib.SMTP("smtp.gmail.com", port=587)
    smtp.starttls()
    smtp.login(user=os.getenv("EMAIL"), password=password) #type: ignore

    smtp.sendmail(
            from_addr=os.getenv("EMAIL"), # type: ignore
            to_addrs=os.getenv("EMAIL"), # type: ignore
            msg=f"Subject:Price alert \n\n the pressure cooker is below 100"
            )