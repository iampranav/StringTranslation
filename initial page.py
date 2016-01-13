import json, urllib2

fl = open("/home/pranav/Downloads/strings.xml", "r")
lines = fl.readlines()
size = len(lines)
infile = []
j = 0

for i in range(0, size-1):
    for item in lines[i].split("</string>"):
        if '\">' in item:
            var = item[item.find("\">") + len("\">"):]
            infile.append(var)

baseUrl = "https://translate.yandex.net/api/v1.5/tr.json/translate"
accessKey = "trnsl.1.1.20160112T160751Z.931856e92a58d2f0.710111159f3a1b35285d8529a9beb1be4b069160"
lang = ["de", "ru", "es"]


for k in range(0, len(infile)-1):
    for l in range(0, len(lang)-1):
        url = baseUrl+"?key="+accessKey+"&text="+infile[k]+"&lang="+lang[l]
        data = json.load(urllib2.urlopen(url))

        for key, value in data.items():
            if key == 'text':
                print value[0]
