from bs4 import BeautifulSoup
import requests

#
# data storing class of Table that stores attributes:
# expression name, expression, description and author
class Table: 
    def __init__(self, exp_name, exp, description, author):
        self.exp_name = exp_name
        self.exp = exp
        # if len(description) > 200:
        #     description = description[0:125]
        description =  description.split('\n')[0]
        self.description = description
        self.author = author
    
    def write_into_file(self):
        print("Writing attributes into csv file...")        
    
    # def print_desc(self):
    #     temp_desc = self.description.split('\n')[0]
    #     print(temp_desc) 

    def print_table(self):
        print("Title: " + self.exp_name)
        print("Expression: " + self.exp)

        print("Description: " + self.description)

        print("Author: " + self.author)
        print("------xxx------")

#
# GLOBAL VARS
MAX_TABLE = 5

def create_table(table):
    try:
        all_as = table.find_all('a')        # creates an array of all a tags
        
        exp_name = all_as[2].text.strip()   # index [2] holds expression name
        exp_author = all_as[3].text.strip() # index [3] holds expression author

        expression = table.find('div', class_="expressionDiv").text.strip()
        description = table.find('div', class_="overflowFixDiv").text.strip()

    except Exception as e:
        exp_name, exp_author, expression, description = '' 

    table = Table(exp_name, expression, description, exp_author)
    return table

#
# web scraping
webpage = "https://regexlib.com/Search.aspx?k=password&c=-1&m=-1&ps=20&AspxAutoDetectCookieSupport=1"
source = requests.get(webpage).text

soup = BeautifulSoup(source, 'lxml')
table = soup.find_all('table')

list_tables = []
list_tables.append(create_table(table[4]))

# count = 0
# while(count != MAX_TABLE ):
#     list_tables.append(table[count])    # list_tables[count].print_table()
#     count += 1

# print("Number of items in the list = ", len(table))
# print("Number of items in created list = ", len(list_tables))


for tab in list_tables:
    tab.print_table()
    # tab.print_desc()

# print(list_tables)