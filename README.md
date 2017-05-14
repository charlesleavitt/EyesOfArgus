# EyesOfArgus
A ModSecurity Log Visualizer  
* Charles Leavitt - cil9957@rit.edu  
* Josh Akers  
* Kortni Sheldon  - kms8085@rit.edu
### Prerequisites: 
* This visualization project reads ModSecurity version 2.9.1+ logs in JSON format. This means you need to either have ModSecurity ver 2.9.1+ running with JSON logs using the OWASP rule set or have a copy of a JSON ModSecurity Log 
* For your convenience a sample log is included
* Other dependencies:  
  * python 2.7+  
  * a running web server eg. Apache2
### Installation:
As root: Clone or copy this repository to your web server's document root. 
### Usage: 
To view the ModSecurity log visualization there are two options:
1. Run with limited permissions on a local copy of the logfile:  
   1. Copy the ModSecurity log file (eg. modsec_audit.log) to the EyesOfArgus directory    
   2. Run "python eyesofargus.py" 
2. Run as root with the log file path/name as an argument:  
   Eg. "sudo python eyesofargus.py /var/log/modsec_audit.log"
   
