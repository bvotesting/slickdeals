

#You should probably use an HTTP client like requests
#to get the document behind the URL, and feed that document to Beautiful Soup.

#Pull data from frontpage deals
#sort prices, find next best deal?

import requests, bs4

res= requests.get('https://slickdeals.net')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc))
    
res.status_code == requests.codes.ok 
#make sure its a valid website

#write to to text, html
playFile = open('deals.html', 'wb')
for chunk in res.iter_content(1000000):
    playFile.write(chunk)

playFile.close()

#beautiful soup
noStarch = bs4.BeautifulSoup(res.text)


#look for price line tag id and get listprice, itemPercentOff, title, itemprice
itemPrice = noStarch.select('.priceLine')
print(len(itemPrice))
print(type(itemPrice[0]))
print(itemPrice[0].getText())

for item in itemPrice:
    print(item)
    
