#2  Information about the company and job, url and location of the job 
#https://careerindex.jp/job_offers/36836422 number is 36836533
from bs4 import BeautifulSoup as bs
import urllib.request
import re
import json
from ordered_set import OrderedSet 

class InfoExtractor:
    def __init__(self, jsonFile, csvFile): 
        self.url = "https://careerindex.jp/job_offers/"
        self.jsonFile = str(jsonFile)
        self.csvFile = str(csvFile)
    
    def keyList(self, jsonFile):
        with open(str(jsonFile), 'r', encoding='utf8') as json_file:
            loaded_json = json.loads(json_file.read())

        titles = OrderedSet()
        titles.update('ID') #### 'ID'
        for k, v in loaded_json.items():
            #print(v.keys())

            for title in v.keys():
                titles.update([title])
        print("----------KEY LIST-------")
        print(titles)
        return list(titles)

    def convertJsontoCSV(self, titles):
        import json
        csv_file = open(self.csvFile, 'a')
        with open(self.jsonFile, 'r', encoding='utf8') as json_file:
            loaded_json = json.loads(json_file.read())
        value = ""
        for company_id,data in loaded_json.items():
            value = company_id+"|" #set id to output string
            for title in titles:
                if title in data.keys():
                    value = value + str(data[title]+"|")
                else:
                    value = value + " |"
            csv_file.write(value+"\n")
        print("---------INFO EXTRACTION-------")
        print("Data Converted from JSON to CSV")




    def extractor(self, idFile, classRequest):
        # iteration = 0 # for testings
        # limit = 1

        #get ids file and iterate
        headList = ''
        dataList = ''
        print(classRequest)
        
        headList= str(classRequest)+"head"
        dataList= str(classRequest)+"data"
    
        job_numbers = open(idFile.name, 'r').read().split()
        all_data = {}


        for job_number in job_numbers:
            
            #fetch the html of the particular job listing
            number = str(job_number)
            url = self.url+number
            try:
                page = urllib.request.urlopen(url)
            except:
                print("An error occured.")
            soup = bs(page, 'html.parser')
            #create company/req/other/apply functions 
            print(dataList, headList)
            content_data = soup.find_all('div', attrs={'class': dataList})
            content_head = soup.find_all('div', attrs={'class': headList})
            
            data_keys = [] 
            data_values = []
            
            for i in content_head:
                head = bs(str(i), 'html.parser')
                data_keys.append(head.text)
            for i in content_data:
                data = bs(str(i), 'html.parser')
                data_values.append(data.text)
                
            zipper = zip(data_keys, data_values)
            
            data_dict = dict(zipper)
            print(data_dict)
            all_data[job_number] = data_dict
            print(job_number)

            # # loop 
            # if iteration>limit:
            #     break
            # iteration = iteration + 1

        print("------Data Extraction------")        
        print("Data Extraction completed ")  


        with open(self.jsonFile, 'w', encoding='utf8') as json_file:
            json.dump(all_data, json_file, ensure_ascii=False)
        titles = self.keyList(self.jsonFile)
        with open(self.csvFile, 'a', encoding='utf8') as  csv_file:
            csv_file.write("ID |")
            for title in titles:
                csv_file.write(str(title)+"|")
            csv_file.write("\n  ")
        self.convertJsontoCSV(titles)
            