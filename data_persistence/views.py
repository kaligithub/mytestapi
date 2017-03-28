from django.http import HttpResponse
from data_persistence.models import *
from coreFiles.DataSets.RssReader import RssReader
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from mytestapi.settings import PROJECT_DIR
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from django.core import serializers
import re
import json
import os


def readconfig(request):
    configjson = open(os.path.join(PROJECT_DIR,'config.json'), 'r').read()
    return HttpResponse(configjson)

def keyword_extractor(request):
    filing = RssReader()
    filing.feedExtractor()
    return HttpResponse('OK')
    
@csrf_exempt    
def search(request):
    received_json_data = ((request.body).decode('utf-8'))
    decoded_json = json.loads(received_json_data)
    user_id = decoded_json['userId']
    searchText = decoded_json['qString']
    #searchText = "benzinga merger buy associate 424 and 14d1 of takeover BB&T BBT HomeTrust Bancshares american banker acqui news bank ally Citybank"
    stop = set(stopwords.words('english'))
    tokens = set([i for i in searchText.lower().split() if i not in stop])
    searchCategory = set()
    searchProvider = set()
    searchFilingType = set()
    searchKeyword = set()
    
    providers = ContentProvider.objects.all()
    categories = Categories.objects.all()
    filingType = RegulatorFilingType.objects.all()
    entityKeywords = Keywords.objects.all()
    
    for text in sorted(tokens):
        for keyword in categories:
            if re.search(text.lower(),keyword.categoryName.lower(),re.M|re.I) or re.search(keyword.categoryName.lower(),text.lower(),re.M|re.I):
                searchCategory.add(keyword.categoryName)
                break
        for provider in providers:
            if re.search(text.lower(),provider.contentProviderName.lower(),re.M|re.I):
                searchProvider.add(provider.contentProviderName)
                break
        for keyword in entityKeywords:
            if re.search(text.lower(),keyword.keywordName.lower(),re.M|re.I):
                searchKeyword.add(keyword.keywordName)
                break
        for fType in filingType:
            if re.search(text.lower(),fType.regFilingType.lower(),re.M|re.I):
                searchFilingType.add(fType.regFilingType)
                break
    
    #content provider sql
    whereList = []
    whereSql = ''
    for cp in searchProvider:
        whereList.append('content_provider.contentProviderName LIKE "%%{0}%%"'.format(cp))
    #category  name sql
    for cat in searchCategory:
        whereList.append('categories.categoryName LIKE "%%{0}%%"'.format(cat))
    #keyword name sql
    for key in searchKeyword:
        whereList.append('keywords.keywordName LIKE "%%{0}%%"'.format(key))

    whereSql += ' OR '.join(whereList) 
    
    where = ''
    if len(whereList) > 0:
        where = ' WHERE ' + whereSql

    
    raw_sql = '''SELECT data_content_assoc.dataItemID,
                    content_item.contentItemID,  
                    content_item.contentItemPublishDate,
                    content_item.contentItemURL, 
                    content_item.contentSummary, 
                    content_item.contentDescription, 
                    content_item.contentTitle,
                    content_provider.contentProviderID, 
                    content_provider.contentProviderName, 
                    categories.categoryName,
                    keywords.keywordName
                    FROM content_item 
                    INNER JOIN content_source ON (content_item.contentSource_id = content_source.contentSourceID) 
                    INNER JOIN content_provider ON (content_source.contentProvider_id = content_provider.contentProviderID)
                    INNER JOIN data_content_assoc ON (content_item.contentItemID = data_content_assoc.contentItem_id)
                    LEFT JOIN data_item_category_assoc ON (data_content_assoc.dataItemID = data_item_category_assoc.dataItemID_id)
                    LEFT JOIN categories ON (categories.categoryID = data_item_category_assoc.categories_id)
                    LEFT JOIN keywords ON (keywords.id = data_item_category_assoc.keyword_id)
            '''
    
    fullsql = raw_sql + where 
    #return HttpResponse(fullsql)

    jsondata = []
    try:
        fullsqlObj = ContentItem.objects.raw(fullsql)
    except Exception as err:
        return HttpResponse(err)
    
    for data in fullsqlObj:
        #return HttpResponse(data.categoryName)
        try:
            favoriteObj = UserFavorites.objects.get(users=user_id, dataContentAssoc=data.dataItemID)
        except UserFavorites.DoesNotExist:
            favoriteObj = None
        if favoriteObj is not None and favoriteObj.itemFavoriteStatus:
            user_fav = True
        else:
            user_fav = False    

    
        jsonObj = {
            "data_item_id":data.dataItemID,
            "url":data.contentItemURL,
            "title":data.contentTitle,
            "contentSummary":data.contentSummary,
            #"description":data.contentDescription,
            "category": data.categoryName,
            "content_provider": data.contentProviderName,
            "keywords": data.keywordName,
            "content_publishdate":data.contentItemPublishDate,
            "favorite":user_fav

        }
        jsondata.append(jsonObj)    
    
    return HttpResponse(json.dumps(jsondata))
    
