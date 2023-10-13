


from bs4 import BeautifulSoup

def process(path):
   file = open(path)
   soup = BeautifulSoup(file)
   lst = soup.find_all('a')
   return len(lst)

