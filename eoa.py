# file: eoa.p
# EyesOfArgus : A ModSecurity log Visualizer
from pprint import *
import webbrowser
import json
import re
import sys

def args_init():
    logpath = "./"
    logname = "modsec_audit.log"
    if len(sys.argv) > 1:
        print sys.argv[1]
        if sys.argv[1].lower() == 'demo':
            demo()
        else:
            logpath = sys.argv[1]
            if logpath[:-1] != '/':
                logpath = logpath + "/"
    else:
        print "No Args"
        logname = "modsec_audit.json"

    logfile = logpath + logname
    return logfile

# Global Variables:
jsonArray = []
outDict = {"name": "flare", "children": []}

""" Function loads ModSecurity logs from a file to an array of JSON objects"""
def get_log(logfile):
    try:
        with open(logfile, 'r') as f:
            for line in f:
                d = unicode(line.strip('\n'),'iso-8859-15')
                jsonArray.append(json.loads(d))
    except IOError as e:
        print e
        if "Permission" in e.strerror:
            print 'Please run with the permissions to read the logfile: eg. sudo'
        else:
            print 'Please provide a valid ModSecurity logfile path'
        exit(0)

"""Function to iterate through JSON logs, extract data, push it to a JSON structure and write to flare.json"""
def parse_json():
    for a in jsonArray:
        for b in a["audit_data"]["error_messages"]:
            owasp = re.search('.*OWASP_CRS/WEB_ATTACK/([\w_]*)"\]', b)
            if owasp:
                #print owasp.group(1)   # prints the OWASP attack type
                new = True
                for d in outDict['children']:
                    if d.get('name') == owasp.group(1):
                        new = False
                        break
                if new:
                    outDict['children'].append({"name": owasp.group(1), "children": []})
                new = True
                ip = re.search('client ([\d\.]*)\]',b)
                if ip:
                    for c in outDict['children']:
                        if c.get('name') == owasp.group(1):
                            for d in c['children']:
                                if d.get('name') == ip.group(1):
                                    num = int(d.get('size'))
                                    num += 1
                                    d['size'] = num
                                    new = False
                                    break
                            if new:
                                c['children'].append({"name": ip.group(1), "size": 1})
    print(outDict)
    with open('flare.json', 'w') as fp:
        json.dump(outDict, fp)

"""Function opens a new tab to the visualizer in the default browser """
def open_webpage():
    # open in a new tab, if possible
    new = 2
    url = "http://127.0.0.1/EyesOfArgus"
    print "Opening Eyes Of Argus in browser..."
    webbrowser.open(url,new=new)

"""A demo function used if run with argument 'demo' """
def demo():
    with open("demo.json", 'r') as f:
        demo = json.load(f)
    with open('flare.json', 'w') as fp:
        json.dump(demo, fp)
    open_webpage()
    exit(0)

def main():
    # handle ars and do setup
    logfile = args_init()

    # bring in the logs
    get_log(logfile)

    # Parse each JSON log and create JSON for visualizer
    parse_json()

    # Open web page to display visualizer
    open_webpage()

main()

