from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

req = Request('http://www.matrade.gov.my/en/97-contents/links-malaysia/343-government-ministries', headers = {'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, 'html.parser')

containers = page_soup.findAll('div', {'class':'newsitem_text'})[0].findAll('a')

import streamlit as st

st.sidebar.markdown('### Government Ministries')

for container in containers:
	st.sidebar.markdown(f""" ###### {container}
		""", unsafe_allow_html = True)

req_1 = Request(containers[0]['href'], headers = {'User-Agent': 'Mozilla/5.0'})
webpage_1 = urlopen(req_1).read()
page_soup_1 = soup(webpage_1, 'html.parser')

containers_1 = page_soup_1.findAll('div',{'class':'carousel-item'})


st.markdown('### MAFI')
for container in containers_1[9:]:
	if container.a['href'][0] != 'h':
		container.a['href'] = 'https://www.mafi.gov.my/'+ container.a['href']
	st.markdown(f""" ###### {container.a}
		""", unsafe_allow_html = True)

req_2 = Request(containers[2]['href'], headers = {'User-Agent': 'Mozilla/5.0'})
webpage_2 = urlopen(req_2).read()
page_soup_2 = soup(webpage_2, 'html.parser')

containers_2 = page_soup_2.findAll('h3',{'class':'uk-panel-title'})


st.markdown('### MOD')
for container in containers_2:
	container.a['href'] = 'http://www.mod.gov.my'+ container.a['href']
	st.markdown(f""" ###### {container.a}
		""", unsafe_allow_html = True)





