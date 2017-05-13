# EyesOfArgus
A ModSecurity Log Visualizer  
* Charles Leavitt - cil9957+EyesofArgus@rit.edu  
* Josh Akers  
* Kortni Sheldon  
### Prerequisites: 
* This visualization project reads ModSecurity version 2.9.1+ logs in JSON format. This means you need to either have ModSecurity ver 2.9.1+ running with JSON logs using the OWASP rule set or have a copy of a JSON ModSecurity Log 
* For your convenience a sample log is included  
### Installation:
Clone or copy this repository to your web server's document root with root permissions  
### Usage: 
To view the ModSecurity log visualization there are two options:
1. Run with limited permissions on a local copy of the logfile:  
   1. Copy the Modsecurity log file to the EyesOfArgus directory    
   2. Run "python eyesofargus.py" 
2. Run as root with the log file path as an argument:  
   Eg. "sudo python eyesofargus.py /var/log/"
   