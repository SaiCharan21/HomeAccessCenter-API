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

while True:   
  try:   
    soup = methods.mechanize_method(u, p)
    break
  except urllib.error.URLError: #because sometimes hac decides its taking the day off
    continue

  

main_grade = {}




classes = soup.findAll("div", {"class": "AssignmentClass"})
for values in classes: 
    parse.main(values, main_grade)

json_object = json.dumps(main_grade, indent = 6)  
print(json_object)  