INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA14','Bank @ltantec','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA3','BB&T','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA22','Cabela\s Master Credit Card Trust ','Other');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA19','Capital Bank Financial Corp. ','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA21','Capital One Financial Corp.','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA6','Citizens National Bancorp','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA20','CommunityOne Bancorp','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA9','CVB Financial Corp.','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA8','DCB Financial Corp.','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA13','Dollar Bank','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA7','First Commonwealth','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA2','First Niagara Financial Group','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA24','GE Asset Management','Other');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA18','Georgetown Bancorp','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA11','HomeTrust Bancshares','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA1','KeyCorp','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA4','National Penn Bancshares','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA16','Progressive-Home Federal Savings and Loan Association','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA17','Salem Five Bancorp','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA5','Simmons First National Corporation ','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA23','State Street Corporation','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA12','TriSummit Bancorp ','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA10','Valley Commerce Bancorp','Bank');
INSERT INTO `entity`(`EntityID`, `EntityName`, `EntityType`) VALUES('MA90','Other','Bank');


INSERT INTO `content_provider`(`ContentProviderID`, `ContentProviderName`,`RelatedToEntityID_id`) VALUES (1,'Benzinga',1);
INSERT INTO `content_provider`(`ContentProviderID`, `ContentProviderName`,`RelatedToEntityID_id`) VALUES (2,'American Banker',2);
INSERT INTO `content_provider`(`ContentProviderID`, `ContentProviderName`,`RelatedToEntityID_id`) VALUES (3,'Efinancial News',3);
INSERT INTO `content_provider`(`ContentProviderID`, `ContentProviderName`,`RelatedToEntityID_id`) VALUES (4,'Seeking Alpha',4);
INSERT INTO `content_provider`(`ContentProviderID`, `ContentProviderName`,`RelatedToEntityID_id`) VALUES (5,'NYT',5);
INSERT INTO `content_provider`(`ContentProviderID`, `ContentProviderName`,`RelatedToEntityID_id`) VALUES (6,'Reuters',6);
INSERT INTO `content_provider`(`ContentProviderID`, `ContentProviderName`,`RelatedToEntityID_id`) VALUES (7,'Middle Market',7);


INSERT INTO `content_source`(`ContentSourceID`, `ContentProviderID_id`, `ChannelType`, `ContentLocation`) VALUES (1,1,'Feed-RSS','http://feeds.benzinga.com/benzinga/news/m-a');
INSERT INTO `content_source`(`ContentSourceID`, `ContentProviderID_id`, `ChannelType`, `ContentLocation`) VALUES (2,2,'Feed-RSS','http://www.americanbanker.com/resources/mergersacquisitions.xml');
INSERT INTO `content_source`(`ContentSourceID`, `ContentProviderID_id`, `ChannelType`, `ContentLocation`) VALUES (3,3,'Feed-RSS','http://www.efinancialnews.com/investmentbanking/mergers-and-acquisitions/rss');
INSERT INTO `content_source`(`ContentSourceID`, `ContentProviderID_id`, `ChannelType`, `ContentLocation`) VALUES (4,4,'Feed-RSS','http://seekingalpha.com/api/sa/combined/MTB.xml');
INSERT INTO `content_source`(`ContentSourceID`, `ContentProviderID_id`, `ChannelType`, `ContentLocation`) VALUES (5,5,'Feed-RSS','http://www.nytimes.com/services/xml/rss/nyt/Dealbook.xml');
INSERT INTO `content_source`(`ContentSourceID`, `ContentProviderID_id`, `ChannelType`, `ContentLocation`) VALUES (6,6,'Feed-RSS','http://feeds.reuters.com/reuters/mergersNews');
INSERT INTO `content_source`(`ContentSourceID`, `ContentProviderID_id`, `ChannelType`, `ContentLocation`) VALUES (7,7,'Feed-RSS','http://www.themiddlemarket.com/news/index.html?zkDo=showRSS');


INSERT INTO `content_item`(`ContentItemID`,`FromContentSourceID_id`, `ContentItemType`, `ContentType`, `ContentItemPublishDate`,`ContentItemURL`) VALUES (1, 1, 'NEWS', 'Text', 'Thu, 15 Dec 2016 19:22:31 +0000', 'http://www.americanbanker.com/news/dealmaking-strategy/cvb-financial-valley-commerce-in-calif-amend-merger-agreement-1092949-1.html');


INSERT INTO `regulator_filing_type`(`RegFilingTypeID`, `RegFilingType`) VALUES (1,'14d1');
INSERT INTO `regulator_filing_type`(`RegFilingTypeID`, `RegFilingType`) VALUES (2,'14d9');
INSERT INTO `regulator_filing_type`(`RegFilingTypeID`, `RegFilingType`) VALUES (3,'144');
INSERT INTO `regulator_filing_type`(`RegFilingTypeID`, `RegFilingType`) VALUES (4,'424');
INSERT INTO `regulator_filing_type`(`RegFilingTypeID`, `RegFilingType`) VALUES (5,'425');
INSERT INTO `regulator_filing_type`(`RegFilingTypeID`, `RegFilingType`) VALUES (6,'FWP');


