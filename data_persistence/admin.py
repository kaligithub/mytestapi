from django.contrib import admin
from .models import *

admin.site.register(Entity)
admin.site.register(ContentProvider)
admin.site.register(ContentSource)
admin.site.register(ContentItem)
admin.site.register(RegulatorFilingType)
admin.site.register(Keywords)
admin.site.register(Categories)
admin.site.register(ContentItemActivityType)
admin.site.register(EntityType)
admin.site.register(ChannelType)
admin.site.register(ContentItemType)
admin.site.register(ContentType)

admin.site.site_title = 'Data Automation Admin'
admin.site.site_header = 'Data Automation Admin'
