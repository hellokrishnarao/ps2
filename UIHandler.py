from IDExtractor import IDExtractor 
from InfoExtractor import InfoExtractor
import re
url = input("\n\n---------Enter the URL ------------\n\n")
url = re.split("\?\&", url)

print("Enter page: start and end page")
pageFrom = int(input())
pageTo = int(input())
print('-----------------------------------------------')
urlFile = open('urlfile.txt', 'r').read()
urlPart1 = 'https://careerindex.jp/job_offers?page='
urlPart2 = str(url[1])


id = IDExtractor(urlPart1,urlPart2, pageFrom, pageTo)
jsonFile, csvFile, idList = id.idExtractor()

print(url)
print(jsonFile)
print(csvFile)

results = InfoExtractor(jsonFile, csvFile)

classList  = ['requirements__', 'company_data__', 'apply_data__']
request = input(print("\n\nEnter the data \n1. Requirements\n2. Company Data\n3. Application Data"))
request = int(request)
if int(request) == 1:
    classRequest = classList[0]
elif int(request) ==2:
    classRequest = classList[1]
elif int(request) ==3:
    classRequest = classList[2]
else: 
    print("Wrong option")
    exit()


results.extractor(idList, classRequest)

