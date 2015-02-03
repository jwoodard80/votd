__author__ = 'jonathan'

#Working release
import requests
from lxml import etree
import HTMLParser
import re

xml = etree.fromstring(requests.get("https://www.biblegateway.com/usage/votd/rss/votd.rdf?49").text)
verse = xml.xpath("/rss/channel/item/title")[0].text
scripture = xml.xpath("/rss/channel/item/content:encoded", namespaces=xml.nsmap)[0]
h = HTMLParser.HTMLParser()
scripture = re.sub(r"<br/>.*", '', h.unescape(scripture.text).strip())

print scripture
print "-- "+verse+" NASB"