import re

url = "https://careerindex.jp/job_offers?&s%5Bagent%5D=0&s%5Bannual_income%5D=&s%5Bemployment%5D%5B%5D=03001&s%5Bemployment%5D%5B%5D=03002&s%5Bfeature%5D%5B%5D=19001&s%5Bnew_arrival%5D=0&s%5Boccupation%5D%5B%5D=05&s%5Bprefecture%5D%5B%5D=13&s%5Bprefecture%5D%5B%5D=14&s%5Bprefecture%5D%5B%5D=11&s%5Bprefecture%5D%5B%5D=12&s%5Bword%5D=&s%5Bword_search_type%5D=all&utf820"
spl = re.split("\?\&", url)
print(str(spl[1]))

url2 = "https://careerindex.jp/job_offers?page=26&s%5Bagent%5D=0&s%5Bannual_income%5D=&s%5Bemployment%5D%5B%5D=03001&s%5Bemployment%5D%5B%5D=03002&s%5Bfeature%5D%5B%5D=19001&s%5Bnew_arrival%5D=0&s%5Boccupation%5D%5B%5D=05&s%5Bprefecture%5D%5B%5D=13&s%5Bprefecture%5D%5B%5D=14&s%5Bprefecture%5D%5B%5D=11&s%5Bprefecture%5D%5B%5D=12&s%5Bword%5D=&s%5Bword_search_type%5D=all&utf820"

url2 = re.split("page=[0-9]*\&", url2)
print(str(url2[1]))

