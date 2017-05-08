# file: eoa.p
# EyesOfArgus : A ModSecurity log Visualizer
from pprint import *
import subprocess
import webbrowser
import signal
import sys
import os
import json

#logpath = "/var/log/"
#logpath = sys.argv
logname = "modsec_audit.json"

def get_log():
    with open(logname, 'r') as f:
        jsonData = json.load(f)
    return jsonData

def open_webpage():
    # open in a new tab, if possible
    new = 2
    url = "http://127.0.0.1/EyesOfArgus"
    webbrowser.open(url,new=new)

def main():
    #open_webpage()
	#f = input("Press enter when done")
    jsonLog = get_log()
    pprint(jsonLog)
	

main()

