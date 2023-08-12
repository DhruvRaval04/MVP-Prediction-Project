class Proxyscrape():


   

    #get the list of free proxies
    def getProxies():
        import requests
        from bs4 import BeautifulSoup
        import random
        r = requests.get('https://free-proxy-list.net/')
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('tbody')
        proxies = []
        for row in table:
            if row.find_all('td')[4].text =='elite proxy':
                proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
                proxies.append(proxy)
            else:
                pass
        return proxies

    def extract(proxylist):
        import requests
        from bs4 import BeautifulSoup
        import random
        #this was for when we took a list into the function, without conc futures.
        #proxy = random.choice(proxylist)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
        for i in proxylist:
            proxy = i
            try:
            #change the url to https://httpbin.org/ip that doesnt block anything
                r = requests.get('https://httpbin.org/ip', headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=1)
                if r.status_code ==503:
                    i = 0
            except requests.ConnectionError as err:
                i = 0
            except requests.ReadTimeout:
                i = 0
        
        return proxylist






