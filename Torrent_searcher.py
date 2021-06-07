# /usr/bin/env python3

from bs4 import BeautifulSoup
import requests

search = input("Enter torrent name to search :")
page = 0 

url = (rf"https://thepiratebay10.org/search/{search}/{page}/99/0")

r = requests.get(url)
soup = BeautifulSoup(r.content , 'html.parser') 


        

title_list=soup.find_all('div',class_='detName')
i=1
for title in title_list:
    print(i,")",title.text)
    i=i+1
    
   
magnet = soup.find_all('a',title='Download this torrent using magnet')
magnetic_link = []       
for m in magnet:
    magnetic_link.append(m['href'])

print("Enter the index number -->")
index = int(input())

    
magnet_link=(magnetic_link[index-1])  
print("Your magnetic link...")
print("\n")
print(magnet_link)
print("\n")



  
        
    
      
