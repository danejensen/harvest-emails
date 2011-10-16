import urllib2
import re

f = open('/home/rhett/Desktop/designblogs.txt','r')
for line in f:
  try:
    http = line[:-1] + "contact"
    request = urllib2.urlopen(http)
    html = request.read()
    email = re.search('[A-Za-z0-9\._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}', html)
    print email.group(0)
    #print html
  except:
    print 'a error'
