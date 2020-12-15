from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import streamlit as st

req_1 = Request('https://www.mafi.gov.my/', headers = {'User-Agent': 'Mozilla/5.0'})
webpage_1 = urlopen(req_1).read()
page_soup_1 = soup(webpage_1, 'html.parser')

st.markdown(f""" {page_soup_1}
		""", unsafe_allow_html = True)