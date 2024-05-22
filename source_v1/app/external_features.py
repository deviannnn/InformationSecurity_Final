import requests
from datetime import datetime
from bs4 import BeautifulSoup

#################################################################################################################################
#               Domain age of a url
#################################################################################################################################

def domain_age(key, domain):
    try:
        r = 'whois'
        domain = domain.split("//")[-1].split("/")[0].split('?')[0]
        res = requests.get('https://api.whoapi.com', dict(domain=domain, r=r, apikey=key))
        if res.status_code == 200:
            data = res.json()
            if int(data['status']) == 0:
                date_created = datetime.strptime(data['date_created'], "%Y-%m-%d %H:%M:%S")
                today = datetime.today()
                domain_age = today - date_created
                return domain_age.days
            else:
                return -2
        else:
            return -1
    except:
        return -1
    

#################################################################################################################################
#               Google index
#################################################################################################################################
from urllib.parse import urlencode

def google_index(url):
    user_agent =  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    headers = {'User-Agent' : user_agent}
    query = {'q': 'site:' + url}
    google = "https://www.google.com/search?" + urlencode(query)
    data = requests.get(google, headers=headers)
    data.encoding = 'ISO-8859-1'
    soup = BeautifulSoup(str(data.content), "html.parser")
    try:
        if 'Our systems have detected unusual traffic from your computer network.' in str(soup):
            return -1
        check = soup.find(id="rso").find("div").find("div").find("a")

        if check and check['href']:
            return 0
        else:
            return 1
        
    except AttributeError:
        return 1


#################################################################################################################################
#               Page rank
#################################################################################################################################

def page_rank(key, domain):
    url = 'https://openpagerank.com/api/v1.0/getPageRank?domains%5B0%5D=' + domain
    try:
        res = requests.get(url, headers={'API-OPR':key})
        data = res.json()
        data = data['response'][0]['page_rank_integer']
        if data:
            return data
        else:
            return 0
    except:
        return -1