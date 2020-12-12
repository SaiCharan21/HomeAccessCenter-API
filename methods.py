import requests
import mechanize
from bs4 import BeautifulSoup


def mechanize_method(username, password):
	
    br = mechanize.Browser()


	# Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Chrome')]

    br.open('https://homeaccess.katyisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess/Classes/Classwork%2f')
      
    br.select_form(nr=0)



    br.form['LogOnDetails.UserName'] = username
    br.form['LogOnDetails.Password'] = password

    br.submit()

    response = br.open("https://homeaccess.katyisd.org/HomeAccess/Content/Student/Assignments.aspx")
    return BeautifulSoup(response.read(), "lxml") 
    

#------------------------------------------


#BROKEN, DOESNT WORK FOR NOW

# def curl_method(username, password):
    # headers = {
        # 'authority': 'homeaccess.katyisd.org',
        # 'pragma': 'no-cache',
        # 'cache-control': 'no-cache',
        # 'origin': 'https://homeaccess.katyisd.org',
        # 'upgrade-insecure-requests': '1',
        # 'dnt': '1',
        # 'content-type': 'application/x-www-form-urlencoded',
        # 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36',
        # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'sec-fetch-site': 'same-origin',
        # 'sec-fetch-mode': 'navigate',
        # 'sec-fetch-user': '?1',
        # 'sec-fetch-dest': 'document',
        # 'referer': 'https://homeaccess.katyisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f',
        # 'accept-language': 'en-US,en;q=0.9',
    # }

    # params = (
        # ('ReturnUrl', '/HomeAccess/'),
    # )

    # data = {
      # 'LogOnDetails.UserName': username,
      # 'LogOnDetails.Password': password
    # }

    # response = requests.post('https://homeaccess.katyisd.org/HomeAccess/Account/LogOn', headers=headers, params=params, data=data, timeout=10)
    # response = requests.get("https://homeaccess.katyisd.org/HomeAccess/Content/Student/Assignments.aspx")

    # return BeautifulSoup(response.text, "lxml") 