from bs4 import BeautifulSoup
import requests
from csv import writer
url = ("https://kamernet.nl/huren/kamers-nederland")
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('div', class_="rowSearchResultRoom col s12 m6 l4")
with open('housing.csv','w', encoding='utf8', newline='') as f:
    thewriter= writer(f)
    header= ['Title', 'City', 'Room_Type', 'Rent', 'Availability','Date_Placed']
    thewriter.writerow(header)
    
    for list in lists:
        title = list.find('a',class_="tile-title truncate").text.replace('\n','')
        city = list.find('div', class_="tile-city").text.replace('\n','')
        roomtype = list.find('div', class_="tile-room-type").text.replace('\n','')
        rent = list.find('div', class_="tile-rent").text.replace('\n','')
        availability = list.find('div', class_="left").text.replace('\n','')
        dateplaced = list.find('div', class_="right tile-dateplaced").text.replace('\n','')
        info = [title,city,roomtype,rent,availability,dateplaced]
        thewriter.writerow(info)
        print(info)
