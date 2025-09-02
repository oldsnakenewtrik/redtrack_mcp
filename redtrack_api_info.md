[![Swagger UI](<Base64-Image-Removed>)swagger](https://api.redtrack.io/docs/index.html#) Explore

## Redtrack API  ```  latest  ```

```
[ Base URL: api.redtrack.io/ ]
```

[doc.json](about:blank)

Schemeshttpshttp

#### Dictionaries

GET/browser\_fullnames

Browsers names list

GET/browsers

Browsers list

GET/categories

Categories list

GET/cities

Cities list

GET/connection\_types

Connection types list

GET/countries

Countries list

GET/currencies

Currencies list

GET/device\_brands

Device brands list

GET/device\_fullnames

Device names list

GET/devices

Devices list

GET/isp

ISP list

GET/languages

Languages list

GET/os

OS list

GET/os\_fullnames

OS names list

GET/proxy\_types

Proxy types list

GET/regions

Regions list

GET/timezones

Timezones list

#### Campaigns

POST/campaigns

Create campaign

PUT/campaigns/{id}

Update campaign

#### Logs

GET/conversions

Get conversions log

POST/conversions

Upload conversions

GET/conversions/export

Get conversions log

POST/export\_conversions

Export conversions to aws s3

POST/export\_tracks

Export clicks to aws s3

GET/tracks

Get clicks log

#### Domains

GET/domains

Get domains

POST/domains

Create domain

POST/domains/regenerated\_free\_ssl/{id}

Regenerated free SSL

PUT/domains/{id}

Update domain

DELETE/domains/{id}

Delete domain

#### Settings

GET/me/settings

Get user settings

PUT/me/settings

Update user settings

#### Offers

POST/offers

Create offer

GET/offers/export

Export offers to aws s3

PUT/offers/{id}

Update offer

#### WhiteLabel

POST/pub/auth

Publisher auth

GET/pub/campaigns

Publisher campaigns

GET/pub/me

Publisher info

GET/pub/payments

Publisher payments

POST/pub/payments

Request payment

PUT/pub/payments/{id}

Update payment

POST/pub/postbacks

Publisher conversions

PUT/pub/profile

Update publisher info

POST/pub/publishers

Signup

GET/pub/reports/traffic

Publisher stat

POST/pub/reset\_password

Reset password

GET/pub/settings

Whitelabel settings

#### Publishers

GET/pub/referrals

Get participants of referral program

GET/publishers/export

Export publishers to aws s3

GET/publishers/referral

Get participants of referral program

PUT/publishers/{id}

Update publisher info

#### Reports

GET/report

Report

POST/tracks/cost

Update costs

#### Scripts

GET/scripts

Get tracking scripts

POST/scripts

Create script

GET/scripts/{id}

Get tracking script

PUT/scripts/{id}

Update script

DELETE/scripts/{id}

Delete script

#### Streams

POST/streams

Create stream

PUT/streams/{id}

Update stream

DELETE/streams/{id}

Delete stream

#### Models

#/definitions/api.Errapi.Err{

|     |     |
| --- | --- |
| error | string |

}

#/definitions/client.ConversionUploadRequestclient.ConversionUploadRequest{

|     |     |
| --- | --- |
| campaign\_id | string |
| clickid | string |
| created\_at | string |
| payout | number |
| type | string |

}

#/definitions/emptypb.Emptyemptypb.Empty{

|
|

}

#/definitions/forms.PubPostbacksLogsFormforms.PubPostbacksLogsForm{

|     |     |
| --- | --- |
| campaign\_ids | \[string\] |
| date\_from | string |
| date\_to | string |
| page | integer |
| per | integer |
| publisher\_ids | \[string\] |
| time\_interval | string |

}

#/definitions/gin.Hgin.H{

|
|

}

#/definitions/models.Browsermodels.Browser{

|     |     |
| --- | --- |
| id | string |
| title | string |

}

#/definitions/models.BrowserFullNamemodels.BrowserFullName{

|     |     |
| --- | --- |
| title | string |

}

#/definitions/models.Campaignmodels.Campaign{

|     |     |
| --- | --- |
| cache\_buster\_enabled | boolean |
| cost\_model | string |
| coupon | string |
| cpc | number |
| created\_at | string |
| creatives | \[#/definitions/models.Creativemodels.Creative{\
\
|     |     |\
| --- | --- |\
| description | string |\
| image\_url | string |\
| title | string |\
\
}\] |
| custom\_conv\_type\_conv\_subs\_geo\_payouts | \[#/definitions/models.CustomConvTypeConvSubsGeoPayoutsmodels.CustomConvTypeConvSubsGeoPayouts{\
\
|     |     |\
| --- | --- |\
| conversion\_type | string |\
| country | string |\
| sub | string |\
| sub\_value | string |\
| value | number |\
\
}\] |
| custom\_conv\_type\_conv\_subs\_payouts | \[#/definitions/models.CustomConvTypeConvSubsPayoutsmodels.CustomConvTypeConvSubsPayouts{\
\
|     |     |\
| --- | --- |\
| conversion\_type | string |\
| sub | string |\
| sub\_value | string |\
| value | number |\
\
}\] |
| custom\_conv\_type\_geo\_payouts | \[#/definitions/models.CustomConvTypeGeoPayoutsmodels.CustomConvTypeGeoPayouts{\
\
|     |     |\
| --- | --- |\
| conversion\_type | string |\
| country | string |\
| value | number |\
\
}\] |
| custom\_conversion\_subs\_payouts | \[#/definitions/models.CustomConversionSubsPayoutmodels.CustomConversionSubsPayout{\
\
|     |     |\
| --- | --- |\
| sub | string |\
| sub\_value | string |\
| value | number |\
\
}\] |
| custom\_conversion\_type\_payouts | \[#/definitions/models.CustomConversionTypePayoutmodels.CustomConversionTypePayout{\
\
|     |     |\
| --- | --- |\
| conversion\_type | string |\
| value | number |\
\
}\] |
| custom\_geo\_os\_payouts | \[#/definitions/models.CustomGeoOsPayoutmodels.CustomGeoOsPayout{\
\
|     |     |\
| --- | --- |\
| country | string |\
| os | string |\
| value | number |\
\
}\] |
| custom\_geo\_payouts | \[#/definitions/models.CustomGeoPayoutmodels.CustomGeoPayout{\
\
|     |     |\
| --- | --- |\
| country | string |\
| value | number |\
\
}\] |
| custom\_pub\_payouts | \[#/definitions/models.CustomPubPayoutmodels.CustomPubPayout{\
\
|     |     |\
| --- | --- |\
| publisher | string |\
| value | number |\
\
}\] |
| custom\_pub\_sub\_geo\_payouts | \[#/definitions/models.CustomPubSubGeoPayoutmodels.CustomPubSubGeoPayout{\
\
|     |     |\
| --- | --- |\
| country | string |\
| publisher | string |\
| sub | string |\
| sub\_value | string |\
| value | number |\
\
}\] |
| custom\_pub\_sub\_payouts | \[#/definitions/models.CustomPubSubPayoutmodels.CustomPubSubPayout{\
\
|     |     |\
| --- | --- |\
| publisher | string |\
| sub | string |\
| sub\_value | string |\
| value | number |\
\
}\] |
| custom\_pub\_sub\_throttles | \[#/definitions/models.CustomPubSubThrottlemodels.CustomPubSubThrottle{\
\
|     |     |\
| --- | --- |\
| publisher | string |\
| status | string |\
| sub | string |\
| sub\_value | string |\
| value | integer |\
\
}\] |
| custom\_pub\_throttles | \[#/definitions/models.CustomPubThrottlemodels.CustomPubThrottle{\
\
|     |     |\
| --- | --- |\
| publisher | string |\
| status | string |\
| value | integer |\
\
}\] |
| custom\_throttles | \[#/definitions/models.CustomThrottlemodels.CustomThrottle{\
\
|     |     |\
| --- | --- |\
| status | string |\
| value | integer |\
\
}\] |
| custom\_type\_payouts | \[#/definitions/models.CustomTypePayoutmodels.CustomTypePayout{\
\
|     |     |\
| --- | --- |\
| type | string |\
| value | number |\
\
}\] |
| domain\_id | string |
| expires\_at | string |
| id | string |
| impression\_postbacks | \[#/definitions/models.URLPostbackmodels.URLPostback{\
\
|     |     |\
| --- | --- |\
| url | string |\
\
}\] |
| impression\_url | string |
| integration\_postback | #/definitions/models.ConversionPostbackmodels.ConversionPostback{

|     |     |
| --- | --- |
| events | \[<br>deprecated<br>string\] |
| goals | \[string\] |
| json\_body | string |
| match\_event | boolean |
| payment\_percent | number |
| request\_method | integer |
| statuses | \[string\] |
| url | string |

} |
| integrations | #/definitions/models.CampaignIntegrationsmodels.CampaignIntegrations{

|     |     |
| --- | --- |
| cost\_update | boolean |
| fraudscore | boolean<br>is used for validating clicks |

} |
| notes | \[string\] |
| notifications | #/definitions/models.CampaignNotificationsmodels.CampaignNotifications{

|     |     |
| --- | --- |
| clicks | integer |
| condition | string |
| conversions | integer |
| enabled | boolean |
| roi | number |

} |
| pixels | \[#/definitions/models.ConversionPostbackmodels.ConversionPostback{\
\
|     |     |\
| --- | --- |\
| events | \[<br>deprecated<br>string\] |\
| goals | \[string\] |\
| json\_body | string |\
| match\_event | boolean |\
| payment\_percent | number |\
| request\_method | integer |\
| statuses | \[string\] |\
| url | string |\
\
}\] |
| postback\_url | string |
| postbacks | \[#/definitions/models.ConversionPostbackmodels.ConversionPostback{\
\
|     |     |\
| --- | --- |\
| events | \[<br>deprecated<br>string\] |\
| goals | \[string\] |\
| json\_body | string |\
| match\_event | boolean |\
| payment\_percent | number |\
| request\_method | integer |\
| statuses | \[string\] |\
| url | string |\
\
}\] |
| publisher\_details | #/definitions/models.PublisherDetailsmodels.PublisherDetails{

|     |     |
| --- | --- |
| advertiser | string |
| campaign\_rate | #/definitions/models.CampaignRatemodels.CampaignRate{

