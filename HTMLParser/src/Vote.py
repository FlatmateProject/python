import urllib

sock = urllib.urlopen("http://plebiscyt.checiny.pl/index.php?option=com_pollxt&Itemid=2")
htmlSource = sock.read()
print htmlSource
sock.close()