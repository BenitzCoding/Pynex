import os
import sys
import getpass
import requests
from yachalk import chalk
from getmac import get_mac_address as gma

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

TRIES = []

def login():
	username = input("username: ")
	if len(username) <= 3:
		if len(TRIES) >= 5:
			return lockout()

		else:
			TRIES.append("Failed")
			print(chalk.bold.red("Invalid login, please try again.\n"))
		return login()
	password = getpass.getpass('password: ')
	response = requests.get(f"https://api.senarc.org/pynex/login/?username={username}&password={password}")
	if response == { "success": True, "address": gma() }:
		print(chalk.bold.green(f"You are now logged in as \"{chalk.bold.blue(username)}\""))
		return
	else:
		if len(TRIES) >= 5:
			return lockout()

		else:
			TRIES.append("Failed")
			print(chalk.bold.red("Invalid login, please try again."))
		return login()

def signup():
	username = input("username: ")
	if len(username) <= 3:
		print(chalk.bold.red("\nYour username can't be less than 3 charecters, please re-enter a different username."))
		return signup()
	validate_username = requests.get(f"https://api.senarc.org/pynex/validate/?username={username}")
	if validate_username == None:
		return print(chalk.bold.red("\nThe API to manage accounts is currently down, please try again later."))
	if validate_username.json() == {"TAKEN": True}:
		print(chalk.bold.red("\nThis username is taken, please enter a different username."))
		return signup
	password = getpass.getpass('password: ')
	response = requests.get(f"https://api.senarc.org/pynex/register/?username={username}&password={password}&address={gma()}")
	if response.json() == {"success": True}:
		print(chalk.bold.green("Your account has been registered successfully."))
		return login()

def options():
	try:
		option = int(input("""
________________________
|  SIGN IN OR SIGN UP  |
|                      |
|     [1]: SIGN IN     |
|     [2]: SIGN UP     |
|______________________|
\n\n> """))
	except:
		input(chalk.bold.red("Invalid Option." + "\n> "))
		return options()
	if option == 1:
		return login()

	elif option == 2:
		return signup()

clear()
options()