import getpass
import requests
from yachalk import chalk
from getmac import get_mac_address as gma

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
			print(chalk.bold.red("Invalid login, please try again."))
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
		return signup
	validate_username = requests.get(f"https://api.senarc.org/pynex/validate/?username={username}")
	if validate_username.json() == {"TAKEN": True}:
		print(chalk.bold.red("\nThis username is taken, please enter a different username."))
		return signup
	password = getpass.getpass('password: ')
	response = requests.get(f"https://api.senarc.org/pynex/register/?username={username}&password={password}&address={gma()}")
	if response.json() == {"success": True}:
		print(chalk.bold.green("Your account has been registered successfully."))
		return login()