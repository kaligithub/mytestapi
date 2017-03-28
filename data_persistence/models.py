from django.db import models
from django.contrib.auth.models import User

class Keywords(models.Model):
    id = models.AutoField(primary_key=True)
    keywordName = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.keywordName

    class Meta:
        db_table = 'keywords'
        verbose_name_plural = "keywords"

class Categories(models.Model):
    categoryID = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName

    class Meta:
        db_table = 'categories'
        verbose_name_plural = "categories"


class EntityType(models.Model):
    entityTypeID = models.AutoField(primary_key=True)

    EntityType_CHOICES = (
        (u'Company', u'Company'),
        (u'Regulator', u'Regulator'),
        (u'SRO', u'SRO'),
        (u'Trade Body', u'Trade Body'),
        (u'Other', u'Other'),
        (u'Bank', u'Bank')
    )
    entityType = models.CharField(max_length=50, choices=EntityType_CHOICES)

    def __str__(self):
        return self.entityType

    class Meta:
        db_table = 'entity_type'

class ContentType(models.Model):
    contentTypeID = models.AutoField(primary_key=True)
    ContentType_CHOICES = (
        (u'Text', u'Text'),
        (u'Audio', u'Audio'),
        (u'Doc', u'Doc'),
        (u'Video', u'Video'),
        (u'Other', u'Other')
    )
    contentType = models.CharField(max_length=50, choices=ContentType_CHOICES)

    class Meta:
        db_table = 'content_type'

class ChannelType(models.Model):
    channelTypeID = models.AutoField(primary_key=True)
    ChannelType_CHOICES = (
        (u'Feed-ATOM', u'Feed-ATOM'),
        (u'Feed-RSS', u'Feed-RSS'),
        (u'Email', u'Email'),
        (u'Web', u'Web')
    )
    channelType = models.CharField(max_length=50, choices=ChannelType_CHOICES)

    class Meta:
        db_table = 'channel_type'


class ContentItemType(models.Model):
    contentItemTypeID = models.AutoField(primary_key=True)
    ContentItemType_CHOICES = (
        (u'News', u'News'),
        (u'Press Release', u'Press Release'),
        (u'Regulatory Filing', u'Regulatory Filing'),
        (u'Opinion', u'Opinion'),
        (u'Other', u'Other')
    )
    contentItemType = models.CharField(max_length=50, choices=ContentItemType_CHOICES)
    
    def __str__(self):
        return self.contentItemType
    
    class Meta:
        db_table = 'content_item_type'