|     |     |
| --- | --- |
| status | integer |
| value | number |

} |
| campaign\_type | string |
| categories | \[string\] |
| countries | \[string\] |
| coupon | string |
| deeplinks | \[#/definitions/models.Deeplinkmodels.Deeplink{\
\
|     |     |\
| --- | --- |\
| active\_direct | boolean |\
| active\_impression | boolean |\
| active\_redirect | boolean |\
| direct\_url | string |\
| impression\_url | string |\
| link | string |\
| name | string |\
| redirect\_url | string |\
\
}\] |
| description | string |
| domain | string |
| hide\_deeplinks | boolean<br>HideDeeplinks shows what we need to hide deeplinks section |
| hide\_direct\_tracking\_urls | boolean<br>HideDirectTrackingURLs shows what we need to hide direct tracking urls section |
| hide\_payout\_details | boolean |
| hide\_redirect\_impression\_url | boolean<br>HideRedirectImpressionURL shows what we need to hide redirect impression url section |
| hide\_redirect\_tracking\_url | boolean<br>HideRedirectTrackingURL shows what we need to hide redirect tracking url section |
| os | \[string\] |
| preview | string |
| preview\_url | string |
| sources | \[string\] |

} |
| redirect\_type | integer |
| rev\_share | number<br>for CPA payout model, this is PERCENT of revenue to publisher |
| rsoc\_enabled | boolean |
| serial\_number | integer |
| source\_campaign\_id | string<br>deprecated |
| source\_campaigns | \[string\] |
| source\_id | string |
| source\_title | string |
| stat | #/definitions/models.Statmodels.Stat{

|
|

} |
| status | integer |
| streams | \[#/definitions/models.CampaignStreammodels.CampaignStream{\
\
|     |     |\
| --- | --- |\
| id | string |\
| optimization | #/definitions/models.StreamOptimizationmodels.StreamOptimization{\
\
|     |     |\
| --- | --- |\
| clicks\_limit | integer |\
| conversion\_types | \[string\] |\
| count | integer |\
| is\_enabled | boolean |\
| limit | integer |\
| metric | string |\
| multiplicator | number |\
| subs | \[string\] |\
| threshold | number |\
| winner\_share\_limit | integer |\
\
} |\
| stream | #/definitions/models.Streammodels.Stream{\
\
|     |     |\
| --- | --- |\
| expires\_at | string |\
| filters | #/definitions/models.Filtersmodels.Filters{\
\
|     |     |\
| --- | --- |\
| browser | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| browser\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| city | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| connection\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| country | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_brand | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_model | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_type | #/definitions/models.DeviceTypeFiltermodels.DeviceTypeFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| domain\_referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| fraud | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| ip | #/definitions/models.IPFiltermodels.IPFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| isp | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| languages | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| proxy\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| region | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| subs | #/definitions/models.SubsFiltermodels.SubsFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| items | #/definitions/models.SubItemsmodels.SubItems{\
\
|     |     |\
| --- | --- |\
| sub1 | string |\
| sub10 | string |\
| sub11 | string |\
| sub12 | string |\
| sub13 | string |\
| sub14 | string |\
| sub15 | string |\
| sub16 | string |\
| sub17 | string |\
| sub18 | string |\
| sub19 | string |\
| sub2 | string |\
| sub20 | string |\
| sub3 | string |\
| sub4 | string |\
| sub5 | string |\
| sub6 | string |\
| sub7 | string |\
| sub8 | string |\
| sub9 | string |\
\
} |\
| kind | integer |\
\
} |\
| unique\_visitor | #/definitions/models.UniqueVisitorFiltermodels.UniqueVisitorFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
\
} |\
\
} |\
| id | string |\
| landings | \[#/definitions/models.StreamLandingmodels.StreamLanding{\
\
|     |     |\
| --- | --- |\
| filters | #/definitions/models.Filtersmodels.Filters{\
\
|     |     |\
| --- | --- |\
| browser | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| browser\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| city | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| connection\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| country | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_brand | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_model | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_type | #/definitions/models.DeviceTypeFiltermodels.DeviceTypeFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| domain\_referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| fraud | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| ip | #/definitions/models.IPFiltermodels.IPFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| isp | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| languages | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| proxy\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| region | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| subs | #/definitions/models.SubsFiltermodels.SubsFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| items | #/definitions/models.SubItemsmodels.SubItems{\
\
|     |     |\
| --- | --- |\
| sub1 | string |\
| sub10 | string |\
| sub11 | string |\
| sub12 | string |\
| sub13 | string |\
| sub14 | string |\
| sub15 | string |\
| sub16 | string |\
| sub17 | string |\
| sub18 | string |\
| sub19 | string |\
| sub2 | string |\
| sub20 | string |\
| sub3 | string |\
| sub4 | string |\
| sub5 | string |\
| sub6 | string |\
| sub7 | string |\
| sub8 | string |\
| sub9 | string |\
\
} |\
| kind | integer |\
\
} |\
| unique\_visitor | #/definitions/models.UniqueVisitorFiltermodels.UniqueVisitorFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
\
} |\
\
} |\
| id | string |\
| name | string |\
| weight | integer |\
\
}\] |\
| offers | \[#/definitions/models.StreamOffermodels.StreamOffer{\
\
|     |     |\
| --- | --- |\
| filters | #/definitions/models.Filtersmodels.Filters{\
\
|     |     |\
| --- | --- |\
| browser | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| browser\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| city | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| connection\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| country | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_brand | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_model | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_type | #/definitions/models.DeviceTypeFiltermodels.DeviceTypeFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| domain\_referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| fraud | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| ip | #/definitions/models.IPFiltermodels.IPFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| isp | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| languages | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| proxy\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| region | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| subs | #/definitions/models.SubsFiltermodels.SubsFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| items | #/definitions/models.SubItemsmodels.SubItems{\
\
|     |     |\
| --- | --- |\
| sub1 | string |\
| sub10 | string |\
| sub11 | string |\
| sub12 | string |\
| sub13 | string |\
| sub14 | string |\
| sub15 | string |\
| sub16 | string |\
| sub17 | string |\
| sub18 | string |\
| sub19 | string |\
| sub2 | string |\
| sub20 | string |\
| sub3 | string |\
| sub4 | string |\
| sub5 | string |\
| sub6 | string |\
| sub7 | string |\
| sub8 | string |\
| sub9 | string |\
\
} |\
| kind | integer |\
\
} |\
| unique\_visitor | #/definitions/models.UniqueVisitorFiltermodels.UniqueVisitorFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
\
} |\
\
} |\
| id | string |\
| name | string |\
| weight | integer |\
\
}\] |\
| prelandings | \[#/definitions/models.StreamLandingmodels.StreamLanding{\
\
|     |     |\
| --- | --- |\
| filters | #/definitions/models.Filtersmodels.Filters{\
\
|     |     |\
| --- | --- |\
| browser | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| browser\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| city | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| connection\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| country | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_brand | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_model | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_type | #/definitions/models.DeviceTypeFiltermodels.DeviceTypeFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| domain\_referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| fraud | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| ip | #/definitions/models.IPFiltermodels.IPFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| isp | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| languages | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| proxy\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| region | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| subs | #/definitions/models.SubsFiltermodels.SubsFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| items | #/definitions/models.SubItemsmodels.SubItems{\
\
|     |     |\
| --- | --- |\
| sub1 | string |\
| sub10 | string |\
| sub11 | string |\
| sub12 | string |\
| sub13 | string |\
| sub14 | string |\
| sub15 | string |\
| sub16 | string |\
| sub17 | string |\
| sub18 | string |\
| sub19 | string |\
| sub2 | string |\
| sub20 | string |\
| sub3 | string |\
| sub4 | string |\
| sub5 | string |\
| sub6 | string |\
| sub7 | string |\
| sub8 | string |\
| sub9 | string |\
\
} |\
| kind | integer |\
\
} |\
| unique\_visitor | #/definitions/models.UniqueVisitorFiltermodels.UniqueVisitorFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
\
} |\
\
} |\
| id | string |\
| name | string |\
| weight | integer |\
\
}\] |\
| template | boolean |\
| title | string |\
| user\_id | string |\
\
} |\
| weight | integer |\
\
}\] |
| tags | \[string\] |
| title | string |
| trackback\_url | string |
| type | string |
| updated\_at | string |
| user\_id | string |

}

#/definitions/models.CampaignIntegrationsmodels.CampaignIntegrations{

|     |     |
| --- | --- |
| cost\_update | boolean |
| fraudscore | boolean<br>is used for validating clicks |

}

#/definitions/models.CampaignNotificationsmodels.CampaignNotifications{

|     |     |
| --- | --- |
| clicks | integer |
| condition | string |
| conversions | integer |
| enabled | boolean |
| roi | number |

}

#/definitions/models.CampaignRatemodels.CampaignRate{

|     |     |
| --- | --- |
| status | integer |
| value | number |

}

#/definitions/models.CampaignStreammodels.CampaignStream{

|     |     |
| --- | --- |
| id | string |
| optimization | #/definitions/models.StreamOptimizationmodels.StreamOptimization{

|     |     |
| --- | --- |
| clicks\_limit | integer |
| conversion\_types | \[string\] |
| count | integer |
| is\_enabled | boolean |
| limit | integer |
| metric | string |
| multiplicator | number |
| subs | \[string\] |
| threshold | number |
| winner\_share\_limit | integer |

} |
| stream | #/definitions/models.Streammodels.Stream{

|     |     |
| --- | --- |
| expires\_at | string |
| filters | #/definitions/models.Filtersmodels.Filters{

|     |     |
| --- | --- |
| browser | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| browser\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| city | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| connection\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| country | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| device\_brand | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| device\_model | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| device\_type | #/definitions/models.DeviceTypeFiltermodels.DeviceTypeFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| domain\_referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| fraud | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| ip | #/definitions/models.IPFiltermodels.IPFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| isp | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| languages | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| os | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| os\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| proxy\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| region | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| subs | #/definitions/models.SubsFiltermodels.SubsFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| items | #/definitions/models.SubItemsmodels.SubItems{

