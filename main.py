#Project TechBot
#Release v.1.0
import webbrowser
import calendar
import time
import os
import subprocess

print("""

████████╗███████╗░█████╗░██╗░░██╗██████╗░░█████╗░████████╗
╚══██╔══╝██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗╚══██╔══╝
░░░██║░░░█████╗░░██║░░╚═╝███████║██████╦╝██║░░██║░░░██║░░░
░░░██║░░░██╔══╝░░██║░░██╗██╔══██║██╔══██╗██║░░██║░░░██║░░░
░░░██║░░░███████╗╚█████╔╝██║░░██║██████╦╝╚█████╔╝░░░██║░░░
░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░
""")
searchbar = input("Enter Command (enter cmds for commands list): ")

#Commands
if searchbar == "cmds":
    print("""
To open apps                  - openapps
To open websites              - browse
To view this month calendar   - calendar
To create reminders           - reminders
""")

#Open Windows Apps
if searchbar == "openapps":
    appname = input("Enter the app name which you want to open: ")
    
    if appname == "notepad":
        subprocess.Popen("C:\\Windows\\System32\\notepad.exe")
        
    if appname == "paint":
        subprocess.Popen("C:\\Windows\\System32\\mspaint.exe")
        
    if appname == "safari":
        subprocess.Popen("D:\\safari.exe")
        
    if appname == "chrome":
        subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

#Open links in Browser
if searchbar == "browse":
    searchquery = input("Enter URL: ")
    webbrowser.open(searchquery)
    
#Calendar
if searchbar == "calendar":
    c = calendar.TextCalendar(calendar.SUNDAY)
    str = c.formatmonth(2022, 5)
    print(str)

#Reminder
if searchbar == "reminders":
    print("What shall I remind you about?")
    text = str(input())
    print("In how many minutes?")
    local_time = float(input())
    local_time = local_time * 60
    time.sleep(local_time)
    print("REMINDER!!!!"+ text)