# -*- coding: utf-8 -*- 
import json
import re
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

    print(d['date'] + "," +d['title'])
    #print re.match(r'(.*)\(*.\)', d['title']).groups()
    #message = message.replace("(","").replace(")","")
    #roads, t, status = match.groups()
    #print category, roads, status, d['date']
f.close()