INSERT INTO `data_content_assoc`(`DataItemID`, `ContentItemID_id`) VALUES (1,1);


INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00001','@lantec');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00002','BB&T');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00003','BBT');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00004','Cabela');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00005','Capital Bank');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00006','CBFC');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00007','Capital One');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00008','CapOne');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00009','Citizens National Bancorp');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00010','CommunityOne');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00011','CVB');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00012','CVB FC');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00013','DCB');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00014','DCB FC');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00015','Dollar Bank');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00016','First Commonwealth');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00017','First Niagara');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00018','FNFG');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00019','GE Asset Management');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00020','GEAM');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00021','Georgetown Bancorp');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00022','HomeTrust Bancshares');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00023','KeyCorp');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00024','National Penn Bancshares');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00025','Progressive-Home Federal Savings and Loan Association');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00026','Salem Five Bancorp');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00027','Simmons First National Corporation ');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00028','Simmons');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00029','StateStreet');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00030','STT');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00031','Trisummit');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00032','Valley Commerce');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00033','Bank');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00034','Bancorp');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00035','Bancshares');
INSERT INTO `keywords`(`KeywordID`, `KeywordName`) VALUES ('KEN00036','BHC');


INSERT INTO `categories`(`CategoryID`, `CategoryName`) VALUES (1,'M&A');
INSERT INTO `categories`(`CategoryID`, `CategoryName`) VALUES (2,'Reg Filing');
INSERT INTO `categories`(`CategoryID`, `CategoryName`) VALUES (3,'T&C');

INSERT INTO `content_item_activity_type`(`ContentItemActivityTypeID`, `ContentItemActivityType`) VALUES (1,'Filtering');
INSERT INTO `content_item_activity_type`(`ContentItemActivityTypeID`, `ContentItemActivityType`) VALUES (2,'Categorization');
INSERT INTO `content_item_activity_type`(`ContentItemActivityTypeID`, `ContentItemActivityType`) VALUES (3,'Extraction');
INSERT INTO `content_item_activity_type`(`ContentItemActivityTypeID`, `ContentItemActivityType`) VALUES (4,'QC');

INSERT INTO `entity_type`(`EntityTypeID`, `EntityType`) VALUES (1,'Company');
INSERT INTO `entity_type`(`EntityTypeID`, `EntityType`) VALUES (2,'Regulator');
INSERT INTO `entity_type`(`EntityTypeID`, `EntityType`) VALUES (3,'SRO');
INSERT INTO `entity_type`(`EntityTypeID`, `EntityType`) VALUES (4,'Trade Body');
INSERT INTO `entity_type`(`EntityTypeID`, `EntityType`) VALUES (5,'Other');
INSERT INTO `entity_type`(`EntityTypeID`, `EntityType`) VALUES (6,'Bank');

INSERT INTO `channel_type`(`ChannelTypeID`, `ChannelType`) VALUES (1,'Feed-ATOM');
INSERT INTO `channel_type`(`ChannelTypeID`, `ChannelType`) VALUES (2,'Feed-RSS');
INSERT INTO `channel_type`(`ChannelTypeID`, `ChannelType`) VALUES (3,'Email');
INSERT INTO `channel_type`(`ChannelTypeID`, `ChannelType`) VALUES (4,'Web');

INSERT INTO `content_item_type`(`ContentItemTypeID`, `ContentItemType`) VALUES (1,'News');
INSERT INTO `content_item_type`(`ContentItemTypeID`, `ContentItemType`) VALUES (2,'Press Release');
INSERT INTO `content_item_type`(`ContentItemTypeID`, `ContentItemType`) VALUES (3,'Regulatory Filing');
INSERT INTO `content_item_type`(`ContentItemTypeID`, `ContentItemType`) VALUES (4,'Opinion');
INSERT INTO `content_item_type`(`ContentItemTypeID`, `ContentItemType`) VALUES (5,'Other');

INSERT INTO `content_type`(`ContentTypeID`, `ContentType`) VALUES (1,'Text');
INSERT INTO `content_type`(`ContentTypeID`, `ContentType`) VALUES (2,'Audio');
INSERT INTO `content_type`(`ContentTypeID`, `ContentType`) VALUES (3,'Doc');
INSERT INTO `content_type`(`ContentTypeID`, `ContentType`) VALUES (4,'Video');
INSERT INTO `content_type`(`ContentTypeID`, `ContentType`) VALUES (5,'Other');







