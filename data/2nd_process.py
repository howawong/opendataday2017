# -*- coding: utf-8 -*- 
import json
import re
from datetime import datetime
f = open('j.json', 'r')
rows = json.loads(f.read())
for d in rows:
    d['title'] = d['title'].encode('utf-8')
    d['date'] = d['date'].encode('utf-8')
    
    d['title'] = d['title'].replace('：', ':')
    d['title'] = d['title'].replace('︰', ':')
    d['title'] = d['title'].replace('﹕', ':')
    d['title'] = d['title'].replace('；', ':')
    d['title'] = d['title'].replace(': ', ':')
    d['title'] = d['title'].replace('：：', ':')
    d['title'] = d['title'].replace('：', ':')
    d['title'] = d['title'].replace(' :', ':')
    d['title'] = d['title'].replace(' :', ':')
    d['title'] = d['title'].replace(':', ':')
    d['title'] = d['title'].replace('(', '(')
    d['title'] = d['title'].replace('）', ')')
    d['title'] = d['title'].replace(')', ')')
    d['title'] = d['title'].replace('(', '(')
    m = re.match(r'(.*)\((.*)\)', d['title'])
    if m == None:
        groups = re.match(r'(.*)(\d\d:\d\d.*)\)', d['title']).groups()
    else:
        groups = m.groups()
    cat = "" 
    t = ""
    year = ""
    month = ""
    day = ""
    t2 = ""
    status = ""
    hour = ""
    minute = ""
    
    if len(groups) == 2:
        parts = [x for x in groups[0].split(':') if x != ""]
        s = str(groups[1]).strip()
        
        g2  = re.match(r'(\d+:\d\d)(.*)', s)
        if g2 == None:
            continue
        t_short, status = g2.groups()
        t2 = datetime.strptime(d['date'], '%d.%m.%Y %H:%M')
        year, month, day = t2.year, t2.month, t2.day
        hour = t2.hour
        minute = t2.minute
        if len(parts) == 1:
            t = parts[0]
        elif len(parts) > 2:
            continue
        else:
            cat, t = parts
    #message = message.replace("(","").replace(")","")
    #roads, t, status = match.groups()
    print  ",".join([str(year),str(month), str(day), str(hour) , str(minute), cat.strip(), t.strip(), status.strip()])
    #print category, roads, status, d['date']
f.close()
