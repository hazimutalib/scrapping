from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re


my_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
uClient = uReq(my_url)

page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')

containers = page_soup.findAll('div', {'class':'_4ddWXP'})

filename = "products.csv"
f = open(filename, "w")

headers = "model, rating, count, sale_price, original_price\n"

f.write(headers)

i=1
for container in containers:
	if i%4 !=0:
		model = container.div.div.div.img["alt"]
		rating = container.span.div.text
		count = re.sub("\D", '', container.findAll("span", {"class":"_2_R_DZ"})[0].text)
		sale_price = re.sub('\D', '', container.findAll("div", {"class":"_30jeq3"})[0].text)
		original_price = re.sub('\D', '', container.findAll("div", {"class":"_3I9_wc"})[0].text)
		
		print("model: " + model )
		print("rating: " + rating )
		print("count: " + str(count) )
		print("sale_price: " + str(sale_price))
		print("original_price: "+ str(original_price))

		f.write(model.replace(',',' ')+',')
		f.write(rating.replace(',',' ')+',')
		f.write(count+',')
		f.write(sale_price+ ',')
		f.write(original_price +'\n')
	
	i=i+1

f.close()


		