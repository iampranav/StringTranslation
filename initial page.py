import json, urllib2

fl = open("strings.xml", "a")

from xml.dom import minidom
xmldoc = minidom.parse('items.xml')
itemlist = xmldoc.getElementsByTagName('item')
print(len(itemlist))
print(itemlist[0].attributes['name'].value)
for s in itemlist:
    print(s.attributes['name'].value)


text = fl.readlines()
size = len(text)

baseUrl = "https://translate.yandex.net/api/v1.5/tr.json/translate"
accessKey = "trnsl.1.1.20160112T160751Z.931856e92a58d2f0.710111159f3a1b35285d8529a9beb1be4b069160"
lang = ["de", "ru", "es"]


for i in range(0, size-1):
    for j in range (0, len(lang)-1):
        url = baseUrl+"?key="+accessKey+"&text="+text[i]+"&lang="+lang[j]

data = json.load(urllib2.urlopen(url))

for key, value in data.items():
    print value