|     |     |
| --- | --- |
| sub1 | string |
| sub10 | string |
| sub11 | string |
| sub12 | string |
| sub13 | string |
| sub14 | string |
| sub15 | string |
| sub16 | string |
| sub17 | string |
| sub18 | string |
| sub19 | string |
| sub2 | string |
| sub20 | string |
| sub3 | string |
| sub4 | string |
| sub5 | string |
| sub6 | string |
| sub7 | string |
| sub8 | string |
| sub9 | string |

} |
| kind | integer |

} |
| unique\_visitor | #/definitions/models.UniqueVisitorFiltermodels.UniqueVisitorFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |

} |

} |
| id | string |
| landings | \[#/definitions/models.StreamLandingmodels.StreamLanding{\
\
|     |     |\
| --- | --- |\
| filters | #/definitions/models.Filtersmodels.Filters{\
\
|     |     |\
| --- | --- |\
| browser | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| browser\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| city | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| connection\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| country | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_brand | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_model | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_type | #/definitions/models.DeviceTypeFiltermodels.DeviceTypeFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| domain\_referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| fraud | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| ip | #/definitions/models.IPFiltermodels.IPFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| isp | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| languages | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| proxy\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| region | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| subs | #/definitions/models.SubsFiltermodels.SubsFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| items | #/definitions/models.SubItemsmodels.SubItems{\
\
|     |     |\
| --- | --- |\
| sub1 | string |\
| sub10 | string |\
| sub11 | string |\
| sub12 | string |\
| sub13 | string |\
| sub14 | string |\
| sub15 | string |\
| sub16 | string |\
| sub17 | string |\
| sub18 | string |\
| sub19 | string |\
| sub2 | string |\
| sub20 | string |\
| sub3 | string |\
| sub4 | string |\
| sub5 | string |\
| sub6 | string |\
| sub7 | string |\
| sub8 | string |\
| sub9 | string |\
\
} |\
| kind | integer |\
\
} |\
| unique\_visitor | #/definitions/models.UniqueVisitorFiltermodels.UniqueVisitorFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
\
} |\
\
} |\
| id | string |\
| name | string |\
| weight | integer |\
\
}\] |
| offers | \[#/definitions/models.StreamOffermodels.StreamOffer{\
\
|     |     |\
| --- | --- |\
| filters | #/definitions/models.Filtersmodels.Filters{\
\
|     |     |\
| --- | --- |\
| browser | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| browser\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| city | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| connection\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| country | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_brand | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_model | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_type | #/definitions/models.DeviceTypeFiltermodels.DeviceTypeFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| domain\_referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| fraud | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| ip | #/definitions/models.IPFiltermodels.IPFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| isp | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| languages | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| proxy\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| region | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| subs | #/definitions/models.SubsFiltermodels.SubsFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| items | #/definitions/models.SubItemsmodels.SubItems{\
\
|     |     |\
| --- | --- |\
| sub1 | string |\
| sub10 | string |\
| sub11 | string |\
| sub12 | string |\
| sub13 | string |\
| sub14 | string |\
| sub15 | string |\
| sub16 | string |\
| sub17 | string |\
| sub18 | string |\
| sub19 | string |\
| sub2 | string |\
| sub20 | string |\
| sub3 | string |\
| sub4 | string |\
| sub5 | string |\
| sub6 | string |\
| sub7 | string |\
| sub8 | string |\
| sub9 | string |\
\
} |\
| kind | integer |\
\
} |\
| unique\_visitor | #/definitions/models.UniqueVisitorFiltermodels.UniqueVisitorFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
\
} |\
\
} |\
| id | string |\
| name | string |\
| weight | integer |\
\
}\] |
| prelandings | \[#/definitions/models.StreamLandingmodels.StreamLanding{\
\
|     |     |\
| --- | --- |\
| filters | #/definitions/models.Filtersmodels.Filters{\
\
|     |     |\
| --- | --- |\
| browser | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| browser\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| city | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| connection\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| country | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_brand | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_model | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_type | #/definitions/models.DeviceTypeFiltermodels.DeviceTypeFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| domain\_referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| fraud | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| ip | #/definitions/models.IPFiltermodels.IPFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| isp | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| languages | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| proxy\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| region | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| subs | #/definitions/models.SubsFiltermodels.SubsFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| items | #/definitions/models.SubItemsmodels.SubItems{\
\
|     |     |\
| --- | --- |\
| sub1 | string |\
| sub10 | string |\
| sub11 | string |\
| sub12 | string |\
| sub13 | string |\
| sub14 | string |\
| sub15 | string |\
| sub16 | string |\
| sub17 | string |\
| sub18 | string |\
| sub19 | string |\
| sub2 | string |\
| sub20 | string |\
| sub3 | string |\
| sub4 | string |\
| sub5 | string |\
| sub6 | string |\
| sub7 | string |\
| sub8 | string |\
| sub9 | string |\
\
} |\
| kind | integer |\
\
} |\
| unique\_visitor | #/definitions/models.UniqueVisitorFiltermodels.UniqueVisitorFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
\
} |\
\
} |\
| id | string |\
| name | string |\
| weight | integer |\
\
}\] |
| template | boolean |
| title | string |
| user\_id | string |

} |
| weight | integer |

}

#/definitions/models.Categorymodels.Category{

|     |     |
| --- | --- |
| alias | string |
| id | string |
| name | string |
| sub\_categories | \[#/definitions/models.SubCategorymodels.SubCategory{\
\
|     |     |\
| --- | --- |\
| alias | string |\
| name | string |\
\
}\] |

}

#/definitions/models.Citymodels.City{

|     |     |
| --- | --- |
| country\_iso | string |
| id | string |
| name | string |
| region | string |

}

#/definitions/models.ColumnSettingsmodels.ColumnSettings{

|     |     |
| --- | --- |
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |
| enabled | boolean<br>Show column in a table or not |
| id | string<br>Column id |
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |

}

#/definitions/models.ConversionPostbackmodels.ConversionPostback{

|     |     |
| --- | --- |
| events | \[<br>deprecated<br>string\] |
| goals | \[string\] |
| json\_body | string |
| match\_event | boolean |
| payment\_percent | number |
| request\_method | integer |
| statuses | \[string\] |
| url | string |

}

#/definitions/models.ConversionTypeToMultiplePostbackmodels.ConversionTypeToMultiplePostback{

|     |     |
| --- | --- |
| < \\* >: | string |

}

#/definitions/models.ConversionTypesmodels.ConversionTypes{

|     |     |
| --- | --- |
| default\_type | string |
| type1 | string |
| type10 | string |
| type11 | string |
| type12 | string |
| type13 | string |
| type14 | string |
| type15 | string |
| type16 | string |
| type17 | string |
| type18 | string |
| type19 | string |
| type2 | string |
| type20 | string |
| type21 | string |
| type22 | string |
| type23 | string |
| type24 | string |
| type25 | string |
| type26 | string |
| type27 | string |
| type28 | string |
| type29 | string |
| type3 | string |
| type30 | string |
| type31 | string |
| type32 | string |
| type33 | string |
| type34 | string |
| type35 | string |
| type36 | string |
| type37 | string |
| type38 | string |
| type39 | string |
| type4 | string |
| type40 | string |
| type5 | string |
| type6 | string |
| type7 | string |
| type8 | string |
| type9 | string |

}

#/definitions/models.ConversionViewmodels.ConversionView{

|     |     |
| --- | --- |
| attribution\_type | string |
| browser | string |
| campaign | string |
| campaign\_id | string |
| city | string |
| clickid | string |
| connection\_type | string |
| conv\_time | string |
| cost | number |
| cost\_default | number |
| cost\_source | number |
| country | string |
| coupon | string |
| created\_at | string |
| currency | string |
| deduplicate\_token | string |
| deeplink | string |
| default\_type | integer |
| device | string |
| device\_brand | string |
| device\_fullname | string |
| duplicate\_status | integer |
| event | string |
| external\_id | string |
| fingerprint | string |
| id | string |
| ip | string |
| is\_transaction | integer |
| isp | string |
| landing | string |
| landing\_id | string |
| network | string |
| offer | string |
| offer\_id | string |
| order | string |
| os | string |
| p\_sub1 | string |
| p\_sub10 | string |
| p\_sub11 | string |
| p\_sub12 | string |
| p\_sub13 | string |
| p\_sub14 | string |
| p\_sub15 | string |
| p\_sub16 | string |
| p\_sub17 | string |
| p\_sub18 | string |
| p\_sub19 | string |
| p\_sub2 | string |
| p\_sub20 | string |
| p\_sub3 | string |
| p\_sub4 | string |
| p\_sub5 | string |
| p\_sub6 | string |
| p\_sub7 | string |
| p\_sub8 | string |
| p\_sub9 | string |
| page | string |
| page\_url | string |
| payout | number |
| payout\_default | number |
| payout\_network | number |
| postback\_ip | string |
| prelanding | string |
| prelanding\_id | string |
| program\_id | string |
| pub\_revenue | number |
| pub\_revenue\_default | number |
| pub\_revenue\_source | number |
| ref\_id | string |
| referer | string |
| region | string |
| rt\_ad | string |
| rt\_ad\_id | string |
| rt\_adgroup | string |
| rt\_adgroup\_id | string |
| rt\_campaign | string |
| rt\_campaign\_id | string |
| rt\_keyword | string |
| rt\_medium | string |
| rt\_placement | string |
| rt\_placement\_hashed | string |
| rt\_placement\_id | string |
| rt\_role\_1 | string |
| rt\_role\_2 | string |
| rt\_source | string |
| server | string |
| source | string |
| source\_id | string |
| status | string |
| sub1 | string |
| sub10 | string |
| sub11 | string |
| sub12 | string |
| sub13 | string |
| sub14 | string |
| sub15 | string |
| sub16 | string |
| sub17 | string |
| sub18 | string |
| sub19 | string |
| sub2 | string |
| sub20 | string |
| sub3 | string |
| sub4 | string |
| sub5 | string |
| sub6 | string |
| sub7 | string |
| sub8 | string |
| sub9 | string |
| track\_time | string |
| type | string |
| type1 | integer |
| type10 | integer |
| type11 | integer |
| type12 | integer |
| type13 | integer |
| type14 | integer |
| type15 | integer |
| type16 | integer |
| type17 | integer |
| type18 | integer |
| type19 | integer |
| type2 | integer |
| type20 | integer |
| type21 | integer |
| type22 | integer |
| type23 | integer |
| type24 | integer |
| type25 | integer |
| type26 | integer |
| type27 | integer |
| type28 | integer |
| type29 | integer |
| type3 | integer |
| type30 | integer |
| type31 | integer |
| type32 | integer |
| type33 | integer |
| type34 | integer |
| type35 | integer |
| type36 | integer |
| type37 | integer |
| type38 | integer |
| type39 | integer |
| type4 | integer |
| type40 | integer |
| type5 | integer |
| type6 | integer |
| type7 | integer |
| type8 | integer |
| type9 | integer |
| user\_agent | string |

}

#/definitions/models.Countrymodels.Country{

|     |     |
| --- | --- |
| id | string |
| iso | string |
| title | string |

}

#/definitions/models.Creativemodels.Creative{

|     |     |
| --- | --- |
| description | string |
| image\_url | string |
| title | string |

}

#/definitions/models.Currencymodels.Currency{

|     |     |
| --- | --- |
| aliases | \[string\] |
| exchange\_rate | #/definitions/models.ExchangeRatemodels.ExchangeRate{

|     |     |
| --- | --- |
| source | string |
| updated\_at | string |
| value | number |

} |
| letter\_code | string |

}

#/definitions/models.CustomColumnmodels.CustomColumn{

