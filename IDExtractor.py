from bs4 import BeautifulSoup as bs
import urllib.request
import re
import datetime
import os
from InfoExtractor import InfoExtractor

##########################################################
# creates files - json and csv 
# gathers company info
# returns a list of job ids for the requested URL
##########################################################

jsonFile = ''
csvFile = ''
idList = ''

urlPart1 = ''
urlPart2 = ''
class IDExtractor:
    def __init__(self, urlPart1, urlPart2, pageFrom, pageTo): 
        self.urlPart1 = str(urlPart1)
        self.urlPart2 = str(urlPart2)
        self.pageFrom= int(pageFrom)
        self.pageTo = int(pageTo)
        x = datetime.datetime.now()
        self.directory = str(x.strftime("%A-%X"))

   
    def createFiles(self, directory):

        #creates data directory if it does not exists
        if not os.path.exists(str("data/"+directory)):
	        os.makedirs(str("data/"+directory))

        if os.path.exists(str("data/"+directory)):
            csvFile = "result_in_csv"+".csv"
            jsonFile = "result_in_json"+".json"
            idList = "company_id_list"+".csv"

            try:
                file = open(str("data/"+directory+"/")+csvFile, 'r')
                file.close()
                file = open(str("data/"+directory+"/")+jsonFile, 'r')
                file.close()
                file = open(str("data/"+directory+"/")+idList, 'r')
                file.close()
                return 'Something wrong with the file creation'
            except IOError:
                file = open(str("data/"+directory+"/")+csvFile, 'w')
                self.csvFile =  str("data/"+directory+"/")+csvFile
                file.close()
                file = open(str("data/"+directory+"/")+jsonFile, 'w')
                self.jsonFile = str("data/"+directory+"/")+jsonFile
                file.close()
                file = open(str("data/"+directory+"/")+idList, 'w')
                self.idList = str("data/"+directory+"/")+idList
                file.close()
                print("----------Files created Sucessfully!------------")
                return True, self.jsonFile, self.csvFile, self.idList
    def idExtractor(self):
        
        i = self.pageFrom # page 1
        pageNumber = self.pageTo # number of pages to be searched
        created, jsonFile, csvFile, idList = self.createFiles(self.directory)
        if created != True:
            return 'Error with file creation'
        while(i<pageNumber+1):
            url = self.urlPart1+str(i)+self.urlPart2
            try:
                page = urllib.request.urlopen(url)
            except:
                print("An error occured.")
                print(url)
                exit()
            print("Data fetched on page", i)
            
            soup = bs(page, 'html.parser')
            regex = re.compile('^job')
            
            htmlData = str(soup.find_all('li', attrs={'class': regex}))

            
            list_containing_company_ids = htmlData.split()
            r = re.compile("data-job-offer-id")
            filtered = list(filter(r.match, list_containing_company_ids))    
            
            company_ids = []
            for line in filtered:
                company_id = re.findall(r"\d+", line)
                company_id = int(company_id[0])
                company_ids.append(company_id)
                
                
            i=i+1
            
            with open(self.idList, 'a') as idList:
                for item in company_ids:
                    idList.write("%s\n" % item)
            idList.close()    
        return jsonFile, csvFile, idList   

