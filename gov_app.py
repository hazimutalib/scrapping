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


st.markdown('### MOHA')

req_6 = Request('http://www.moha.gov.my/index.php/ms/', headers = {'User-Agent': 'Mozilla/5.0'})
webpage_6 = urlopen(req_6).read()
page_soup_6 = soup(webpage_6, 'html.parser')

containers_6 = page_soup_6.findAll('div',{'class':'carian-popular'})[0].findAll('li')

for container in containers_6:
  container.a['href'] = containers[10]['href']+ container.a['href']
  st.markdown(f""" ###### {container.a}
    """, unsafe_allow_html = True)




st.markdown('### MOHR')

req_7 = Request('https://www.mohr.gov.my/index.php/ms/', headers = {'User-Agent': 'XYZ/3.0'})
webpage_7 = urlopen(req_7,timeout=20).read()
page_soup_7 = soup(webpage_7, 'html.parser')

containers_7 = page_soup_7.findAll('li', {'class':'post'})

for container in containers_7:
  container.a['href'] = containers[11]['href']+ container.a['href']
  st.markdown(f""" ###### {container.a}
    """, unsafe_allow_html = True)


st.markdown('### MPIC')

req_8 = Request(containers[14]['href'], headers = {'User-Agent': 'Mozilla/5.0'})
webpage_8 = urlopen(req_8).read()
page_soup_8 = soup(webpage_8, 'html.parser')

containers_8 = page_soup_8.findAll('div',{'class':'sprocket-lists'})[0].findAll('li')

for container in containers_8[:-1]:
  container.a['href'] = containers[14]['href']+ container.a['href']
  st.markdown(f""" ###### {container.a}
    """, unsafe_allow_html = True)


st.markdown('### RURAL')

req_9 = Request('https://www.rurallink.gov.my/', headers = {'User-Agent': 'Mozilla/5.0'})
webpage_9 = urlopen(req_9).read()
page_soup_9 = soup(webpage_9, 'html.parser')

containers_9 = page_soup_9.findAll('h3',{'class':'elementor-post__title'})

for container in containers_9:
  st.markdown(f""" ###### {container}
    """, unsafe_allow_html = True)



st.markdown('### MOSTI')

req_10 = Request('https://www.mosti.gov.my/web/', headers = {'User-Agent': 'Mozilla/5.0'})
webpage_10 = urlopen(req_10).read()
page_soup_10 = soup(webpage_10, 'html.parser')

containers_10 = page_soup_10.findAll('ul',{'class':'display-posts-listing'})[0].findAll('li')

for container in containers_10:
  st.markdown(f""" ###### {container.a}
    """, unsafe_allow_html = True)


st.markdown('### MOTOUR')

req_11 = Request('http://www.motour.gov.my/', headers = {'User-Agent': 'Mozilla/5.0'})
webpage_11 = urlopen(req_11).read()
page_soup_11 = soup(webpage_11, 'html.parser')

containers_11 = page_soup_11.findAll('table',{'class':'uk-table uk-table-condensed'})[0].findAll('tr')

for container in containers_11:
  container.a['href'] = 'http://www.motour.gov.my/'+ container.a['href']
  st.markdown(f""" ###### {container.a}
    """, unsafe_allow_html = True)



st.markdown('### MOT')

req_12 = Request('https://www.mot.gov.my/en', headers = {'User-Agent': 'Mozilla/5.0'})
webpage_12 = urlopen(req_12).read()
page_soup_12 = soup(webpage_12, 'html.parser')

containers_12 = page_soup_12.findAll('div', {'id':'ctl00_ctl50_g_74ad80ce_403e_4d56_a0f2_2e99ef765303'})[0].findAll('li')

for container in containers_12:
  container.a['href'] = 'https://www.mot.gov.my/'+ container.a['href']
  st.markdown(f""" ###### {container.a}
    """, unsafe_allow_html = True)


st.markdown('### KPKT')

req_13 = Request('https://www.kpkt.gov.my/', headers = {'User-Agent': 'Mozilla/5.0'})
webpage_13 = urlopen(req_13).read()
page_soup_13 = soup(webpage_13, 'html.parser')

containers_13 = page_soup_13.findAll('div',{'class':'content-assessment-tag-container'})[0].findAll('tr')

for container in containers_13:
  container.img['src'] = 'https://www.kpkt.gov.my/'+ container.img['src']
  container.a['href'] = 'https://www.kpkt.gov.my/'+ container.a['href']
  st.markdown(f""" ###### {container}
    """, unsafe_allow_html = True)


st.markdown('### KPWKM')

req_14 = Request('https://www.kpwkm.gov.my/kpwkm/index.php?r=portal/index', headers = {'User-Agent': 'Mozilla/5.0'})
webpage_14 = urlopen(req_14).read()
page_soup_14 = soup(webpage_14, 'html.parser')

containers_14 = page_soup_14.findAll('div',{'class':'homeset-backColor'})[0].findAll('li')[:4]

for container in containers_14:
  container.a['href'] = 'https://www.kpwkm.gov.my/'+ container.a['href']
  st.markdown(f""" ###### {container.a}
    """, unsafe_allow_html = True)


st.markdown('### KKR')

req_15 = Request('http://www.kkr.gov.my/ms', headers = {'User-Agent': 'Mozilla/5.0'})
webpage_15 = urlopen(req_15).read()
page_soup_15 = soup(webpage_15, 'html.parser')

containers_15 = page_soup_15.findAll('div',{'class':'hsr-hot-topics'})[0].findAll('li')

for container in containers_15:
  container.a['href'] = 'http://www.kkr.gov.my/'+ container.a['href']
  st.markdown(f""" ###### {container.a}
    """, unsafe_allow_html = True)


st.markdown('### KBS')

req_16 = Request('http://www.kbs.gov.my/info-terkini.html', headers = {'User-Agent': 'Mozilla/5.0'})
webpage_16 = urlopen(req_16).read()
page_soup_16 = soup(webpage_16, 'html.parser')

containers_16 = page_soup_16.findAll('table',{'class':'category table table-striped table-bordered table-hover'})[0].findAll('tr')

for container in containers_16:
  container.a['href'] = 'http://www.kbs.gov.my/'+ container.a['href']
  st.markdown(f""" ###### {container.a}
    """, unsafe_allow_html = True)