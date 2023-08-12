class WebScraper(): 
    ##adding free proxies to rotate
    ##from proxy import Proxyscrape
    ##setting real header
    ##headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

    ##creating list with free proxies
    ##proxylist = Proxyscrape.getProxies()
    ##finalist = Proxyscrape.extract(proxylist)
    ##for i in finalist:
        ##if i == 0:
            ##finalist.remove()

    def create_csv(url):
        import csv
        import re
        import random
        ##selecting random ip address
        ##ran = random.choice(self.proxylist)
        import requests
        from bs4 import BeautifulSoup
        page = requests.get(url) 
        ##headers=self.headers, proxies = {'http' : ran,'https': ran})
        startindex = url.find('NBA_') + 4
        endindex = url.find('_per')
        year_number = url[startindex:endindex]
      

        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table',id ="per_game_stats")

        #find all rows
        rows = table.findAll('tr')

        # strip the header from rows
        headers = rows[0]
        header_text = ['Year']

        # add the table header text to array
        for th in headers.findAll('th'):
            header_text.append(th.text)

        # init row text array
        row_text_array = []

        # loop through rows and add row text to array
        for row in rows[1:]:
            row_text = [year_number]
        # loop through the elements
            for row_element in row.findAll(['th', 'td']):
        # append the array with the elements inner text
                row_text.append(row_element.text.replace('\n', '').strip())
         # append the text array to the row text array
            row_text_array.append(row_text)

        with open((year_number + ".csv"), "w",  encoding="utf-8") as f:
            wr = csv.writer(f)
            wr.writerow(header_text)
            for row_text_single in row_text_array:
                wr.writerow(row_text_single) 


    def mvp(url):
        import csv
        import re
        import random
        ##ran = random.choice(self.proxylist)
        import requests
        from bs4 import BeautifulSoup

        page = requests.get(url) 
        ##headers=self.headers, proxies = {'http' : ran,'https': ran})

        soup = BeautifulSoup(page.content, 'html.parser')
        tempinfo = soup.find("div", id = "meta")
        listofaccolades = tempinfo.find_all('a')
        mvp = ''
        num = 0
        for i in listofaccolades: 
            if num == 5:
                mvp = i.text
            num = num+1
        return str(mvp)

    def teamrecordnum(teamurl):
        import csv
        import re
        import random
        import requests
        from bs4 import BeautifulSoup
        ##ran = random.choice(self.proxylist)
        page = requests.get(teamurl) ##headers=self.headers, proxies = {'http' : ran,'https': ran})

        soupnum = BeautifulSoup(page.content, 'html.parser')
        tempinfonum = soupnum.find("div", id = "meta")

        ##finding all paragraphs on webpage
        listofstats = tempinfonum.find_all('p')

        #isolating paragraph that includes record
        teamrecord = listofstats[2]

        teamrecordstring = str(teamrecord)

        ##isolating the actual substring in paragraph - the record, using indexes
        endindex = teamrecordstring.index("Finished") - 2
        ## -2 used to remove comma and spaces, +18 used to remove </strong> and spaces
        startindex = teamrecordstring.index("</strong>") + 18
        teamrecordnum = teamrecordstring[startindex:endindex]
        
        return str(teamrecordnum)

    def teamrecordsetup(self, teamurl):
        import csv
        import re
        import random
        import pandas as pd
        import requests
        from bs4 import BeautifulSoup as bs
        import lxml
        ##ran = random.choice(self.proxylist)
        ##gathering data from webpage, isolating the name and team of each player 
        r = requests.get(teamurl) ##headers=self.headers, proxies = {'http' : ran,'https': ran})
        soup = bs(r.content, 'lxml')
        table = pd.read_html(str(soup.select_one('table:has(th:-soup-contains("Rk"))')))[0]
        columns = ['Player','Tm']
        table = table.loc[:, columns].iloc[:, :2]
        table.columns = columns
        w, h = 3, len(table)
        masterlist = [[0 for x in range(w)] for y in range(h)] 
        year_number = re.findall(r'\d+', teamurl)

        ##this sets up the list with player name, team and record (record has a 0)
        for i in range(len(table)):
            for j in range(2):
                masterlist[i][j] = table.iloc[i][j]
    
        return(masterlist)

    


 

        
     