|     |     |
| --- | --- |
| description | string |
| format | integer<br>Format stores info for frontend |
| formula | string<br>contains formula i.e. “roi\*2” |
| id | string |
| name | string<br>Name contains user’s name of column |
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |

}

#/definitions/models.CustomConvTypeConvSubsGeoPayoutsmodels.CustomConvTypeConvSubsGeoPayouts{

|     |     |
| --- | --- |
| conversion\_type | string |
| country | string |
| sub | string |
| sub\_value | string |
| value | number |

}

#/definitions/models.CustomConvTypeConvSubsPayoutsmodels.CustomConvTypeConvSubsPayouts{

|     |     |
| --- | --- |
| conversion\_type | string |
| sub | string |
| sub\_value | string |
| value | number |

}

#/definitions/models.CustomConvTypeGeoPayoutsmodels.CustomConvTypeGeoPayouts{

|     |     |
| --- | --- |
| conversion\_type | string |
| country | string |
| value | number |

}

#/definitions/models.CustomConversionSubsPayoutmodels.CustomConversionSubsPayout{

|     |     |
| --- | --- |
| sub | string |
| sub\_value | string |
| value | number |

}

#/definitions/models.CustomConversionTypePayoutmodels.CustomConversionTypePayout{

|     |     |
| --- | --- |
| conversion\_type | string |
| value | number |

}

#/definitions/models.CustomGeoOsPayoutmodels.CustomGeoOsPayout{

|     |     |
| --- | --- |
| country | string |
| os | string |
| value | number |

}

#/definitions/models.CustomGeoPayoutmodels.CustomGeoPayout{

|     |     |
| --- | --- |
| country | string |
| value | number |

}

#/definitions/models.CustomPubPayoutmodels.CustomPubPayout{

|     |     |
| --- | --- |
| publisher | string |
| value | number |

}

#/definitions/models.CustomPubSubGeoPayoutmodels.CustomPubSubGeoPayout{

|     |     |
| --- | --- |
| country | string |
| publisher | string |
| sub | string |
| sub\_value | string |
| value | number |

}

#/definitions/models.CustomPubSubPayoutmodels.CustomPubSubPayout{

|     |     |
| --- | --- |
| publisher | string |
| sub | string |
| sub\_value | string |
| value | number |

}

#/definitions/models.CustomPubSubThrottlemodels.CustomPubSubThrottle{

|     |     |
| --- | --- |
| publisher | string |
| status | string |
| sub | string |
| sub\_value | string |
| value | integer |

}

#/definitions/models.CustomPubThrottlemodels.CustomPubThrottle{

|     |     |
| --- | --- |
| publisher | string |
| status | string |
| value | integer |

}

#/definitions/models.CustomThrottlemodels.CustomThrottle{

|     |     |
| --- | --- |
| status | string |
| value | integer |

}

#/definitions/models.CustomTypePayoutmodels.CustomTypePayout{

|     |     |
| --- | --- |
| type | string |
| value | number |

}

#/definitions/models.Deeplinkmodels.Deeplink{

|     |     |
| --- | --- |
| active\_direct | boolean |
| active\_impression | boolean |
| active\_redirect | boolean |
| direct\_url | string |
| impression\_url | string |
| link | string |
| name | string |
| redirect\_url | string |

}

#/definitions/models.Devicemodels.Device{

|     |     |
| --- | --- |
| code | string |
| id | string |
| title | string |

}

#/definitions/models.DeviceBrandmodels.DeviceBrand{

|     |     |
| --- | --- |
| title | string |

}

#/definitions/models.DeviceFullNamemodels.DeviceFullName{

|     |     |
| --- | --- |
| title | string |

}

#/definitions/models.DeviceTypeFiltermodels.DeviceTypeFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

}

#/definitions/models.ExchangeRatemodels.ExchangeRate{

|     |     |
| --- | --- |
| source | string |
| updated\_at | string |
| value | number |

}

#/definitions/models.FacebookMatchmodels.FacebookMatch{

|     |     |
| --- | --- |
| conversion\_type | string<br>ConversionType is type of conversion in Redtrack: default, type1, type20 |
| facebook\_type | integer<br>FacebookType is type of conversion in Facebook: Purchase, AddToCart, etc. |

}

#/definitions/models.FacebookPixelmodels.FacebookPixel{

|     |     |
| --- | --- |
| action\_source\_fb | string<br>ActionSourceFB is a place where a conversion occurred (e.g. mail, website, etc.) |
| conversions\_apikey | string<br>ConversionsApikey is an access token to the pixel |
| event\_source\_url\_fb | string<br>EventSourceUrlFB is a browser URL where a conversion happened |
| pixel\_id | string<br>PixelID is Facebook pixel id |

}

#/definitions/models.Filtersmodels.Filters{

|     |     |
| --- | --- |
| browser | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| browser\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| city | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| connection\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| country | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| device\_brand | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| device\_model | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| device\_type | #/definitions/models.DeviceTypeFiltermodels.DeviceTypeFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| domain\_referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| fraud | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| ip | #/definitions/models.IPFiltermodels.IPFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| isp | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| languages | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| os | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| os\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| proxy\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| region | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| subs | #/definitions/models.SubsFiltermodels.SubsFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| items | #/definitions/models.SubItemsmodels.SubItems{

|     |     |
| --- | --- |
| sub1 | string |
| sub10 | string |
| sub11 | string |
| sub12 | string |
| sub13 | string |
| sub14 | string |
| sub15 | string |
| sub16 | string |
| sub17 | string |
| sub18 | string |
| sub19 | string |
| sub2 | string |
| sub20 | string |
| sub3 | string |
| sub4 | string |
| sub5 | string |
| sub6 | string |
| sub7 | string |
| sub8 | string |
| sub9 | string |

} |
| kind | integer |

} |
| unique\_visitor | #/definitions/models.UniqueVisitorFiltermodels.UniqueVisitorFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |

} |

}

#/definitions/models.FingerprintSettingsmodels.FingerprintSettings{

|     |     |
| --- | --- |
| assisted\_click\_weight | integer |
| first\_click\_weight | integer |
| last\_click\_weight | integer |

}

#/definitions/models.IPFiltermodels.IPFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

}

#/definitions/models.ISPmodels.ISP{

|     |     |
| --- | --- |
| name | string |

}

#/definitions/models.MailerCustomizationmodels.MailerCustomization{

|     |     |
| --- | --- |
| pub\_campaign\_status\_changed | #/definitions/models.MailerFieldsmodels.MailerFields{

|     |     |
| --- | --- |
| body | string |
| email\_notifications | boolean |
| greeting | string |
| signature | string |
| subject | string |

} |
| pub\_declined | #/definitions/models.MailerFieldsmodels.MailerFields{

|     |     |
| --- | --- |
| body | string |
| email\_notifications | boolean |
| greeting | string |
| signature | string |
| subject | string |

} |
| pub\_new\_campaign | #/definitions/models.MailerFieldsmodels.MailerFields{

|     |     |
| --- | --- |
| body | string |
| email\_notifications | boolean |
| greeting | string |
| signature | string |
| subject | string |

} |
| pub\_password\_reset | #/definitions/models.MailerFieldsmodels.MailerFields{

|     |     |
| --- | --- |
| body | string |
| email\_notifications | boolean |
| greeting | string |
| signature | string |
| subject | string |

} |
| pub\_paused | #/definitions/models.MailerFieldsmodels.MailerFields{

|     |     |
| --- | --- |
| body | string |
| email\_notifications | boolean |
| greeting | string |
| signature | string |
| subject | string |

} |
| pub\_signup\_completed | #/definitions/models.MailerFieldsmodels.MailerFields{

|     |     |
| --- | --- |
| body | string |
| email\_notifications | boolean |
| greeting | string |
| signature | string |
| subject | string |

} |
| pub\_signup\_requested | #/definitions/models.MailerFieldsmodels.MailerFields{

|     |     |
| --- | --- |
| body | string |
| email\_notifications | boolean |
| greeting | string |
| signature | string |
| subject | string |

} |

}

#/definitions/models.MailerFieldsmodels.MailerFields{

|     |     |
| --- | --- |
| body | string |
| email\_notifications | boolean |
| greeting | string |
| signature | string |
| subject | string |

}

#/definitions/models.OSmodels.OS{

|     |     |
| --- | --- |
| id | string |
| title | string |

}

#/definitions/models.OSFullNamemodels.OSFullName{

|     |     |
| --- | --- |
| title | string |

}

#/definitions/models.Offermodels.Offer{

|     |     |
| --- | --- |
| action\_source\_fb | string |
| cap | integer |
| cap\_alert | boolean |
| category | string |
| clcap | integer |
| clcap\_alert | boolean |
| click\_cap | integer |
| click\_cap\_period | string |
| click\_cap\_type | string |
| country\_codes | \[string\] |
| created\_at | string |
| default\_conversion\_status | string |
| event\_source\_url\_fb | string |
| expires\_at | string |
| facebook\_matching | \[#/definitions/models.FacebookMatchmodels.FacebookMatch{\
\
|     |     |\
| --- | --- |\
| conversion\_type | string<br>ConversionType is type of conversion in Redtrack: default, type1, type20 |\
| facebook\_type | integer<br>FacebookType is type of conversion in Facebook: Purchase, AddToCart, etc. |\
\
}\] |
| facebook\_pixels | \[#/definitions/models.FacebookPixelmodels.FacebookPixel{\
\
|     |     |\
| --- | --- |\
| action\_source\_fb | string<br>ActionSourceFB is a place where a conversion occurred (e.g. mail, website, etc.) |\
| conversions\_apikey | string<br>ConversionsApikey is an access token to the pixel |\
| event\_source\_url\_fb | string<br>EventSourceUrlFB is a browser URL where a conversion happened |\
| pixel\_id | string<br>PixelID is Facebook pixel id |\
\
}\] |
| fingerprint\_settings | #/definitions/models.FingerprintSettingsmodels.FingerprintSettings{

|     |     |
| --- | --- |
| assisted\_click\_weight | integer |
| first\_click\_weight | integer |
| last\_click\_weight | integer |

} |
| id | string |
| network\_title | string |
| notes | string |
| payment | #/definitions/models.OffersPaymentmodels.OffersPayment{

|     |     |
| --- | --- |
| amount | number |

} |
| postback\_url | string |
| program\_id | string |
| script\_id | string |
| serial\_number | integer |
| snapchat\_matching | \[#/definitions/models.SnapchatMatchingmodels.SnapchatMatching{\
\
|     |     |\
| --- | --- |\
| conversions\_type | string<br>ConversionsType is type of conversion in Redtrack: default, type1, type20 |\
| snapchat\_type | integer<br>SnapchatType is type of conversion in Snapchat: PURCHASE, ADD\_CARD, etc. |\
\
}\] |
| snapchat\_pixels | \[#/definitions/models.SnapchatPixelmodels.SnapchatPixel{\
\
|     |     |\
| --- | --- |\
| pixel\_id | string |\
| pixel\_token | string |\
\
}\] |
| stat | #/definitions/models.Statmodels.Stat{