@csrf_exempt    
def content_providerjson(request):
    received_json_data = ((request.body).decode('utf-8'))
    decoded_json = json.loads(received_json_data)
    
    user_id = decoded_json['user_id'][0]
    #user_id = 1
    jsondata = []
    try:
        contentItemObj = ContentItem.objects.select_related().all()
        #return HttpResponse(contentItemObj.query)
    except Exception as err:
        print(err)
    for data in contentItemObj:
        #return HttpResponse(data.contentItemID)
        try:
            dataContentAssocObj = DataContentAssoc.objects.get(contentItem=data.contentItemID)
        except DataContentAssoc.DoesNotExist:
            dataContentAssocObj = None
        if dataContentAssocObj is not None:
            try:
                favoriteObj = UserFavorites.objects.get(users=user_id, dataContentAssoc=dataContentAssocObj.dataItemID)
            except UserFavorites.DoesNotExist:
                favoriteObj = None
            if favoriteObj is not None and favoriteObj.itemFavoriteStatus:
                user_fav = True
            else:
                user_fav = False    
        
            try:        
                dataItemCatAssObj = DataItemCategoryAssoc.objects.get(dataItemID=dataContentAssocObj.dataItemID)
            except  DataItemCategoryAssoc.DoesNotExist:
                dataItemCatAssObj = None   
            if dataItemCatAssObj is not None:
                categoryObj = Categories.objects.get(pk = dataItemCatAssObj.categories_id)
                keywordsObj = Keywords.objects.get(pk = dataItemCatAssObj.keyword_id)
            
    
            jsonObj = {
                "data_item_id":dataContentAssocObj.dataItemID,
                "url":data.contentItemURL,
                "title":data.contentTitle,
                "contentSummary":data.contentSummary,
                #"description":data.contentDescription,
                "category": categoryObj.categoryName,
                "content_provider": data.contentSource.contentProvider.contentProviderName,
                "keywords": keywordsObj.keywordName,
                "content_publishdate":data.contentItemPublishDate,
                "favorite":user_fav
    
             }
            jsondata.append(jsonObj)
    
    return HttpResponse(json.dumps(jsondata))

@csrf_exempt
def favorite_status(request):
    received_json_data = ((request.body).decode('utf-8'))
    decoded_json = json.loads(received_json_data)
    
    data_item_id = decoded_json['data_item_id'][0]
    user_id = decoded_json['user_id'][0];
    
    try:
        favoriteObj = UserFavorites.objects.get(users=user_id,dataContentAssoc=data_item_id)
    except UserFavorites.DoesNotExist:
        favoriteObj = None
        
    if favoriteObj is not None and favoriteObj.itemFavoriteStatus:
        favorite = False
    else:
        favorite = True    
    
    obj, created = UserFavorites.objects.update_or_create(
        dataContentAssoc_id=data_item_id,
        users_id=user_id,
        defaults={'dataContentAssoc_id': data_item_id,'users_id':user_id,'itemFavoriteStatus':favorite},
    )
    return HttpResponse(json.dumps({"status":"ok","data_item_id":data_item_id,"favorite":favorite}))


@csrf_exempt   
def signup(request):
    
    return HttpResponse(json.dumps({"status":"ok"}))

    

@csrf_exempt   
def login(request):
    received_json_data = ((request.body).decode('utf-8'))
    decoded_json = json.loads(received_json_data)
    
    username = decoded_json['username']
    password = decoded_json['password']

    #username = 'admin'
    #password = 'incedo123'
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth_login(request, user)
        return HttpResponse(json.dumps({"userstatus":"success","user_id": request.user.id,"username": username}))
    else:
        return HttpResponse(json.dumps({"userstatus":"incorrect"}))
    

def logout(request):
    auth_logout(request)
    return HttpResponse(json.dumps({"status":"logout"}))

def get_allusers(request):
    users = serializers.serialize("json",User.objects.all())
    return HttpResponse(users)

@csrf_exempt   
def get_user_byid(request):
    received_json_data = ((request.body).decode('utf-8'))
    decoded_json = json.loads(received_json_data)
    
    id = decoded_json['id']

    users = serializers.serialize("json",User.objects.all().filter(id__exact=1))
    return HttpResponse(users)
