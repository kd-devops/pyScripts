import os
import sys

PATH="/etc/ansible/repo/playbook/dirbot/roles/"
#roles_name = sys.argv[1]
print "Enter roles name!"
roles_name = raw_input()

cwd = os.getcwd()
new_roles_path = PATH + roles_name
print new_roles_path

templates = 'templates'
varriables = 'var'
files = 'files'
handlers = 'handlers'
meta = 'meta'
tasks = 'tasks'

if not os.path.exists(new_roles_path):
   os.mkdir(new_roles_path)
   os.mkdir(new_roles_path + '/' + templates)
   os.mkdir(new_roles_path + '/' + varriables)
   os.mkdir(new_roles_path + '/' + files)
   os.mkdir(new_roles_path + '/' + handlers)
   os.mkdir(new_roles_path + '/' + meta)
   os.mkdir(new_roles_path + '/' + tasks)
