from bs4 import BeautifulSoup
import mechanize
import methods
import urllib
import parse
import json
import time
import re
from getpass import getpass


main_grade = {}

# u = input("Username: ")
# p = getpass()
# l = "homeaccess.katyisd.org"



def main(username, password, link):
    main_grade = {}


    soup = methods.main(username, password, link)
    classes = soup.findAll("div", {"class": "AssignmentClass"}) 
    #print(classes)

    main_grade = parse.main(classes)


    return main_grade