|
|

} |
| status | integer |
| subcategory | string |
| tags | \[string\] |
| title | string |
| updated\_at | string |
| url | string |
| user\_id | string |

}

#/definitions/models.OffersPaymentmodels.OffersPayment{

|     |     |
| --- | --- |
| amount | number |

}

#/definitions/models.Paginationmodels.Pagination{

|     |     |
| --- | --- |
| limit | integer |
| page | integer |
| total | integer |

}

#/definitions/models.PaymentNotificationsmodels.PaymentNotifications{

|     |     |
| --- | --- |
| is\_email | boolean<br>IsEmail is true if we should send payout request to user email |
| is\_webhook | boolean<br>IsWebhook is true if we should send payout request to webhook |
| webhook\_url | string<br>WebhookURL is client’s url for getting payout request (only POST method) |

}

#/definitions/models.PaymentRequestSettingsmodels.PaymentRequestSettings{

|     |     |
| --- | --- |
| company\_name | string<br>CompanyName is organization name, will also be used in invoice description |
| details | string<br>Details are billing and/ contact details |
| payment\_notifications | #/definitions/models.PaymentNotificationsmodels.PaymentNotifications{

|     |     |
| --- | --- |
| is\_email | boolean<br>IsEmail is true if we should send payout request to user email |
| is\_webhook | boolean<br>IsWebhook is true if we should send payout request to webhook |
| webhook\_url | string<br>WebhookURL is client’s url for getting payout request (only POST method) |

} |
| payment\_terms | integer<br>PaymentTerms are “Net” payment terms for invoice |
| payment\_types | \[\
\
PaymentTypes contains list of payment types (wire transfer, paypal, etc.)\
\
#/definitions/models.PaymentTypemodels.PaymentType{\
\
|     |     |\
| --- | --- |\
| amount | number<br>Amount is minimum allowed amount of request payout |\
| is\_enabled | boolean<br>IsEnabled is true if we should display the payment type in publisher interface |\
| name | string<br>Name of payment type |\
\
}\] |

}

#/definitions/models.PaymentTypemodels.PaymentType{

|     |     |
| --- | --- |
| amount | number<br>Amount is minimum allowed amount of request payout |
| is\_enabled | boolean<br>IsEnabled is true if we should display the payment type in publisher interface |
| name | string<br>Name of payment type |

}

#/definitions/models.PromotionalBannermodels.PromotionalBanner{

|     |     |
| --- | --- |
| picture\_url | string |
| redirect\_url | string |

}

#/definitions/models.PubPaymentmodels.PubPayment{

|     |     |
| --- | --- |
| amount | number |
| amount\_paid | number |
| created\_at | string |
| id | string<br>InvitedBy points to referral inviter. Could be empty. |
| note | string |
| payment\_date | string |
| payment\_method | string |
| pub\_id | string<br>InvitedBy points to referral inviter. Could be empty. |
| serial\_number | integer |
| status | integer |
| updated\_at | string |
| user\_id | string<br>InvitedBy points to referral inviter. Could be empty. |

}

#/definitions/models.PubSettingsmodels.PubSettings{

|     |     |
| --- | --- |
| allow\_signup | boolean |
| brand | string |
| conversion\_type\_to\_multiple\_postback\_active | {

|     |     |
| --- | --- |
| < \\* >: | boolean |

} |
| conversions\_settings | \[\
\
ConversionsSettings stores the rules for displaying columns in the conversions log in a pub panel\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |
| currency | string |
| data\_retention | integer |
| default\_campaigns | \[string<br>InvitedBy points to referral inviter. Could be empty.<br>\] |
| default\_sources | \[string<br>InvitedBy points to referral inviter. Could be empty.<br>\] |
| domain | string |
| domain\_id | string<br>InvitedBy points to referral inviter. Could be empty. |
| favicon\_url | string |
| goals | #/definitions/models.ConversionTypesmodels.ConversionTypes{

|     |     |
| --- | --- |
| default\_type | string |
| type1 | string |
| type10 | string |
| type11 | string |
| type12 | string |
| type13 | string |
| type14 | string |
| type15 | string |
| type16 | string |
| type17 | string |
| type18 | string |
| type19 | string |
| type2 | string |
| type20 | string |
| type21 | string |
| type22 | string |
| type23 | string |
| type24 | string |
| type25 | string |
| type26 | string |
| type27 | string |
| type28 | string |
| type29 | string |
| type3 | string |
| type30 | string |
| type31 | string |
| type32 | string |
| type33 | string |
| type34 | string |
| type35 | string |
| type36 | string |
| type37 | string |
| type38 | string |
| type39 | string |
| type4 | string |
| type40 | string |
| type5 | string |
| type6 | string |
| type7 | string |
| type8 | string |
| type9 | string |

} |
| gtm\_id | string<br>GtmID is account for Google Tag Manager id |
| id | string<br>InvitedBy points to referral inviter. Could be empty. |
| is\_alias\_enabled | boolean |
| is\_multiple\_postbacks\_active | boolean |
| logo\_url | string |
| mailer\_customization | #/definitions/models.MailerCustomizationmodels.MailerCustomization{

|     |     |
| --- | --- |
| pub\_campaign\_status\_changed | #/definitions/models.MailerFieldsmodels.MailerFields{

|     |     |
| --- | --- |
| body | string |
| email\_notifications | boolean |
| greeting | string |
| signature | string |
| subject | string |

} |
| pub\_declined | #/definitions/models.MailerFieldsmodels.MailerFields{

|     |     |
| --- | --- |
| body | string |
| email\_notifications | boolean |
| greeting | string |
| signature | string |
| subject | string |

} |
| pub\_new\_campaign | #/definitions/models.MailerFieldsmodels.MailerFields{

|     |     |
| --- | --- |
| body | string |
| email\_notifications | boolean |
| greeting | string |
| signature | string |
| subject | string |

} |
| pub\_password\_reset | #/definitions/models.MailerFieldsmodels.MailerFields{

|     |     |
| --- | --- |
| body | string |
| email\_notifications | boolean |
| greeting | string |
| signature | string |
| subject | string |

} |
| pub\_paused | #/definitions/models.MailerFieldsmodels.MailerFields{

|     |     |
| --- | --- |
| body | string |
| email\_notifications | boolean |
| greeting | string |
| signature | string |
| subject | string |

} |
| pub\_signup\_completed | #/definitions/models.MailerFieldsmodels.MailerFields{

|     |     |
| --- | --- |
| body | string |
| email\_notifications | boolean |
| greeting | string |
| signature | string |
| subject | string |

} |
| pub\_signup\_requested | #/definitions/models.MailerFieldsmodels.MailerFields{

|     |     |
| --- | --- |
| body | string |
| email\_notifications | boolean |
| greeting | string |
| signature | string |
| subject | string |

} |

} |
| manager\_email | string<br>ManagerEmail is contact information of publishers manager email. |
| needs\_approval | boolean |
| payment\_request\_settings | #/definitions/models.PaymentRequestSettingsmodels.PaymentRequestSettings{

|     |     |
| --- | --- |
| company\_name | string<br>CompanyName is organization name, will also be used in invoice description |
| details | string<br>Details are billing and/ contact details |
| payment\_notifications | #/definitions/models.PaymentNotificationsmodels.PaymentNotifications{

|     |     |
| --- | --- |
| is\_email | boolean<br>IsEmail is true if we should send payout request to user email |
| is\_webhook | boolean<br>IsWebhook is true if we should send payout request to webhook |
| webhook\_url | string<br>WebhookURL is client’s url for getting payout request (only POST method) |

} |
| payment\_terms | integer<br>PaymentTerms are “Net” payment terms for invoice |
| payment\_types | \[\
\
PaymentTypes contains list of payment types (wire transfer, paypal, etc.)\
\
#/definitions/models.PaymentTypemodels.PaymentType{\
\
|     |     |\
| --- | --- |\
| amount | number<br>Amount is minimum allowed amount of request payout |\
| is\_enabled | boolean<br>IsEnabled is true if we should display the payment type in publisher interface |\
| name | string<br>Name of payment type |\
\
}\] |

} |
| privacy\_policy\_url | string |
| promotional\_banners | \[#/definitions/models.PromotionalBannermodels.PromotionalBanner{\
\
|     |     |\
| --- | --- |\
| picture\_url | string |\
| redirect\_url | string |\
\
}\] |
| referral\_program | #/definitions/models.ReferralProgramOptionsmodels.ReferralProgramOptions{

|     |     |
| --- | --- |
| enabled | boolean<br>Enabled indicates that referral program is enabled for specific PubSetting/whitelabel |
| maximumReferralsChain | integer<br>MaximumReferralsChain is maximum count of users which are participated in referral program. For<br>setting, use it native (like MaximumReferralsChain = ), but for getting, use GetMaxSteps()<br>method, cause this field may contain invalid values.<br>0 is invalid, default value is 1. If set to -1, payments will make biggest chain ever possible, and<br>will pay to sediment<br>Default value is 9. If value is -1, then it must be interpreted as maximum possible chain. If it is<br>zero, then referral chain must be interpreted as 1 |
| paymentsFirstMultiplier | number<br>PaymentsFirstMultiplier is base multiplier for the first referral emitent after publisher who received.<br>Default value is 0.1 |
| referralURL | string<br>ReferralURL is custom url for referral program signup link |
| stepDecrementCoefficient | number<br>StepDecrementCoefficient is a field that denotes the number to which the main factor of the first step<br>is reduced.<br>Default value is 0.01 |

} |
| settings | \[\
\
Settings stores the rules for displaying columns in reports in a pub panel\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |
| show\_accrued\_conversions | boolean<br>if true we have to consider campaigns condition postbacks in filters |
| show\_alias | boolean |
| show\_payouts | boolean |
| show\_postbacks\_logs | boolean |
| show\_sign\_up | boolean |
| sign\_in\_form | #/definitions/models.SignFormmodels.SignForm{

|     |     |
| --- | --- |
| sub\_title | string |
| title | string |

} |
| sign\_up\_form | #/definitions/models.SignFormmodels.SignForm{

|     |     |
| --- | --- |
| sub\_title | string |
| title | string |

} |
| sign\_up\_form\_fields | #/definitions/models.SignUpFormFieldsmodels.SignUpFormFields{

