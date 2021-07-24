
'''
This .py takes the 'user_input.txt' file, appends it to the RegExLib.com search link,
and scrapes up to MAX_TABLE different expressions and it's details. Finally, it 
writes these out into a file called 'pg_content.txt' for other files to use.
'''

from os import link
from bs4 import BeautifulSoup
import requests

import csv


''' GLOBAL VARS'''
MAX_TABLE = 5 #100      # the number of data that will be added to csv
RM_STR = '[email'

'''
    Creates a data storing class of Table that stores attributes:
    expression name, expression, description and author
'''
class Table: 
    def __init__(self, exp_name, exp, description, link, author):
        self.exp_name = exp_name

        result = exp.find(RM_STR)       # gets rid of '[email protected]'
        if result != -1:        
            exp = exp[result:]          # cuts string up to result and then up to ']'
            j = 0
            while j < len(exp) and exp[j] != ']':
                j += 1
            exp = exp[j+1:]
        self.exp = exp

        description =  description.split('\n')[0].replace(',', '')
        self.description = description

        self.link = link
        self.author = author.replace(',', '')

    '''
    writes content into a csv file for given table
    '''
    def get_row(self):
        return [self.exp_name, self.exp, self.description, self.link, self.author]

    '''
    displays the table class objects
    '''
    def print_table(self):
        print("Title: " + self.exp_name + "\nExpression: " + self.exp \
        + "\nDescription: " + self.description + "\nLink: " + self.link \
        + "\nAuthor: " + self.author + "\n------xxx------")


def create_table(table):
    try:
        all_as = table.find_all('a')        # creates an array of all a tags
        # print(all_as[2].get('href'))        # href is in all_as[2] 
        link = 'regexlib.com/' + all_as[2].get('href')

        exp_name = all_as[2].text.strip()   # index [2] holds expression name
        exp_author = all_as[len(all_as) - 1].text.strip() # index [last item] holds expression author

        expression = table.find('div', class_="expressionDiv").text.strip()
        description = table.find('div', class_="overflowFixDiv").text.strip()

    except Exception as e:
        exp_name, exp_author, expression, description = '' 

    table = Table(exp_name, expression, description, link, exp_author)
    # table.print_table()
    return table

'''web scraping code
given a webpage, up to 5 tables are copied and placed into a csv file'''
webpage = 'https://regexlib.com/Search.aspx?k= &c=-1&m=-1&ps=20'.split(' ')
f = open('user_input.txt', 'r')     # creates webpage link from an input file
webpage = webpage[0] + f.readline() + webpage[1] 

source = requests.get(webpage).text

soup = BeautifulSoup(source, 'lxml')    # create BS obj of article 
table = soup.find_all('table')

list_tables = []

if MAX_TABLE > len(table):
    MAX_TABLE = len(table)

f = open('pg_content.csv', 'w')
writer = csv.writer(f)

count = 0
for i in range(MAX_TABLE):
    list_tables.append(create_table(table[i]))
    if list_tables[count].exp != '': 
        writer.writerow(list_tables[count].get_row())
    count += 1
    
f.close()
