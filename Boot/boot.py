import os
import sys
from utils import get_data, register_value
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
	try:
		return os.system(get_command("python") + f" {get_data('path')}/Boot/login.py")
	except:
		try:
			os.system(get_command("clear"))
			path = repr(input(f"""
    ____                       
   / __ \__  ______  ___  _  __
  / /_/ / / / / __ \/ _ \| |/_/
 / ____/ /_/ / / / /  __/>  <  
/_/    \__, /_/ /_/\___/_/|_|  
      /____/                   
\n\nWhere is Pynex Folder (ex. "/root/Pynex")? """)).strip("'").replace("\\\\", "/")
			register_value(variable="path", value=path)
			done_count = 0
			with open(path + "/Boot/pypi.txt", 'r') as file:
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
\n\nInstalling Packages...""")
					for content in file.readlines():
						ps = run(get_command("pip") + f" install {content}", stdout=PIPE, stderr=STDOUT, shell=True, text=True)
					os.system(get_command("clear"))
					print("""
    ____                       
   / __ \__  ______  ___  _  __
  / /_/ / / / / __ \/ _ \| |/_/
 / ____/ /_/ / / / /  __/>  <  
/_/    \__, /_/ /_/\___/_/|_|  
      /____/                   
\n\nInstalled All Packages, Running Pynex...""")
					sleep(3)
					os.system(get_command("clear"))
					return os.system(get_command("python") + " " + path + " /Boot/login.py")
		except Exception as e:
			print(e)
			return

clear()
boot()