|     |     |
| --- | --- |
| show\_affiliate\_type | boolean |
| show\_country | boolean |
| show\_find\_us | boolean |
| show\_first\_name | boolean |
| show\_geos | boolean |
| show\_last\_name | boolean |
| show\_messenger | boolean |
| show\_messenger\_type | boolean |
| show\_payout\_type | boolean |
| show\_payout\_volume | boolean |
| show\_referral | boolean |
| show\_traffic\_type | boolean |
| show\_verticals | boolean |
| show\_verticals\_details | boolean |

} |
| terms\_conditions\_url | string |
| terms\_enabled | boolean |
| title | string |
| user\_id | string<br>InvitedBy points to referral inviter. Could be empty. |
| webhook\_url | string |
| website | string |

}

#/definitions/models.Publishermodels.Publisher{

|     |     |
| --- | --- |
| affiliate\_types | \[<br>What is your specialization?<br>integer\] |
| alias | string |
| apikey | string |
| balance | number |
| billing\_details | string |
| campaign\_titles | \[string\] |
| campaigns | \[string<br>InvitedBy points to referral inviter. Could be empty.<br>\] |
| company\_type | string |
| contact\_details | string |
| conversion\_type\_to\_multiple\_postback | #/definitions/models.ConversionTypeToMultiplePostbackmodels.ConversionTypeToMultiplePostback{

|     |     |
| --- | --- |
| < \\* >: | string |

} |
| country | string<br>Country of publisher |
| coupon\_token | string |
| created\_at | string |
| email | string |
| find\_us | integer<br>How did you hear about us? |
| find\_us\_details | string |
| firstname | string<br>Firstname of publisher |
| geos | \[<br>Your top GEOs<br>integer\] |
| id | string |
| invite\_key | string |
| invited\_by | string<br>InvitedBy points to referral inviter. Could be empty. |
| language | string |
| lastname | string<br>Lastname of publisher |
| manager\_email | string<br>ManagerEmail is contact information of publisher’s manager email. See RTK-421 for more info |
| messenger | string<br>Messenger is account name in a messenger |
| messenger\_type | string<br>MessengerType is type of messenger (facebook, skype, telegram, phone, other) |
| parents | \[<br>Parents array of Ids of all referral parents. Referral program: A -> B -> C.<br>For publisher C field ‘parents’ will contain id of publisher A and id of publisher B<br>string<br>InvitedBy points to referral inviter. Could be empty.<br>\] |
| password | string |
| password\_confirmation | string |
| payment\_type | string<br>PaymentType is a preferred payment type for this publisher. This field can contain any value of payment<br>identificator for specific pubSettings (publisher whitelabel). Typically, if PaymentType contains<br>invalid identificator (/^\[a-zA-Z0-9\_-\]$/) or it doesn’t contain in pubSettings payment methods, then<br>any action with payout must throw error |
| payout\_types | \[<br>What payout types do you work with<br>integer\] |
| payout\_volume | integer<br>What is your monthly volume for your offers |
| postbacks | \[string\] |
| referral | boolean<br>Were you referred by our AM or another publisher? |
| referral\_balance | number |
| referral\_commission | number |
| referral\_count | integer |
| referral\_details | string |
| referral\_program | #/definitions/models.ReferralProgramOptionsmodels.ReferralProgramOptions{

|     |     |
| --- | --- |
| enabled | boolean<br>Enabled indicates that referral program is enabled for specific PubSetting/whitelabel |
| maximumReferralsChain | integer<br>MaximumReferralsChain is maximum count of users which are participated in referral program. For<br>setting, use it native (like MaximumReferralsChain = ), but for getting, use GetMaxSteps()<br>method, cause this field may contain invalid values.<br>0 is invalid, default value is 1. If set to -1, payments will make biggest chain ever possible, and<br>will pay to sediment<br>Default value is 9. If value is -1, then it must be interpreted as maximum possible chain. If it is<br>zero, then referral chain must be interpreted as 1 |
| paymentsFirstMultiplier | number<br>PaymentsFirstMultiplier is base multiplier for the first referral emitent after publisher who received.<br>Default value is 0.1 |
| referralURL | string<br>ReferralURL is custom url for referral program signup link |
| stepDecrementCoefficient | number<br>StepDecrementCoefficient is a field that denotes the number to which the main factor of the first step<br>is reduced.<br>Default value is 0.01 |

} |
| referral\_program\_approved | boolean<br>ReferralProgramApproved<br>аппрув паблишеру в реф программе, означает,<br>что пригласивший паблишер и все паблишеры выше по иерархии будут получать выплаты по<br>реф программе за действия аппрувнотого паблишера.<br>Если аппрува нет, то выплаты будут засчитываться, но не учитываться. |
| settings\_id | string |
| source\_titles | \[string\] |
| sources | \[string<br>InvitedBy points to referral inviter. Could be empty.<br>\] |
| status | integer |
| total\_balance | number |
| traffic\_handling\_policy | integer |
| traffic\_types | \[<br>What is your primary traffic type?<br>integer\] |
| traffic\_types\_details | string |
| user\_id | string |
| verticals | \[<br>Your main verticals<br>integer\] |
| verticals\_details | string<br>Please tell us more about offers you work with |

}

#/definitions/models.PublisherDetailsmodels.PublisherDetails{

|     |     |
| --- | --- |
| advertiser | string |
| campaign\_rate | #/definitions/models.CampaignRatemodels.CampaignRate{

|     |     |
| --- | --- |
| status | integer |
| value | number |

} |
| campaign\_type | string |
| categories | \[string\] |
| countries | \[string\] |
| coupon | string |
| deeplinks | \[#/definitions/models.Deeplinkmodels.Deeplink{\
\
|     |     |\
| --- | --- |\
| active\_direct | boolean |\
| active\_impression | boolean |\
| active\_redirect | boolean |\
| direct\_url | string |\
| impression\_url | string |\
| link | string |\
| name | string |\
| redirect\_url | string |\
\
}\] |
| description | string |
| domain | string |
| hide\_deeplinks | boolean<br>HideDeeplinks shows what we need to hide deeplinks section |
| hide\_direct\_tracking\_urls | boolean<br>HideDirectTrackingURLs shows what we need to hide direct tracking urls section |
| hide\_payout\_details | boolean |
| hide\_redirect\_impression\_url | boolean<br>HideRedirectImpressionURL shows what we need to hide redirect impression url section |
| hide\_redirect\_tracking\_url | boolean<br>HideRedirectTrackingURL shows what we need to hide redirect tracking url section |
| os | \[string\] |
| preview | string |
| preview\_url | string |
| sources | \[string\] |

}

#/definitions/models.PublisherProfilemodels.PublisherProfile{

|     |     |
| --- | --- |
| affiliate\_types | \[<br>What is your specialization?<br>integer\] |
| billing\_details | string |
| company\_type | string |
| contact\_details | string |
| conversion\_type\_to\_multiple\_postback | #/definitions/models.ConversionTypeToMultiplePostbackmodels.ConversionTypeToMultiplePostback{

|     |     |
| --- | --- |
| < \\* >: | string |

} |
| country | string<br>Country of publisher |
| find\_us | integer<br>How did you hear about us? |
| find\_us\_details | string |
| firstname | string<br>Firstname of publisher |
| geos | \[<br>Your top GEOs<br>integer\] |
| invited\_by | string<br>InvitedBy points to referral inviter. Could be empty. |
| language | string |
| lastname | string<br>Lastname of publisher |
| manager\_email | string<br>ManagerEmail is contact information of publisher’s manager email. See RTK-421 for more info |
| messenger | string<br>Messenger is account name in a messenger |
| messenger\_type | string<br>MessengerType is type of messenger (facebook, skype, telegram, phone, other) |
| password | string |
| password\_confirmation | string |
| payment\_type | string<br>PaymentType is a preferred payment type for this publisher. This field can contain any value of payment<br>identificator for specific pubSettings (publisher whitelabel). Typically, if PaymentType contains<br>invalid identificator (/^\[a-zA-Z0-9\_-\]$/) or it doesn’t contain in pubSettings payment methods, then<br>any action with payout must throw error |
| payout\_types | \[<br>What payout types do you work with<br>integer\] |
| payout\_volume | integer<br>What is your monthly volume for your offers |
| postbacks | \[string\] |
| referral | boolean<br>Were you referred by our AM or another publisher? |
| referral\_details | string |
| traffic\_types | \[<br>What is your primary traffic type?<br>integer\] |
| traffic\_types\_details | string |
| verticals | \[<br>Your main verticals<br>integer\] |
| verticals\_details | string<br>Please tell us more about offers you work with |

}

#/definitions/models.ReferralProgramOptionsmodels.ReferralProgramOptions{

|     |     |
| --- | --- |
| enabled | boolean<br>Enabled indicates that referral program is enabled for specific PubSetting/whitelabel |
| maximumReferralsChain | integer<br>MaximumReferralsChain is maximum count of users which are participated in referral program. For<br>setting, use it native (like MaximumReferralsChain = ), but for getting, use GetMaxSteps()<br>method, cause this field may contain invalid values.<br>0 is invalid, default value is 1. If set to -1, payments will make biggest chain ever possible, and<br>will pay to sediment<br>Default value is 9. If value is -1, then it must be interpreted as maximum possible chain. If it is<br>zero, then referral chain must be interpreted as 1 |
| paymentsFirstMultiplier | number<br>PaymentsFirstMultiplier is base multiplier for the first referral emitent after publisher who received.<br>Default value is 0.1 |
| referralURL | string<br>ReferralURL is custom url for referral program signup link |
| stepDecrementCoefficient | number<br>StepDecrementCoefficient is a field that denotes the number to which the main factor of the first step<br>is reduced.<br>Default value is 0.01 |

}

#/definitions/models.Settingsmodels.Settings{

|     |     |
| --- | --- |
| created\_at | string<br>the time when user settings were created |
| id | string<br>InvitedBy points to referral inviter. Could be empty. |
| table\_acquisition | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_adverts | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_auto\_optimization\_report | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_campaigns | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_campaigns\_report | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_clicks | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_conversions | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_conversions\_report | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_costs | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_ip\_report | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_landings | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_networks | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_networks\_report | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_offers | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_offers\_report | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_postbacks | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_postbacks\_int | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_publishers | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_publishers\_statistics | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_sources | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| table\_sources\_report | #/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

} |
| updated\_at | string<br>last time when user settings were updated |
| user\_id | string<br>InvitedBy points to referral inviter. Could be empty. |

}

#/definitions/models.SignFormmodels.SignForm{

|     |     |
| --- | --- |
| sub\_title | string |
| title | string |

}

#/definitions/models.SignUpFormFieldsmodels.SignUpFormFields{

