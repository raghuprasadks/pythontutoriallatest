# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
# Collect and parse first page
page = requests.get('http://shopping.rediff.com/?sc_cid=inhome_icon')
soup = BeautifulSoup(page.text, 'html.parser')

# Remove bottom links
last_links = soup.find(class_='AlphaNav')


