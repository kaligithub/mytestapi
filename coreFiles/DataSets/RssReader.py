# -*- coding: utf-8 -*-
import feedparser
import time
import re
from bs4 import BeautifulSoup
import datetime as dt
import urllib.request
from mytestapi.settings import PROJECT_DIR
from coreFiles.Utility import PayloadExtractor
from data_persistence.models import *

class RssReader:
    feed_name = 'RSS'
    db = PROJECT_DIR + '/coreFiles/DbFiles/rssReader.db'
    limit = 24 * 60 * 60
    posts_to_print = []
    posts_to_skip = []
    feedData = []
    i = 1
    current_time_millis = lambda: int(round(time.time() * 1000))
    current_timestamp = current_time_millis()
    today = dt.datetime.today().strftime("%Y-%d-%m")
    mapping = ""
    #data from database
    sources = ContentSource.objects.all()
    providers = ContentProvider.objects.all()
    categories = Categories.objects.all()
    entities = Entity.objects.all()
    filingType = RegulatorFilingType.objects.all()
    entityKeywords = Keywords.objects.all()
    
    def post_is_in_db(self,title):
        with open(self.db, 'r') as database:
            for line in database:
                if title in line:
                    return True
        return False
    
    def post_is_in_db_with_old_timestamp(self,title):
        with open(self.db, 'r') as database:
            for line in database:
                if title in line:
                    ts_as_string = line.split('|', 1)[1]
                    ts = float(ts_as_string)
                    if self.current_timestamp - ts > self.limit:
                        return True
        return False
    
    def dbInsertion(self):
        f = open(self.db, 'a')
        for item in self.posts_to_print:
            if not self.post_is_in_db(item):
                f.write(item + "|" + str(self.current_timestamp) + "\n")
        f.close

    def feedExtractor(self):
        for data in self.sources:
            for content in self.providers:
                if str(data.contentProvider) == str(content.contentProviderName):
                    if content.entity == None:
                        self.mapping = "notMapped"
                        break
                    else:
                        self.mapping = "mapped"
                        break
            try:    
                url = data.contentLocation
                feed = feedparser.parse(url)
                contentItemType = data.contentItemType
                contentID = content.contentProviderID
                
                if self.mapping == "notMapped":
                    if feed.bozo == 1:
                        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                        html = urllib.request.urlopen(req).read()
                        soup = BeautifulSoup(html, 'xml')
                        for item in soup.find_all('item'):
                            title = item.title.string
                            if self.post_is_in_db(title):
                                self.posts_to_skip.append(title)
                            else:
                                self.posts_to_print.append(title)
                                for keyword in self.entityKeywords:
                                    entityKeyword = str(keyword.keywordName)
                                    keywordID = keyword.id
                                    try:
                                        searchObj = False
                                        searchObj = re.search(entityKeyword.lower(),title.lower(),re.M|re.I)
                                    except:
                                        print("Exception")
                                    if searchObj:
                                        for category in self.categories:
                                            keyword = category.categoryName
                                            try:
                                                searchObj = False
                                                searchObj = re.search(keyword.lower(),title.lower(),re.M|re.I)
                                            except:
                                                print("Exception")
                                            if searchObj:
                                                entity = Entity.objects.filter(keywords__id = keywordID)
                                                contentItemURL = item.link.string
                                                contentTitle = item.title.string
                                                contentSummary = BeautifulSoup(item.description.string).text
                                                try:
                                                    contentDescription= PayloadExtractor.html_to_text(contentItemURL)
                                                except Exception as e:
                                                    print(e)
                                                contentSource = ContentSource.objects.filter(contentLocation = str(data.contentLocation))
                                                contentItemType = "News"
                                                contentType = "Text"
                                                channelType = "Feed-RSS"
                                                contentLocation = "URL"
                                                contentItemReceiveDate = self.today
                                                try:
                                                    contentItemPublishDate = item.published.string
                                                except:
                                                    contentItemPublishDate = self.today
                                                
                                                contentObj = ContentItem(contentItemType=contentItemType,contentType=contentType,
                                                                         channelType=channelType,contentLocation=contentLocation,
                                                                         contentSource=contentSource[0],contentItemReceiveDate=contentItemReceiveDate,
                                                                         contentItemPublishDate=contentItemPublishDate,contentItemURL=contentItemURL,
                                                                         contentSummary=contentSummary,contentDescription=contentDescription,contentTitle=contentTitle)
                                                contentObj.save() 
                                                
                                                contentObj.save() 
                                                contentItemObj = ContentItem.objects.get(pk=contentObj.pk)
                                                dataContentAssocObj = DataContentAssoc(contentItem=contentItemObj)   
                                                dataContentAssocObj.save()
                                                dataItemEntityObj = DataContentAssoc.objects.get(pk=dataContentAssocObj.pk)
                                                dataItemEntityAssocObj = DataItemEntityAssoc(dataItemID=dataItemEntityObj,entity=entity[0]) 
                                                dataItemEntityAssocObj.save()
                                                categoryObj = Categories.objects.filter(categoryName = str(keyword))
                                                keywordObj = Keywords.objects.filter(keywordName = str(entityKeyword))
                                                dataItemCategoryAssocObj = DataItemCategoryAssoc(dataItemID=dataItemEntityObj,keyword=keywordObj,categories=categoryObj)
                                                dataItemCategoryAssocObj.save()
                                        
                    else:
                        for post in feed.entries:
                            title = post.title
                            if self.post_is_in_db(title):
                                self.posts_to_skip.append(title)
                            else:
                                self.posts_to_print.append(title)
                                for keyword in self.entityKeywords:
                                    entityKeyword = str(keyword.keywordName) 
                                    keywordID = keyword.id
                                    try:
                                        searchObj = False
                                        searchObj = re.search(entityKeyword.lower(),title.lower(),re.M|re.I)
                                    except:
                                        print("Exception")
                                    if searchObj:
                                        for category in self.categories:
                                            keyword = category.categoryName
                                            try:
                                                searchObj = False
                                                searchObj = re.search(keyword.lower(),title.lower(),re.M|re.I)
                                            except:
                                                print("Exception")
                                            if searchObj:
                                                entity = Entity.objects.filter(keywords__id = keywordID)
                                                contentSource = ContentSource.objects.filter(contentLocation = str(data.contentLocation))
                                                contentItemType = "News"
                                                contentType = "Text"
                                                channelType = "Feed-RSS"
                                                contentLocation = "URL"
                                                contentItemReceiveDate = self.today
                                                contentItemPublishDate = self.today
                                                
                                                contentItemURL = post.link
                                                contentSummary = BeautifulSoup(post.description).text
                                                contentDescription = PayloadExtractor.html_to_text(contentItemURL)
                                                contentTitle = title
                                                
                                                contentObj = ContentItem(contentItemType=contentItemType,contentType=contentType,
                                                                         channelType=channelType,contentLocation=contentLocation,
                                                                         contentSource=contentSource[0],contentItemReceiveDate=contentItemReceiveDate,
                                                                         contentItemPublishDate=contentItemPublishDate,contentItemURL=contentItemURL,
                                                                         contentSummary=contentSummary,contentDescription=contentDescription,contentTitle=contentTitle)
                                                contentObj.save() 
                                                contentItemObj = ContentItem.objects.get(pk=contentObj.pk)
                                                dataContentAssocObj = DataContentAssoc(contentItem=contentItemObj)   
                                                dataContentAssocObj.save()
                                                dataItemEntityObj = DataContentAssoc.objects.get(pk=dataContentAssocObj.pk)
                                                dataItemEntityAssocObj = DataItemEntityAssoc(dataItemID=dataItemEntityObj,entity=entity[0]) 
                                                dataItemEntityAssocObj.save()  
                                                categoryObj = Categories.objects.filter(categoryName = str(keyword))[0]
                                                keywordObj = Keywords.objects.filter(keywordName = str(entityKeyword))[0]
                                                dataItemCategoryAssocObj = DataItemCategoryAssoc(dataItemID=dataContentAssocObj,keyword=keywordObj,categories=categoryObj)
                                                dataItemCategoryAssocObj.save()
                
                if self.mapping == "mapped":
                    contentItemType = "Regulatory Filing"
                    if str(contentItemType) == "Regulatory Filing":
                        regexp = "\d{7,10}"
                        cik = re.findall(regexp, url)
                        for post in feed.entries:
                            formType = post["filing-type"]
                            for filing in self.filingType:
                                fType = str(filing.regFilingType)
                                if formType == fType:
                                    formName = [x.replace(' ', '') for x in formType]
                                    formName = [x.replace('/', '') for x in formName]
                                    formName = ''.join(formName)
                                    title = post.title
                                    if self.post_is_in_db(title):
                                        self.posts_to_skip.append(title)
                                    else:
                                        self.posts_to_print.append(title)
                                        contentItemURL = post.link
                                        contentTitle = post.title
                                        contentDescription = BeautifulSoup(post.description).text
                                        contentSource = ContentSource.objects.filter(contentLocation = str(data.contentLocation))
                                        contentItemType = "News"
                                        contentType = "Text"
                                        channelType = "Feed-RSS"
                                        contentLocation = "URL"
                                        contentItemReceiveDate = self.today
                                        try:
                                            contentItemPublishDate = item.published.string
                                        except:
                                            contentItemPublishDate = self.today
                                        regEntity = Entity.objects.get(pk = (ContentProvider.objects.get(pk = contentID).entity_id))
                                        filingItemObj = FilingItem(regulatoryContentProviderID=content,regulatorFilingNumber=cik[0],
                                                                   regulatorFilingType=filing)
                                        filingItemObj.save()
                                        contentObj = ContentItem(contentItemType=contentItemType,contentType=contentType,
                                                                 channelType=channelType,contentLocation=contentLocation,
                                                                 contentSource=contentSource[0],contentItemReceiveDate=contentItemReceiveDate,
                                                                 contentItemPublishDate=contentItemPublishDate,contentItemURL=contentItemURL,
                                                                 contentDescription=contentDescription,contentTitle=contentTitle)
                                        contentObj.save() 
                                        contentItemObj = ContentItem.objects.get(pk=contentObj.pk)
                                        dataContentAssocObj = DataContentAssoc(contentItem=contentItemObj)   
                                        dataContentAssocObj.save()
                                        dataItemEntityObj = DataContentAssoc.objects.get(pk=dataContentAssocObj.pk)
                                        dataItemEntityAssocObj = DataItemEntityAssoc(dataItemID=dataItemEntityObj,entity=regEntity) 
                                        dataItemEntityAssocObj.save()
            except Exception as e:
                print(e)
                                                                                 
            print("Items processed:", self.i)
            self.i = self.i + 1

        self.dbInsertion()
        print('Process Finished')
