from bs4 import BeautifulSoup
from getpass import getpass
import mechanize
import methods
import parse
import json
import time
import re


u = input("Username: ")
p = getpass()

import urllib

while True:   
  try:   
    soup = methods.mechanize_method(u, p)
    break
  except urllib.error.URLError as e: #because sometimes hac decides its taking the day off
    e.reason
    continue




main_grade = {}



def main():
    classes = soup.findAll("div", {"class": "AssignmentClass"})
    for values in classes: 
        parse.main(values, main_grade)

    json_object = json.dumps(main_grade, indent = 6)  

    return json_object




        
    
    
print(main())