from bs4 import BeautifulSoup
from datetime import datetime
import json
import os
def parse(filename):
    f = open(filename, 'r')
    s = f.read()
    soup = BeautifulSoup(s, 'html.parser')
    links = soup.find_all('a', {"class":"hyRoadTitle"}) + soup.find_all('a', {"class":"hyRoadTitleTop2"})
    dates = soup.find_all('span', {"class": "hyRoadDate"})
    rows = []
    #output = zip([l.text for l in links], [datetime.strptime(d.text, '%d.%m.%Y %H:%M') for d in dates])
    output = zip([l.text for l in links], [d.text for d in dates], [l['href'] for l in links])
    for o in output:
        d = {'title': o[0], 'date': o[1], 'link': o[2]}
        rows.append(d)
    f.close()
    return rows

all_rows = []
htmls = [f for f in os.listdir('.') if f.endswith("html")]
for html in htmls:
    all_rows = all_rows + parse(html)
f = open('j.json', 'w')
f.write(json.dumps(all_rows))
f.close()
