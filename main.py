from turtle import title

from bs4 import BeautifulSoup
import requests
import pandas as pd
import time



headers = {"User-Agent": "Mozilla/5.0"}

Title=[]
Brand=[]
Description=[]
Price=[]
Extra_features=[]

for page_num in range(1, 5):
  url = f"https://www.startech.com.bd/laptop-notebook?page={page_num}"
  res=requests.get(url, headers=headers)
  if res.status_code != 200:
    print(f"Page {page_num} failed: {res.status_code}")
    continue
  soup = BeautifulSoup(res.text, 'lxml')


  titles = soup.find_all('h4',class_='p-item-name')

  for t in titles:
        full_title = t.text.strip()
        Title.append(full_title)
        words = full_title.split()
        Brand.append(' '.join(words[:2]))
        Description.append(' '.join(words[2:]))




  prices = soup.find_all('div', class_='p-item-price')

  for p in prices:
    span = p.find('span', class_='price-new')
    text = span.text.strip() if span else p.text.strip()
    if text:
      Price.append(text.replace('৳', '').strip())
    else:
       Price.append("Out of Stock")  
    #import re
    #Price.append(re.sub(r'[^\d,]', '', text))

  

  items = soup.find_all("div", class_="short-description")

  for item in items:
    found = False  # Flag 
    
    for li in item.find_all("li"):
        text = li.get_text(strip=True)
        
        if text.startswith('Features'):
            feature = text.replace('Features:', '').strip()
            Extra_features.append(feature)
            found = True
            break  # break if one found
    
    if not found:  # no feature = N/A
        Extra_features.append("N/A")

  #nxt_btn = soup.find('ul', class_='pagination').find('a').get('href')  
  #print(nxt_btn)
  #url = nxt_btn if nxt_btn else None
  time.sleep(1.5)  
      
        

print (Extra_features)

print(len(Extra_features))
print(len(Brand))
print(len(Description))
print(len(Price))


df = pd.DataFrame({  
    
    "Brand": Brand,
    "Description": Description,
    "Extra Features": Extra_features,
    "Price": Price
    
})
df.to_csv("laptops1.csv", index=False)

print(df)
print(f"\nTotal {len(df)} products scraped.")