pip install python-whois
pip install futures
import python-whois
import whois
import datetime

def domain_registration(url):
    w = whois.whois(url)
    updated = w.updated_date
    exp = w.expiration_date
    length = (exp[0]-updated[0]).days
    if(length<=365):
        return 1
    else:
        return -1
    
def age_of_domain(url):
    w = whois.whois(url)
    start_date = w.creation_date
    current_date = datetime.datetime.now()
    age =(current_date-start_date[0]).days
    if(age>=180):
        return -1
    else:
        return 1

>>> import seolib 
>>> alexa_rank = seolib.get_alexa('http://google.com')
>>> print alexa_rank

pip install beautifulsoup4
from bs4 import BeautifulSoup
pip install urllib3
import urllib
def Links_in_tags(url):
    opener = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(opener, 'lxml')
    no_of_meta =0
    no_of_link =0
    no_of_script =0
    anchors=0
    avg =0
    for meta in soup.find_all('meta'):
        no_of_meta = no_of_meta+1
    for link in soup.find_all('link'):
        no_of_link = no_of_link +1
    for script in soup.find_all('script'):
        no_of_script = no_of_script+1
    for anchor in soup.find_all('a'):
        anchors = anchors+1
    total = no_of_meta + no_of_link + no_of_script+anchors
    tags = no_of_meta + no_of_link + no_of_script
    if(total!=0):
        avg = tags/total
    if(avg<0.25):
        return -1
    elif(0.25<=avg<=0.81):
        return 0
    else:
        return 1        
