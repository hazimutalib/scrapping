from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import streamlit as st
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

st.markdown(
    """
    <style>
    .reportview-container {
        background-image: linear-gradient(#A9A9A9,#C0C0C0,#D3D3D3,#DCDCDC);
   	 	color: black;
   	 	font-family: "Oswald"

    }
 	</style>
""",
    unsafe_allow_html=True,
)


st.markdown("""<style>
  h1,h2,h3,h4,h5,h6 {font-family: "Oswald"}
  </style>""", unsafe_allow_html=True)


req = Request('http://www.matrade.gov.my/en/97-contents/links-malaysia/343-government-ministries', headers = {'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, 'html.parser')

containers = page_soup.findAll('div', {'class':'newsitem_text'})[0].findAll('a')

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



req_3 = Request(containers[4]['href'], headers = {'User-Agent': 'Mozilla/5.0'})
webpage_3 = urlopen(req_3).read()
page_soup_3 = soup(webpage_3, 'html.parser')

containers_3 = page_soup_3.findAll('ul',{'class':'latestnews'})

st.markdown('### MOE')
for container in containers_3:
  container.a['href'] = containers[4]['href']+ container.a['href']
  st.markdown(f""" ###### {container.a}
    """, unsafe_allow_html = True)

st.markdown('### MOF')

req_4 = Request(containers[7]['href'], headers = {'User-Agent': 'Mozilla/5.0'})
webpage_4 = urlopen(req_4).read()
page_soup_4 = soup(webpage_4, 'html.parser')

containers_4 = page_soup_4.findAll('div', {'class':'k2ItemsBlock'})


for container in containers_4:
  container.a['href'] = containers[7]['href']+ container.a['href']
  st.markdown(f""" ###### {container.a}
    """, unsafe_allow_html = True)


st.markdown('### MOH')

req_5 = Request('https://www.moh.gov.my/index.php/pages/view/2573', headers = {'User-Agent': 'Mozilla/5.0'})
webpage_5 = urlopen(req_5).read()
page_soup_5 = soup(webpage_5, 'html.parser')

containers_5 = page_soup_5.findAll('div',{'id':'223'})[0].findAll('tr')

for container in containers_5[:-1]:
  container.a['href'] = containers[9]['href']+ container.a['href']
  st.markdown(f""" ###### {container.a}
    """, unsafe_allow_html = True)


st.markdown('### MOHR')

req_6 = Request('https://www.mohr.gov.my/index.php/ms/', headers = {'User-Agent': 'XYZ/3.0'})
webpage_6 = urlopen(req_6,timeout=20).read()
page_soup_6 = soup(webpage_6, 'html.parser')

containers_6 = page_soup_6.findAll('li', {'class':'post'})

for container in containers_6:
  container.a['href'] = containers[10]['href']+ container.a['href']
  st.markdown(f""" ###### {container.a}
    """, unsafe_allow_html = True)