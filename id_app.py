from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req = Request('https://elhkpn.kpk.go.id/portal/user/login#', headers = {'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, 'html.parser')

containers = page_soup.findAll('div',{'class':'col-lg-6'})[5].findAll('a')


import streamlit as st

st.markdown('# elhkpn')

for container in containers:
	st.markdown(f""" ###### {container}
		""", unsafe_allow_html = True)