class Entity(models.Model):
    id = models.AutoField(primary_key=True)
    entityName = models.CharField(max_length=50,null=True)
    keywords = models.ManyToManyField(Keywords, blank=True, null=True)
    category = models.ManyToManyField(Categories, blank=True, null=True)

    entityType = models.ForeignKey(EntityType)
    hasParent = models.NullBooleanField(blank=True)
    parentEntityID = models.IntegerField(default=0, blank=True, null=True)
    parentEntityName = models.CharField(max_length=50,blank=True, null=True)
    isTracked = models.NullBooleanField(blank=True)
    trackStartDate = models.DateField(null=True,blank=True)
    trackEndDate = models.DateField(null=True,blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.entityName


    class Meta:
        db_table = 'entity'


class ContentProvider(models.Model):
    contentProviderID = models.AutoField(primary_key=True)
    contentProviderName = models.CharField(max_length=50,null=True)
    entity = models.ForeignKey(Entity,blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.contentProviderName

    class Meta:
        db_table = 'content_provider'


class ContentSource(models.Model):
    contentSourceID = models.AutoField(primary_key=True)
    contentProvider = models.ForeignKey(ContentProvider)

    ChannelType_CHOICES = (
        (u'Feed-ATOM', u'Feed-ATOM'),
        (u'Feed-RSS', u'Feed-RSS'),
        (u'Email', u'Email'),
        (u'Web', u'Web')
    )
    channelType = models.CharField(max_length=50, choices=ChannelType_CHOICES)
    contentItemType = models.ForeignKey(ContentItemType,blank=True, null=True)
    contentLocation = models.CharField(max_length=100)
    isTracked = models.NullBooleanField(blank=True, null=True)
    trackStartDate = models.DateField(null=True, blank=True)
    trackEndDate = models.DateField(null=True, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.contentLocation

    class Meta:
        db_table = 'content_source'

class ContentItem(models.Model):
    contentItemID = models.AutoField(primary_key=True)
    ContentItemType_CHOICES = (
        (u'News', u'News'),
        (u'Press Release', u'Press Release'),
        (u'Regulatory Filing', u'Regulatory Filing'),
        (u'Opinion', u'Opinion'),
        (u'Other', u'Other')
    )
    contentItemType = models.CharField(max_length=50, choices=ContentItemType_CHOICES)

    ContentType_CHOICES = (
        (u'Text', u'Text'),
        (u'Audio', u'Audio'),
        (u'Doc', u'Doc'),
        (u'Video', u'Video'),
        (u'Other', u'Other')

    )
    contentType = models.CharField(max_length=50, choices=ContentType_CHOICES)

    ChannelType_CHOICES = (
        (u'Feed-ATOM', u'Feed-ATOM'),
        (u'Feed-RSS', u'Feed-RSS'),
        (u'Email', u'Email'),
        (u'Web', u'Web')
    )
    channelType = models.CharField(max_length=50, null=True, choices=ChannelType_CHOICES)
    contentLocation = models.CharField(max_length=254,null=True)
    contentSource = models.ForeignKey(ContentSource)
    contentItemReceiveDate = models.CharField(max_length=50,blank=True,null=True)
    contentItemPublishDate = models.CharField(max_length=50,blank=True,null=True)
    contentItemUniqueID = models.IntegerField(default=0, blank=True, null=True)
    contentItemURL = models.CharField(max_length=254, blank=True, null=True)
    contentSummary = models.TextField(null=True, blank=True)
    contentDescription = models.TextField(null=True)
    contentAttachment = models.BinaryField(null=True)
    contentTitle = models.CharField(max_length=254,null=True)


    class Meta:
        db_table = 'content_item'


class RegulatorFilingType(models.Model):
    regFilingTypeID = models.AutoField(primary_key=True)
    regFilingType = models.CharField(max_length=50,null=True)

    class Meta:
        db_table = 'regulator_filing_type'



class FilingItem(models.Model):
    contentItemID = models.AutoField(primary_key=True)
    regulatoryContentProviderID = models.ForeignKey(ContentProvider)
    regContentProviderName = models.CharField(max_length=50,null=True)
    regulatorFilingNumber = models.CharField(max_length=50,null=True)
    regulatorFilingType = models.ForeignKey(RegulatorFilingType)

    class Meta:
        db_table = 'filing_item'



class ContentPayload(models.Model):
    contentItemID = models.AutoField(primary_key=True)
    contentPayload = models.TextField(null=True)

    class Meta:
        db_table = 'content_payload'


class DataContentAssoc(models.Model):
    dataItemID = models.AutoField(primary_key=True)
    contentItem = models.ForeignKey(ContentItem)

    class Meta:
        db_table = 'data_content_assoc'

class DataItemEntityAssoc(models.Model):
    dataItemID = models.ForeignKey(DataContentAssoc)
    entity = models.ForeignKey(Entity)

    class Meta:
        db_table = 'data_item_entity_assoc'

class DataItemCategoryAssoc(models.Model):
    dataItemID = models.ForeignKey(DataContentAssoc)
    keyword = models.ForeignKey(Keywords)
    categories = models.ForeignKey(Categories)

    class Meta:
        db_table = 'data_item_category_assoc'


class ContentItemActivityType(models.Model):
    contentItemActivityTypeID = models.AutoField(primary_key=True)
    ContentItemActivityType_CHOICES = (
        (u'Filtering', u'Filtering'),
        (u'Categorization', u'Categorization'),
        (u'Extraction', u'Extraction'),
        (u'QC', u'QC')
    )
    contentItemActivityType = models.CharField(max_length=50,null=True, choices=ContentItemActivityType_CHOICES)

    class Meta:
        db_table = 'content_item_activity_type'

class ContentItemHistory(models.Model):
    contentItemID = models.AutoField(primary_key=True)
    contentItemActivityType = models.ForeignKey(ContentItemActivityType)
    contentItemActivityDate = models.DateField(null=True)
    contentItemActivityActor = models.IntegerField(default=0,null=True,blank=True)

    class Meta:
        db_table = 'content_item_history'

'''class Users(models.Model):
    userID = models.AutoField(primary_key=True)
    password = models.CharField(max_length=20)
    userFirstName = models.CharField(max_length=50,null=True)
    userLastName = models.CharField(max_length=50,null=True)
    userEmail = models.EmailField()

    class Meta:
        db_table = 'users'''

class UserWatchlist(models.Model):
    watchlistID = models.AutoField(primary_key=True)
    watchlistName = models.CharField(max_length=50,null=True)
    users = models.ForeignKey(User)
    isActive = models.BooleanField()
    wLActiveStartDate = models.DateField()
    wLActiveEndDate = models.DateField()

    class Meta:
        db_table = 'user_watchlist'

class UserWatchlistDetails(models.Model):
    id = models.AutoField(primary_key=True)
    userWatchlist = models.ForeignKey(UserWatchlist)
    users = models.ForeignKey(User)
    keywords = models.ForeignKey(Keywords)
    keywordName = models.CharField(max_length=50)
    categories = models.ForeignKey(Categories)
    entity = models.ForeignKey(Entity)

    class Meta:
        db_table = 'user_watchlist_details'

class UserFavorites(models.Model):
    dataContentAssoc = models.ForeignKey(DataContentAssoc)
    users = models.ForeignKey(User)
    itemFavoriteStatus = models.BooleanField()

    class Meta:
        db_table = 'user_favorites'