|     |     |
| --- | --- |
| show\_affiliate\_type | boolean |
| show\_country | boolean |
| show\_find\_us | boolean |
| show\_first\_name | boolean |
| show\_geos | boolean |
| show\_last\_name | boolean |
| show\_messenger | boolean |
| show\_messenger\_type | boolean |
| show\_payout\_type | boolean |
| show\_payout\_volume | boolean |
| show\_referral | boolean |
| show\_traffic\_type | boolean |
| show\_verticals | boolean |
| show\_verticals\_details | boolean |

}

#/definitions/models.SnapchatMatchingmodels.SnapchatMatching{

|     |     |
| --- | --- |
| conversions\_type | string<br>ConversionsType is type of conversion in Redtrack: default, type1, type20 |
| snapchat\_type | integer<br>SnapchatType is type of conversion in Snapchat: PURCHASE, ADD\_CARD, etc. |

}

#/definitions/models.SnapchatPixelmodels.SnapchatPixel{

|     |     |
| --- | --- |
| pixel\_id | string |
| pixel\_token | string |

}

#/definitions/models.Statmodels.Stat{

|
|

}

#/definitions/models.Streammodels.Stream{

|     |     |
| --- | --- |
| expires\_at | string |
| filters | #/definitions/models.Filtersmodels.Filters{

|     |     |
| --- | --- |
| browser | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| browser\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| city | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| connection\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| country | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| device\_brand | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| device\_model | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| device\_type | #/definitions/models.DeviceTypeFiltermodels.DeviceTypeFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| domain\_referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| fraud | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| ip | #/definitions/models.IPFiltermodels.IPFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| isp | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| languages | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| os | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| os\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| proxy\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| region | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| subs | #/definitions/models.SubsFiltermodels.SubsFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| items | #/definitions/models.SubItemsmodels.SubItems{

|     |     |
| --- | --- |
| sub1 | string |
| sub10 | string |
| sub11 | string |
| sub12 | string |
| sub13 | string |
| sub14 | string |
| sub15 | string |
| sub16 | string |
| sub17 | string |
| sub18 | string |
| sub19 | string |
| sub2 | string |
| sub20 | string |
| sub3 | string |
| sub4 | string |
| sub5 | string |
| sub6 | string |
| sub7 | string |
| sub8 | string |
| sub9 | string |

} |
| kind | integer |

} |
| unique\_visitor | #/definitions/models.UniqueVisitorFiltermodels.UniqueVisitorFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |

} |

} |
| id | string |
| landings | \[#/definitions/models.StreamLandingmodels.StreamLanding{\
\
|     |     |\
| --- | --- |\
| filters | #/definitions/models.Filtersmodels.Filters{\
\
|     |     |\
| --- | --- |\
| browser | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| browser\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| city | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| connection\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| country | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_brand | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_model | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_type | #/definitions/models.DeviceTypeFiltermodels.DeviceTypeFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| domain\_referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| fraud | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| ip | #/definitions/models.IPFiltermodels.IPFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| isp | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| languages | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| proxy\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| region | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| subs | #/definitions/models.SubsFiltermodels.SubsFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| items | #/definitions/models.SubItemsmodels.SubItems{\
\
|     |     |\
| --- | --- |\
| sub1 | string |\
| sub10 | string |\
| sub11 | string |\
| sub12 | string |\
| sub13 | string |\
| sub14 | string |\
| sub15 | string |\
| sub16 | string |\
| sub17 | string |\
| sub18 | string |\
| sub19 | string |\
| sub2 | string |\
| sub20 | string |\
| sub3 | string |\
| sub4 | string |\
| sub5 | string |\
| sub6 | string |\
| sub7 | string |\
| sub8 | string |\
| sub9 | string |\
\
} |\
| kind | integer |\
\
} |\
| unique\_visitor | #/definitions/models.UniqueVisitorFiltermodels.UniqueVisitorFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
\
} |\
\
} |\
| id | string |\
| name | string |\
| weight | integer |\
\
}\] |
| offers | \[#/definitions/models.StreamOffermodels.StreamOffer{\
\
|     |     |\
| --- | --- |\
| filters | #/definitions/models.Filtersmodels.Filters{\
\
|     |     |\
| --- | --- |\
| browser | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| browser\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| city | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| connection\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| country | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_brand | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_model | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_type | #/definitions/models.DeviceTypeFiltermodels.DeviceTypeFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| domain\_referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| fraud | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| ip | #/definitions/models.IPFiltermodels.IPFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| isp | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| languages | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| proxy\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| region | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| subs | #/definitions/models.SubsFiltermodels.SubsFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| items | #/definitions/models.SubItemsmodels.SubItems{\
\
|     |     |\
| --- | --- |\
| sub1 | string |\
| sub10 | string |\
| sub11 | string |\
| sub12 | string |\
| sub13 | string |\
| sub14 | string |\
| sub15 | string |\
| sub16 | string |\
| sub17 | string |\
| sub18 | string |\
| sub19 | string |\
| sub2 | string |\
| sub20 | string |\
| sub3 | string |\
| sub4 | string |\
| sub5 | string |\
| sub6 | string |\
| sub7 | string |\
| sub8 | string |\
| sub9 | string |\
\
} |\
| kind | integer |\
\
} |\
| unique\_visitor | #/definitions/models.UniqueVisitorFiltermodels.UniqueVisitorFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
\
} |\
\
} |\
| id | string |\
| name | string |\
| weight | integer |\
\
}\] |
| prelandings | \[#/definitions/models.StreamLandingmodels.StreamLanding{\
\
|     |     |\
| --- | --- |\
| filters | #/definitions/models.Filtersmodels.Filters{\
\
|     |     |\
| --- | --- |\
| browser | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| browser\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| city | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| connection\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| country | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_brand | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_model | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| device\_type | #/definitions/models.DeviceTypeFiltermodels.DeviceTypeFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| domain\_referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| fraud | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| ip | #/definitions/models.IPFiltermodels.IPFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| isp | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| languages | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| os\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| proxy\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| region | #/definitions/models.ValuesFiltermodels.ValuesFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
| values | \[string\] |\
\
} |\
| subs | #/definitions/models.SubsFiltermodels.SubsFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| items | #/definitions/models.SubItemsmodels.SubItems{\
\
|     |     |\
| --- | --- |\
| sub1 | string |\
| sub10 | string |\
| sub11 | string |\
| sub12 | string |\
| sub13 | string |\
| sub14 | string |\
| sub15 | string |\
| sub16 | string |\
| sub17 | string |\
| sub18 | string |\
| sub19 | string |\
| sub2 | string |\
| sub20 | string |\
| sub3 | string |\
| sub4 | string |\
| sub5 | string |\
| sub6 | string |\
| sub7 | string |\
| sub8 | string |\
| sub9 | string |\
\
} |\
| kind | integer |\
\
} |\
| unique\_visitor | #/definitions/models.UniqueVisitorFiltermodels.UniqueVisitorFilter{\
\
|     |     |\
| --- | --- |\
| active | boolean |\
| comparison\_type | string |\
| exclude | boolean |\
| kind | integer |\
\
} |\
\
} |\
| id | string |\
| name | string |\
| weight | integer |\
\
}\] |
| template | boolean |
| title | string |
| user\_id | string |

}

#/definitions/models.StreamLandingmodels.StreamLanding{

|     |     |
| --- | --- |
| filters | #/definitions/models.Filtersmodels.Filters{

|     |     |
| --- | --- |
| browser | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| browser\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| city | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| connection\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| country | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| device\_brand | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| device\_model | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| device\_type | #/definitions/models.DeviceTypeFiltermodels.DeviceTypeFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| domain\_referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| fraud | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| ip | #/definitions/models.IPFiltermodels.IPFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| isp | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| languages | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| os | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| os\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| proxy\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| region | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| subs | #/definitions/models.SubsFiltermodels.SubsFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| items | #/definitions/models.SubItemsmodels.SubItems{

|     |     |
| --- | --- |
| sub1 | string |
| sub10 | string |
| sub11 | string |
| sub12 | string |
| sub13 | string |
| sub14 | string |
| sub15 | string |
| sub16 | string |
| sub17 | string |
| sub18 | string |
| sub19 | string |
| sub2 | string |
| sub20 | string |
| sub3 | string |
| sub4 | string |
| sub5 | string |
| sub6 | string |
| sub7 | string |
| sub8 | string |
| sub9 | string |

} |
| kind | integer |

} |
| unique\_visitor | #/definitions/models.UniqueVisitorFiltermodels.UniqueVisitorFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |

} |

} |
| id | string |
| name | string |
| weight | integer |

}

#/definitions/models.StreamOffermodels.StreamOffer{

|     |     |
| --- | --- |
| filters | #/definitions/models.Filtersmodels.Filters{

|     |     |
| --- | --- |
| browser | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| browser\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| city | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| connection\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| country | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| device\_brand | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| device\_model | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| device\_type | #/definitions/models.DeviceTypeFiltermodels.DeviceTypeFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| domain\_referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| fraud | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| ip | #/definitions/models.IPFiltermodels.IPFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| isp | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| languages | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| os | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| os\_version | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| proxy\_type | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| referrer | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| region | #/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

} |
| subs | #/definitions/models.SubsFiltermodels.SubsFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| items | #/definitions/models.SubItemsmodels.SubItems{

|     |     |
| --- | --- |
| sub1 | string |
| sub10 | string |
| sub11 | string |
| sub12 | string |
| sub13 | string |
| sub14 | string |
| sub15 | string |
| sub16 | string |
| sub17 | string |
| sub18 | string |
| sub19 | string |
| sub2 | string |
| sub20 | string |
| sub3 | string |
| sub4 | string |
| sub5 | string |
| sub6 | string |
| sub7 | string |
| sub8 | string |
| sub9 | string |

} |
| kind | integer |

} |
| unique\_visitor | #/definitions/models.UniqueVisitorFiltermodels.UniqueVisitorFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |

} |

} |
| id | string |
| name | string |
| weight | integer |

}

#/definitions/models.StreamOptimizationmodels.StreamOptimization{

|     |     |
| --- | --- |
| clicks\_limit | integer |
| conversion\_types | \[string\] |
| count | integer |
| is\_enabled | boolean |
| limit | integer |
| metric | string |
| multiplicator | number |
| subs | \[string\] |
| threshold | number |
| winner\_share\_limit | integer |

}

#/definitions/models.SubCategorymodels.SubCategory{

|     |     |
| --- | --- |
| alias | string |
| name | string |

}

#/definitions/models.SubItemsmodels.SubItems{

|     |     |
| --- | --- |
| sub1 | string |
| sub10 | string |
| sub11 | string |
| sub12 | string |
| sub13 | string |
| sub14 | string |
| sub15 | string |
| sub16 | string |
| sub17 | string |
| sub18 | string |
| sub19 | string |
| sub2 | string |
| sub20 | string |
| sub3 | string |
| sub4 | string |
| sub5 | string |
| sub6 | string |
| sub7 | string |
| sub8 | string |
| sub9 | string |

}

