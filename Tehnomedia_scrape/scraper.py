import requests 
from bs4 import BeautifulSoup
import smtplib 

URL='https://www.tehnomedia.rs/bela-tehnika/masina-za-pranje-vesa/samsung-ww80t754dbh-s7.html#data'

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}


def check_price():
    
    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')  

    #print(soup.prettify())  

    price=soup.find(class_="theme_color").get_text() 
    

    
    converted_price=float(price[0:6])    
    
    if (converted_price>70.000):
        send_email()
    
    print(converted_price)


def send_email():
    server=smtplib.SMTP('64.233.184.108')  
    server.ehlo()     
    server.starttls()   
    server.ehlo()

    
    server.login('pavicaleksandra293@gmail.com','dnrrowxxdgecldog')

    
    subject="Hey, we have great news for you! Price of the machine fell down!"
    body="Chech this Tehnomedia link https://www.tehnomedia.rs/bela-tehnika/masina-za-pranje-vesa/samsung-ww80t754dbh-s7.html#data"

    msg=f"Subject: {subject}\n\n{body}"

    server.sendmail('pavicaleksandra293@gmail.com','aleksandra.pavic99@gmail.com',msg)

    print('Hey an email has been sent!')

    server.quit()

check_price()