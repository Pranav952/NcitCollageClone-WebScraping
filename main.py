from bs4 import  BeautifulSoup
import  requests
response=requests.get('https://pu.edu.np/')
soup=BeautifulSoup(response.text,'html.parser')
print(soup.prettify())