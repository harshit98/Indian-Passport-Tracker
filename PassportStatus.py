# Code to check passport status in your terminal.

import urllib
import tkinter.messagebox as tk

from bs4 import BeautifulSoup

url = 'https://portal2.passportindia.gov.in/AppOnlineProject/statusTracker/trackStatusInpNew'

user_info = {
    'status': 'APPLICATION STATUS',
    'file': 'FILE_NUMBER',
    'dob': 'dd/mm/yyyy',
}

# Get information
data = urllib.parse.urlencode(user_info)

# Request data from server
req = urllib.request.Request(url, data)

# Collect response
response = urllib.request.urlopen(req)

# Read the response received
page = response.read()

soup = BeautifulSoup(page)
form = str(soup.findChildren('form')[1].findChildren('table')[0].findChildren('tr')[7].findChildren('td')[1])

status = form.split('<td>')[1].split('</td>')[0]

f = open('~/status.txt', 'r+')

if status == f.readline():
    pass
else:
    tk.showinfo(title="Passport-Status", message=status)
    f.seek()
    f.write(status)

f.close()
