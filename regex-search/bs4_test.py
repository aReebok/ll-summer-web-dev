from bs4 import BeautifulSoup
import requests

#
# data storing class of Table that stores attributes:
# expression name, expression, description and author
class Table: 
    def __init__(self, exp_name, exp, description, author):
        self.exp_name = exp_name
        self.exp = exp
        self.description = description
        self.author = author
    
    def write_into_file(self):
        print("Writing attributes into csv file...")

    def print_table(self):
        print("Title: " + self.exp_name)
        print("Expression: " + self.exp)
        print("Description: " + self.description)
        print("Author: " + self.author)
        print("------xxx------")
#
# web scraping
webpage = "https://regexlib.com/Search.aspx?k=password&c=-1&m=-1&ps=20&AspxAutoDetectCookieSupport=1"
source = requests.get(webpage).text

soup = BeautifulSoup(source, 'lxml')
table = soup.find('table')

count = 0
for a in table.find_all('a'):
    count += 1
    if(count == 3):
        exp_name = a.text.strip()
        # 
    if(count == 4):
        exp_author = a.text.strip()
        # 
expression = table.find('div', class_="expressionDiv").text.strip()
# print(expression.text)

description = table.find('div', class_="overflowFixDiv").text.strip()
# print(description.text)

table = Table(exp_name, expression, description, exp_author)
table.print_table()
