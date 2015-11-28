#!/usr/bin/env python
import json
import urllib2


f = open('top10k', 'w')
scoreRange = range(0,10000,50)
for i in scoreRange:
    url = 'http://services.runescape.com/m=hiscore/ranking.json?table=0&category=0&size=50&toprank={}'.format(str(i))
    hiscores = json.load(urllib2.urlopen(url))

    for obj in hiscores:
        value = (obj['name']+'\n')

        f.write(str(value))

f.close()