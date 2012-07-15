#-*- coding: utf-8 -*-

import HTMLParser
import urllib

for j in range(1,14):
    sock = urllib.urlopen("http://www.ang.pl/nauka/slownictwo/2/page/%d" % j)
    htmlSource = sock.read()
    l = htmlSource.rsplit('</tr>')
    n=len(l)-1
    i=1

    while(i<n):
        l[i]=l[i].replace('\t','')
        l[i]=l[i].replace('\x0D\n','')
        l[i]=l[i].replace('<tr class="r1">','')
        l[i]=l[i].replace('<tr class="r2">','')
        l[i]=l[i].replace('<td class="word_word">','')
        l[i]=l[i].replace('</td>','\t')
        l[i]=l[i].replace('<td class="word_translation">','')
        l[i]=l[i].replace('<td class="word_example">','')
        print l[i]
        i+=1

    sock.close()


