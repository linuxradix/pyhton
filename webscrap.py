
#!/usr/bin/python
# coding: utf-8

# # Immoscout24.de Scraper
# 
# Ein Script zum dumpen (in `.csv` schreiben) von Immobilien, welche auf [immoscout24.de](http://immoscout24.de) angeboten werden

# In[5]:

from bs4 import BeautifulSoup
import json
import urllib.request as urllib2
import random
from random import choice
import time

# In[7]:

# urlquery from Achim Tack. Thank you!
# https://github.com/ATack/GoogleTrafficParser/blob/master/google_traffic_parser.py
def urlquery(url):
    # function cycles randomly through different user agents and time intervals to simulate more natural queries
    try:
        sleeptime = float(random.randint(1,6))/5
        time.sleep(sleeptime)

        agents = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17',
        'Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0',
        'Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02',
        'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Mozilla/3.0',
        'Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543a Safari/419.3',
        'Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522+ (KHTML, like Gecko) Safari/419.3',
        'Opera/9.00 (Windows NT 5.1; U; en)']

        agent = choice(agents)
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', agent)]

        html = opener.open(url).read()
        time.sleep(sleeptime)
        
        return html

    except Exception as e:
         print('Something went wrong with Crawling:\n%s' % e)

# In[9]:

def immoscout24parser(url):
    
    ''' Parser holt aus Immoscout24.de Suchergebnisseiten die Immobilien '''
    
    try:
        soup = BeautifulSoup(urlquery(url), 'html.parser')
        scripts = soup.findAll('script')
        for script in scripts:
            #print script.text.strip()
            if 'IS24.resultList' in script.text.strip():
                s = script.string.split('\n')
                for line in s:
                    #print('\n\n\'%s\'' % line)
                    if line.strip().startswith('resultListModel'):
                        resultListModel = line.strip('resultListModel: ')
                        immo_json = json.loads(resultListModel[:-1])

                        searchResponseModel = immo_json[u'searchResponseModel']
                        resultlist_json = searchResponseModel[u'resultlist.resultlist']
                        
                        return resultlist_json

    except Exception as e:
         print("Fehler in immoscout24 parser: %s" % e)

# ## Main Loop
# 
# Geht Wohnungen und HŠuser, jeweils zum Kauf und Miete durch und sammelt die Daten

# In[31]:

immos = {}

b = 'Sachsen' # Bundesland
s = 'Leipzig' # Stadt
k = 'Wohnung' # Wohnung oder Haus
w = 'Kauf' # Miete oder Kauf

page = 0
# print('Suche %s / %s' % (k, w))