#/definitions/models.SubsFiltermodels.SubsFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| items | #/definitions/models.SubItemsmodels.SubItems{

|     |     |
| --- | --- |
| sub1 | string |
| sub10 | string |
| sub11 | string |
| sub12 | string |
| sub13 | string |
| sub14 | string |
| sub15 | string |
| sub16 | string |
| sub17 | string |
| sub18 | string |
| sub19 | string |
| sub2 | string |
| sub20 | string |
| sub3 | string |
| sub4 | string |
| sub5 | string |
| sub6 | string |
| sub7 | string |
| sub8 | string |
| sub9 | string |

} |
| kind | integer |

}

#/definitions/models.TableSettingsmodels.TableSettings{

|     |     |
| --- | --- |
| custom\_columns | \[\
\
Custom contains formula to calculate custom column and other additional info\
\
Custom columns saving for table, not for template.\
\
#/definitions/models.CustomColumnmodels.CustomColumn{\
\
|     |     |\
| --- | --- |\
| description | string |\
| format | integer<br>Format stores info for frontend |\
| formula | string<br>contains formula i.e. “roi\*2” |\
| id | string |\
| name | string<br>Name contains user’s name of column |\
| variable\_ids | \[<br>VariableIDs contains unique column ids that uses in formula<br>string\] |\
\
}\] |
| templates | \[#/definitions/models.TableTemplatemodels.TableTemplate{\
\
|     |     |\
| --- | --- |\
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |\
| enabled | boolean<br>Should we use this template or not |\
| id | string<br>Template id |\
\
}\] |

}

#/definitions/models.TableTemplatemodels.TableTemplate{

|     |     |
| --- | --- |
| columns | \[\
\
Columns is a list of active and disabled columns in a table\
\
#/definitions/models.ColumnSettingsmodels.ColumnSettings{\
\
|     |     |\
| --- | --- |\
| color\_enabled | boolean<br>ColorEnabled allows to enable/disable row highlighting according to column. Only one column can have true value. |\
| enabled | boolean<br>Show column in a table or not |\
| id | string<br>Column id |\
| is\_custom\_column | boolean<br>IsCustom == true if column is custom |\
\
}\] |
| enabled | boolean<br>Should we use this template or not |
| id | string<br>Template id |

}

#/definitions/models.TrackViewmodels.TrackView{

|     |     |
| --- | --- |
| browser | string |
| campaign | string |
| campaign\_id | string |
| city | string |
| connection\_type | string |
| cost | number |
| cost\_default | number |
| cost\_source | number |
| country | string |
| deeplink | string |
| device | string |
| device\_brand | string |
| device\_fullname | string |
| external\_id | string |
| fingerprint | string |
| id | string |
| ip | string |
| is\_attribution | integer |
| is\_baddevice | integer |
| is\_blacklist | integer |
| is\_datacenter | integer |
| is\_lp\_track | integer |
| is\_ok | integer |
| is\_prelp\_track | integer |
| isp | string |
| landing | string |
| landing\_id | string |
| network | string |
| offer | string |
| offer\_id | string |
| os | string |
| page | string |
| prelanding | string |
| prelanding\_id | string |
| program\_id | string |
| ref\_id | string |
| referer | string |
| region | string |
| rt\_ad | string |
| rt\_ad\_id | string |
| rt\_adgroup | string |
| rt\_adgroup\_id | string |
| rt\_campaign | string |
| rt\_campaign\_id | string |
| rt\_keyword | string |
| rt\_medium | string |
| rt\_placement | string |
| rt\_placement\_hashed | string |
| rt\_placement\_id | string |
| rt\_role\_1 | string |
| rt\_role\_2 | string |
| rt\_source | string |
| server | string |
| source | string |
| source\_id | string |
| sub1 | string |
| sub10 | string |
| sub11 | string |
| sub12 | string |
| sub13 | string |
| sub14 | string |
| sub15 | string |
| sub16 | string |
| sub17 | string |
| sub18 | string |
| sub19 | string |
| sub2 | string |
| sub20 | string |
| sub3 | string |
| sub4 | string |
| sub5 | string |
| sub6 | string |
| sub7 | string |
| sub8 | string |
| sub9 | string |
| track\_time | string |
| type | string |
| uniq | integer |
| user\_agent | string |
| user\_id | string |

}

#/definitions/models.URLPostbackmodels.URLPostback{

|     |     |
| --- | --- |
| url | string |

}

#/definitions/models.UniqueVisitorFiltermodels.UniqueVisitorFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |

}

#/definitions/models.ValuesFiltermodels.ValuesFilter{

|     |     |
| --- | --- |
| active | boolean |
| comparison\_type | string |
| exclude | boolean |
| kind | integer |
| values | \[string\] |

}

#/definitions/protobuf.CustomSslprotobuf.CustomSsl{

|     |     |
| --- | --- |
| active | boolean |
| crt | string |
| error | string |
| expires | string |
| key | string |

}

#/definitions/protobuf.Domainprotobuf.Domain{

|     |     |
| --- | --- |
| acme | #/definitions/protobuf.CustomSslprotobuf.CustomSsl{

|     |     |
| --- | --- |
| active | boolean |
| crt | string |
| error | string |
| expires | string |
| key | string |

} |
| created\_at | string |
| fallback\_url | string |
| id | string |
| ssl | #/definitions/protobuf.CustomSslprotobuf.CustomSsl{

|     |     |
| --- | --- |
| active | boolean |
| crt | string |
| error | string |
| expires | string |
| key | string |

} |
| type | string |
| url | string |
| use\_auto\_generated\_ssl | boolean |
| user\_id | string |

}

#/definitions/providers.Languageproviders.Language{

|     |     |
| --- | --- |
| alpha3 | string |
| code | string |
| title | string |

}

#/definitions/publishers.NewPublisherBodypublishers.NewPublisherBody{

|     |     |
| --- | --- |
| affiliate\_types | \[integer\] |
| billing\_details | string |
| company\_type | string |
| contact\_details | string |
| country | string |
| email | string |
| find\_us | integer<br>How did you hear about us? |
| find\_us\_details | string |
| firstname | string |
| geos | \[integer\] |
| language | string |
| lastname | string |
| manager\_email | string |
| messenger | string |
| messenger\_type | string |
| password | string |
| payout\_types | \[integer\] |
| payout\_volume | integer<br>What is your monthly volume for your offers |
| referral | boolean |
| referral\_details | string |
| traffic\_types | \[integer\] |
| traffic\_types\_details | string |
| verticals | \[integer\] |
| verticals\_details | string |

}

#/definitions/referral.ActiveProgramSettingsreferral.ActiveProgramSettings{

|     |     |
| --- | --- |
| first\_step\_percent | integer |
| is\_enabled | boolean |
| maximum\_steps | integer |
| step\_decrement | integer |

}

#/definitions/referral.FinancialDatareferral.FinancialData{

|     |     |
| --- | --- |
| approved\_recommender\_commission\_for\_referral | number |
| approved\_referral\_commission | number |
| not\_approved\_recommender\_commission\_for\_referral | number |
| not\_approved\_referral\_commission | number |
| referral\_commission\_paid | number |
| total\_commission | number |
| total\_referral\_commission | number<br>deprecated |

}

#/definitions/referral.Referralreferral.Referral{

|     |     |
| --- | --- |
| active\_program\_settings | #/definitions/referral.ActiveProgramSettingsreferral.ActiveProgramSettings{

|     |     |
| --- | --- |
| first\_step\_percent | integer |
| is\_enabled | boolean |
| maximum\_steps | integer |
| step\_decrement | integer |

} |
| email | string |
| financial\_data | #/definitions/referral.FinancialDatareferral.FinancialData{

|     |     |
| --- | --- |
| approved\_recommender\_commission\_for\_referral | number |
| approved\_referral\_commission | number |
| not\_approved\_recommender\_commission\_for\_referral | number |
| not\_approved\_referral\_commission | number |
| referral\_commission\_paid | number |
| total\_commission | number |
| total\_referral\_commission | number<br>deprecated |

} |
| id | string |
| invited\_by\_email | string |
| invited\_by\_id | string |
| referral\_program\_approved | boolean |
| registration\_date | string |
| status | string |

}

#/definitions/referral.Reportreferral.Report{

|     |     |
| --- | --- |
| pagination | #/definitions/models.Paginationmodels.Pagination{

|     |     |
| --- | --- |
| limit | integer |
| page | integer |
| total | integer |

} |
| publishers | \[#/definitions/referral.Referralreferral.Referral{\
\
|     |     |\
| --- | --- |\
| active\_program\_settings | #/definitions/referral.ActiveProgramSettingsreferral.ActiveProgramSettings{\
\
|     |     |\
| --- | --- |\
| first\_step\_percent | integer |\
| is\_enabled | boolean |\
| maximum\_steps | integer |\
| step\_decrement | integer |\
\
} |\
| email | string |\
| financial\_data | #/definitions/referral.FinancialDatareferral.FinancialData{\
\
|     |     |\
| --- | --- |\
| approved\_recommender\_commission\_for\_referral | number |\
| approved\_referral\_commission | number |\
| not\_approved\_recommender\_commission\_for\_referral | number |\
| not\_approved\_referral\_commission | number |\
| referral\_commission\_paid | number |\
| total\_commission | number |\
| total\_referral\_commission | number<br>deprecated |\
\
} |\
| id | string |\
| invited\_by\_email | string |\
| invited\_by\_id | string |\
| referral\_program\_approved | boolean |\
| registration\_date | string |\
| status | string |\
\
}\] |

}

#/definitions/requests.Scriptrequests.Script{

|     |     |
| --- | --- |
| attribution\_type | integer |
| attribution\_window | integer |
| campaign\_id | string<br>InvitedBy points to referral inviter. Could be empty. |
| cookie\_domain | string |
| domain\_id | string<br>InvitedBy points to referral inviter. Could be empty. |
| name | string |
| script\_type | integer |

}

#/definitions/responses.Scriptresponses.Script{

|     |     |
| --- | --- |
| attribution\_type | integer |
| attribution\_window | integer |
| campaign\_id | string<br>InvitedBy points to referral inviter. Could be empty. |
| cookie\_domain | string |
| domain\_id | string<br>InvitedBy points to referral inviter. Could be empty. |
| id | string<br>InvitedBy points to referral inviter. Could be empty. |
| is\_auto\_generated | boolean |
| name | string |
| reg\_view\_once | boolean |
| script\_code | string |
| script\_type | integer |

nythi