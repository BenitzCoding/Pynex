import os
import sys
import getpass
import requests
from yachalk import chalk
from getmac import get_mac_address as gma

ALLOWED_CHARACTERS = [
	'a',
	'b',
	'c',
	'd',
	'e',
	'f',
	'g',
	'h',
	'i',
	'j',
	'k',
	'l',
	'm',
	'n',
	'o',
	'p',
	'q',
	'r',
	's',
	't',
	'u',
	'v',
	'w',
	'x',
	'y',
	'z',
	'0',
	'1',
	'2',
	'3',
	'4',
	'5',
	'6',
	'7',
	'8',
	'9',
	'.',
	'-',
	'_'
]

def lockout():
	print(chalk.bold.red("Session ended because of too many failed login attempts."))
	return sys.exit()

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
	response = requests.get(f"https://api.senarc.org/pynex/login/{username}/{password}/{gma()}")
	if response.json() == { "success": True, "address": gma() }:
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
		print(chalk.bold.red("\nYour username can't be less than 3 characters, please re-enter a different username."))
		return signup()
	elif len(username) >= 16:
		print(chalk.bold.red("\nYour username can't be more than 16 characters, please re-enter a different username."))
		return signup()
	for character in list(username):
		if character in ALLOWED_CHARACTERS:
			continue
		else:
			print(chalk.bold.red("\nYour username should only consist ASCII Text."))
			return signup()
	try:
		validate_username = requests.get(f"https://api.senarc.org/pynex/validate/{username}")
		if validate_username.json() == {"TAKEN": True}:
			print(chalk.bold.red("\nThis username is taken, please enter a different username."))
			return signup
		password = getpass.getpass('password: ')
		confirm_password = getpass.getpass('confirm password: ')
		if password != confirm_password:
			print(chalk.bold.green("Those password don't match, please re-enter."))
			return signup()
		response = requests.get(f"https://api.senarc.org/pynex/register/{username}/{password}/{gma()}")
		if response.json() == {"success": True}:
			print(chalk.bold.green("Your account has been registered successfully."))
			return login()
	except:
		return print(chalk.bold.red("\nThe API to manage accounts is currently down, please try again later."))

def options(i=None):
	try:
		if i != None:
			option = input("> ")
		else:
			option = input("""
________________________
|  SIGN IN OR SIGN UP  |
|                      |
|     [1]: SIGN IN     |
|     [2]: SIGN UP     |
|______________________|
\n\n> """)
	except:
		print(chalk.bold.red("Invalid Option."))
		return options("i")
	if option == "1":
		return login()

	elif option == "2":
		return signup()

	else:
		print(chalk.bold.red("Invalid Option."))
		return options("i")

clear()
options()