from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.matrade.gov.my/en/97-contents/links-malaysia/343-government-ministries'
uClient = uReq(my_url)

page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')

containers = page_soup.findAll('div', {'class':'newsitem_text'})[0].findAll('a')

import streamlit as st

st.sidebar.markdown('### Government Ministries')

for container in containers:
	st.sidebar.markdown(f""" ###### {container}
		""", unsafe_allow_html = True)



url_1 = containers[0]['href']
uClient_1 = uReq(url_1)
page_html_1 = uClient_1.read()
uClient_1.close()
page_soup_1 = soup(page_html_1, 'html.parser')