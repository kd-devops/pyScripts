import os
import time
import shlex
import subprocess

from subprocess import Popen , PIPE


APACHE_VERSION = "apache2 -v"
APACHE_CHECK = "service apache2 status"
status = {}

def check_apache_installed():
    ver_cmd = shlex.split(APACHE_VERSION)
    ver = subprocess.Popen(ver_cmd, stdout=subprocess.PIPE)
    apache_ver = ver.communicate()[0]
    return apache_ver

def check_apache_status():
    apache_installed = check_apache_installed()
    if apache_installed:
    	cmd= shlex.split(APACHE_CHECK)
    	response = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    	apache_status = response.communicate()[0]
    	result = apache_status
    else:
	msg = "Apache is Not Installed in System"
	result = msg

    status["Apache Status"] = result
    return(status)
apache_status = check_apache_status()
print apache_status
