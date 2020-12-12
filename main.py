import urllib



import methods
import parse

from getpass import getpass
    
u = input("Username: ")
p = getpass()

while True:   
  try:   
    soup = methods.mechanize_method(u, p)
    break
  except urllib.error.URLError:
    continue


#soup = BeautifulSoup(open("demofile2.html"), "lxml")
    






classes = soup.findAll("div", {"class": "AssignmentClass"})


# for values in classes:
    


#     main_grade = get_shit.main(values)
    


print(parse(classes[7]))