from __future__ import print_function
from bs4 import BeautifulSoup
from gi.repository import Notify
import re
import subprocess
from mechanize import Browser
import time
import urllib
import urllib2

changed = 0

def Starting():
    Notify.init("Checking status...")
    Notify.Notification.new("\nPassport check initiated.").show()

def Check():
    while changed != 1:
        Starting()
        main()
        if changed == 1:
            Notify()
        time.sleep(3600) 

def Notify():
    Notify.init("Status changed")
    Notify.Notification.new("\nPassport status changed.").show()

def main():
    global changed
    url = 'https://portal1.passportindia.gov.in/AppOnlineProject/statusTracker/trackStatusInpNew'
    file_number = ''
    date_of_birth = '' # dd / mm / yyyy
    current_status = '' # copy and paste current application status
    nav = Browser()
    nav.set_handle_robots(False)
    nav.addheaders = [('User-agent', 'Chrome')]
    nav.open(url)
    nav.select_form('track-status')
    nav.form[nav.controls[0].name] = ['Application Status']
    nav.form[nav.controls[1].name] = file_number
    nav.form[nav.controls[2].name] = date_of_birth
    response = BeautifulSoup(nav.submit())
    tableClass = response.find("div", attrs={ "class": "block_right_inner" })
    table = tableClass.find("table", attrs={ "role": "presentation" })
    tableValue = table.find("td", attrs={ "": "" }).get_text()

    if current_status not in tableValue:
        changed = 1
        subprocess.call(['spd-say', '"Passport Status Changed!"'])

if __main__ == '__main__':
    Check()
