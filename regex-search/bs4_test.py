from bs4 import BeautifulSoup
import requests

''' GLOBAL VARS'''
MAX_TABLE = 1 #100      # the number of data that will be added to csv
RM_STR = '[email'

'''
    Creates a data storing class of Table that stores attributes:
    expression name, expression, description and author
'''
class Table: 
    def __init__(self, exp_name, exp, description, author):
        self.exp_name = exp_name

        result = exp.find(RM_STR)       # gets rid of '[email protected]'
        if result != -1:        
            exp = exp[result:]          # cuts string up to result and then up to ']'
            j = 0
            while j < len(exp) and exp[j] != ']':
                j += 1
            exp = exp[j+1:]

        self.exp = exp
        description =  description.split('\n')[0]
        self.description = description
        self.author = author
    
    '''
    writes content into a csv file for given table
    '''
    def write_into_file(self):
        print("Writing attributes into csv file...")        
    
    '''
    displays the table class objects
    '''
    def print_table(self):
        print("Title: " + self.exp_name)
        print("Expression: " + self.exp)
        print("Description: " + self.description)
        print("Author: " + self.author)
        print("------xxx------")


def create_table(table):
    try:
        all_as = table.find_all('a')        # creates an array of all a tags
        exp_name = all_as[2].text.strip()   # index [2] holds expression name
        exp_author = all_as[len(all_as) - 1].text.strip() # index [last item] holds expression author

        expression = table.find('div', class_="expressionDiv").text.strip()
        description = table.find('div', class_="overflowFixDiv").text.strip()

    except Exception as e:
        exp_name, exp_author, expression, description = '' 

    table = Table(exp_name, expression, description, exp_author)
    return table

'''web scraping code
given a webpage, up to 5 tables are copied and placed into a csv file'''
webpage = "https://regexlib.com/Search.aspx?k=email&c=-1&m=-1&ps=20"
source = requests.get(webpage).text

soup = BeautifulSoup(source, 'lxml')
table = soup.find_all('table')

list_tables = []

if MAX_TABLE > len(table):
    MAX_TABLE = len(table)

for i in range(MAX_TABLE):
    list_tables.append(create_table(table[i]))

for tab in list_tables:
    tab.print_table()
