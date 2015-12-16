import urllib
import xml.etree.ElementTree as ET


url = raw_input('Enter data-url: ')
print 'Retrieving: ', url

xmlh = urllib.urlopen(url)
data = xmlh.read()
print 'Retrieved',len(data),'characters'


tree = ET.fromstring(data)
lst = tree.findall("comments/comment")

count = 0
sum = 0
for item in lst : 
    cnt = item.find("count").text
    cnt = int(cnt)
    sum = sum + cnt
    count = count + 1

print "Count:", count
print "Sum: ", sum
    