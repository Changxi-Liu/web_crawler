#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import cookielib 
from bs4 import BeautifulSoup
import requests
import urllib2

import urllib
url = 'https://sparse.tamu.edu/MM/'
print('Before Open')
cookie = cookielib.CookieJar()
header={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36'}
values = {'name' : 'lcx',
          'location' : 'BeiJing',
          'language' : 'Python' }
def get_data(url_arg):

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    urllib2.install_opener(opener)
#    data = urllib.urlencode(values)
    request = urllib2.Request(url=url_arg, headers = header)
    response1 = urllib2.urlopen(request)
    html_doc =  (response1.read())
    return html_doc
html_doc = get_data( url )

print('Read Completed')
#(response1.getcode())
soup = BeautifulSoup(html_doc,"html.parser",from_encoding="utf-8")


pattern = re.compile("[a-zA-Z\-0-9_]+/$")

pattern2 = re.compile("[a-zA-Z\-0-9_]+\.tar\.gz$")
links = soup.find_all('a')
#print(links)
file_name = open("log.txt",'w')
for link in links:
    folder = link['href']
    print(folder)
    if(pattern.match(folder) != None):
        url_new = url + folder
        html_new = get_data( url_new )
        soup_new = BeautifulSoup( html_new,"html.parser",from_encoding="utf-8" )
        links_new = soup_new.find_all('a')
        for link_new in links_new:
            folder_new = link_new['href']
            if(pattern2.match(folder_new)!=None):
                print(url_new+folder_new)
                file_name.write(url_new+folder_new+"\n")
file_name.close()
