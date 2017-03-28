from readability.readability import Document
from bs4 import BeautifulSoup
import re
import urllib.request
url = 'http://feeds.benzinga.com/~r/benzinga/news/m-a/~3/x3PSBMiWXzI/mid-day-market-update-naked-brand-gains-on-merger-news-uranium-resources'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = str(urllib.request.urlopen(req).read())
readable_article = Document(html).summary()
print(re.sub("\n","",BeautifulSoup(readable_article).text))

#readable_title = Document(html).short_title()
#print(readable_title)