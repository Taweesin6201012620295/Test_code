# Refference https://www.youtube.com/watch?v=X2EpWtIYIjY&t=319s&fbclid=IwAR2Nl5iefEZI7wjydNAD-3H3LCScm0geNAsXRGn-rqqeZ1Mr9k7xnPcsMR0&ab_channel=BorntoDev

import requests                 # รับลิ้งเข้า python
from bs4 import BeautifulSoup   # กรองให้เหลือส่วนของข้อมูลที่เราต้องการ

url = "https://www.thairath.co.th/" 
web_data = requests.get(url)

soup = BeautifulSoup(web_data.text, "html.parser")
find_word = soup.find_all("h3",{"class":"css-16shodj efr6tej3"}) # ค้นหาข้อมูลที่มี Class ชื่อนี้ #เรื่องโควิด
for i in find_word:
    print(i.text)       