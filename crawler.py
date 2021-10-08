# Alexandros Darras crawler program for penetration testing portfolio , student id : 100567110

#                            ,-.
#       ___,---.__          /'|`\          __,---,___
#    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
#  ,'        |           ~'\     /`~           |        `.
# /      ___//              `. ,'          ,  , \___      \
#|    ,-'   `-.__   _         |        ,    __,-'   `-.    |
#|   /          /\_  `   .    |    ,      _/\          \   |
#\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
# \  \           | `._   `\\  |  //'   _,' |           /  /
#  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
#     ``       /     \    ,='/ \`=.    /     \       ''
#             |__   /|\_,--.,-.--,--._/|\   __|
#             /  `./  \\`\ |  |  | /,//' \,'  \
#           /   /     ||--+--|--+-/-|     \   \
#           |   |     /'\_\_\ | /_/_/`\     |   |
#            \   \__, \_     `~'     _/ .__/   /
#             `-._,-'   `-._______,-'   `-._,-'

import requests #a simple http request library.
from bs4 import BeautifulSoup as bs# A python package for parsing html documents,
                            # we use it to extract data from html more easily

url=str(input('give url for scraping ***please include "http://": ')) # here we promt the user to provide the program with the url that is going to be the target.

def get_soup(url): # this function will convert the plain text of the selected url to a beautifulsoup object so we can search easier for data.
    return bs(requests.get(url).text,'html.parser') #we use bs instead of beautifulsoup as indicated when we imported the library.

print('Scraping files from:',url)
for link in get_soup(url).findAll('a'):  # ' link ' is an identifiable parameter in beautifulsoup, 'a' is the parameter within link.
    file_link=link.get('href') #we get the href section of the link and store it in file_link.
    #now each of the if statements checks for a specific file type and downloads it, we can add or remove file types by modifying the code below.
    if '.jpg' in file_link:
        print(file_link)
        with open(link.text,'wb')as file:
            response=requests.get(url+'/'+file_link)
            file.write(response.content)
    elif '.md' in file_link:
        print(file_link)
        with open(link.text,'wb')as file:
            response=requests.get(url+'/'+file_link)
            file.write(response.content)
    elif  '.html' in file_link:
        print(file_link)
        with open(link.text,'wb')as file:
            response=requests.get(url+'/'+file_link)
            file.write(response.content)
    elif  '.pdf' in file_link:
        print(file_link)
        with open(link.text,'wb')as file:
            response=requests.get(url+'/'+file_link)
            file.write(response.content)



