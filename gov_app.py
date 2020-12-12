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

from urllib.request import Request, urlopen

req_1 = Request(containers[0]['href'], headers = {'User-Agent': 'Mozilla/5.0'})
webpage_1 = urlopen(req_1).read()
page_soup_1 = soup(webpage_1, 'html.parser')

containers_1 = page_soup_1.findAll('div',{'class':'carousel-item'})


st.markdown('### MAFI')
for container in containers_1[9:]:
	container.a['href'] = 'https://www.mafi.gov.my/'+ container.a['href']
	st.markdown(f""" ###### {container.a}
		""", unsafe_allow_html = True)

