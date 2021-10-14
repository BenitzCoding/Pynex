import os
import sys
import subprocess
import progressbar
from time import sleep
from subprocess import run, PIPE, STDOUT

def get_command(command):
	clear_command = {
		"win32": "cls",
		"linux": "clear"
	}
	pip_command = {
		"win32": "pip",
		"linux": "pip3"
	}
	python_command = {
		"win32": "python",
		"linux": "python3"
	}
	if command == "clear":
		return clear_command[sys.platform]

	elif command == "pip":
		return pip_command[sys.platform]
	
	elif command == "python":
		return python_command[sys.platform]
	

def clear():
	os.system(get_command("clear"))
	print("""
    ____                       
   / __ \__  ______  ___  _  __
  / /_/ / / / / __ \/ _ \| |/_/
 / ____/ /_/ / / / /  __/>  <  
/_/    \__, /_/ /_/\___/_/|_|  
      /____/                   
\n\n""")

def boot():
	if os.path.isfile('.installed'):
		return os.system(get_command("python") + " ./Boot/login.py")

	else:
		done_count = 0
		with open(os.getcwd() + "/Boot/pypi.txt", 'r') as file:
			line_count = 0
			for line in file:
				line_count += 1
				print(f"""
    ____                       
   / __ \__  ______  ___  _  __
  / /_/ / / / / __ \/ _ \| |/_/
 / ____/ /_/ / / / /  __/>  <  
/_/    \__, /_/ /_/\___/_/|_|  
      /____/                   
\n\nInstalling Packages""")
				for content in file.readlines():
					ps = run(get_command("pip") + f"install {content}", stdout=PIPE, stderr=STDOUT, shell=True, text=True)
				with open('.installed', 'w') as f:
					f.write('Pynex installed pypi packages.')
				os.system(get_command("clear"))
				print("""
    ____                       
   / __ \__  ______  ___  _  __
  / /_/ / / / / __ \/ _ \| |/_/
 / ____/ /_/ / / / /  __/>  <  
/_/    \__, /_/ /_/\___/_/|_|  
      /____/                   
\n\nInstalled All Packages, Starting Pynex...""")
				return os.system(get_command("python") + " ./Boot/login.py")

clear()
boot()