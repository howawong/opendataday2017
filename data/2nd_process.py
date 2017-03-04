# -*- coding: utf-8 -*- 
import json
import re
f = open('j.json', 'r')
rows = json.loads(f.read())
for d in rows:
    d['title'] = d['title'].encode('utf-8')

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
    print ",".join([d['title'], d['date']])

    #message = message.replace("(","").replace(")","")
    #roads, t, status = match.groups()
    #print category, roads, status, d['date']
f.close()