while True:
    page+=1
    url = 'http://www.immobilienscout24.de/Suche/S-T/P-%s/%s-%s/%s/-/-/-/-/-/true?pagerReporting=true' % (page, k, w, b)
    #url = 'http://www.immobilienscout24.de/Suche/S-T/P-%s/%s-%s/%s/%s/-/-/-/-/true?pagerReporting=true' % (page, k, w, b, s)
    sites = {}
    # print(url)
    # Because of some timeout or immoscout24.de errors,
    # we try until it works \o/
    resultlist_json = None
    while resultlist_json is None:
        try:
            resultlist_json = immoscout24parser(url)
            numberOfPages = int(resultlist_json[u'paging'][u'numberOfPages'])
            pageNumber = int(resultlist_json[u'paging'][u'pageNumber'])
        except:
            pass

    if page>numberOfPages:
    #if page>1:
        break

    # Get the data
    for resultlistEntry in resultlist_json['resultlistEntries'][0][u'resultlistEntry']:
        realEstate_json = resultlistEntry[u'resultlist.realEstate']
        
        realEstate = {}

        realEstate[u'Miete/Kauf'] = w
        realEstate[u'Haus/Wohnung'] = k

        realEstate['address'] = realEstate_json['address']['description']['text']
        realEstate['city'] = realEstate_json['address']['city']
        realEstate['postcode'] = realEstate_json['address']['postcode']
        realEstate['quarter'] = realEstate_json['address']['quarter']
        try:
            realEstate['lat'] = realEstate_json['address'][u'wgs84Coordinate']['latitude']
            realEstate['lon'] = realEstate_json['address'][u'wgs84Coordinate']['longitude']
        except:
            realEstate['lat'] = None
            realEstate['lon'] = None
            
        realEstate['title'] = realEstate_json['title']

        realEstate['numberOfRooms'] = realEstate_json['numberOfRooms']
        realEstate['livingSpace'] = realEstate_json['livingSpace']
        
        if k=='Wohnung':
            realEstate['balcony'] = realEstate_json['balcony']
            realEstate['builtInKitchen'] = realEstate_json['builtInKitchen']
            realEstate['garden'] = realEstate_json['garden']
            realEstate['price'] = realEstate_json['price']['value']
            realEstate['privateOffer'] = realEstate_json['privateOffer']
        elif k=='Haus':
            realEstate['isBarrierFree'] = realEstate_json['isBarrierFree']
            realEstate['cellar'] = realEstate_json['cellar']
            realEstate['plotArea'] = realEstate_json['plotArea']
            realEstate['price'] = realEstate_json['price']['value']
            realEstate['privateOffer'] = realEstate_json['privateOffer']
        
        realEstate['floorplan'] = realEstate_json['floorplan']
        realEstate['from'] = realEstate_json['companyWideCustomerId']
        realEstate['ID'] = realEstate_json[u'@id']
        realEstate['url'] = u'https://www.immobilienscout24.de/expose/%s' % realEstate['ID']

        immos[realEstate['ID']] = realEstate
        sites[realEstate['ID']] = realEstate['url']
   
    # print("sites")
    # print(sites)
    #print("immos")
    #print(immos)

    for script in sites:
      # print(script)
      # print(sites[script])#['url'])
      url2 = sites[script]
      soup = BeautifulSoup(urlquery(url2), 'html.parser')
      #scripts = soup.findAll('dt')
      scripts2 = soup.findAll('dd')
      #print(scripts2)
      #print(immos[script]) #=scripts2
      aa=0
      bb=0
      miete={}
      #print(scripts2)
      for tt in scripts2:
        str3 = str(tt)
        #print(str3)
        if str3.find("mieteinnahmen-pro-monat")>0:
          # print("here")
          # print(str3)
          # find string position 
          aa = str3.find(">")
          bb = str3.find("</")

          # cut string - take string string[from: to]
          miete = str3[aa+1:bb]

      #print(immos[script])
      #print("")
      #print("test")
      #print("")
      immos[script]['miete'] = miete
      immos[script]['xml'] =scripts2
      #print("")
      #print("test")
      #print("")
      #print(immos[script]['xml'])
      #print("")
      #print("test")
      #print("")
      #print(script)

    print('Scrape Page %i/%i (%i Immobilien %s %s gefunden)' % (page, numberOfPages, len(immos), k, w))


# In[32]:

# print("Scraped %i Immos" % len(immos))

# ## Datenaufbereitung & Cleaning
# 
# Die gesammelten Daten werden in ein sauberes Datenformat konvertiert, welches z.B. auch mit Excel gelesen werden kann. Weiterhin werden die Ergebnisse pseudonymisiert, d.h. die Anbieter bekommen eindeutige Nummern statt Klarnamen.

# In[33]:
#print(immos)
#print(sites)

  
#print(immos) 




from datetime import datetime
timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M')

# In[34]:

import pandas as pd

# In[35]:

df = pd.DataFrame(immos).T
df.index.name = 'ID'

# In[36]:

len(df)

# In[37]:

df.head()

# ## Alles Dumpen

# In[38]:

f = open('%s-%s-%s.csv' % (timestamp, k, w), 'w')
f.write('# %s %s from immoscout24.de on %s\n' % (k,w,timestamp))
df[(df['Haus/Wohnung']==k) & (df['Miete/Kauf']==w)].to_csv(f, encoding='utf-8')
f.close()
print("scraping..")
# In[39]:

#df.to_excel('%s-%s-%s.xlsx' % (timestamp, k, w))

# Fragen? [@Balzer82](https://twitter.com/Balzer82)


