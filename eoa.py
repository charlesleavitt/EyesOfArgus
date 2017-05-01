# file: eoa.p
# EyesOfArgus : A ModSecurity log Visualizer
import subprocess
import webbrowser
import signal
import os

#webserver = subprocess.Popen("python3 /root/Desktop/EyesOfArgus/webserver.py", shell=True)
#print("WEBSERVER PID:", webserver.pid)

def open_webpage():
	# open in a new tab, if possible
	new = 2 
	url = "http://127.0.0.1/EyesOfArgus"
	webbrowser.open(url,new=new)

def main():
	open_webpage()
	f = input("Press enter when done")	
	
	#os.kill(webserver.pid, signal.SIGKILL)	
	#os.kill(webserver.pid+1, signal.SIGKILL)
	#webserver.communicate(signal.SIGINT)
	#webserver.kill()
	

main()

