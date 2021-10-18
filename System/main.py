import os
import click
from utils import get_data, register_value

def listen(username):
	os.system("cd " + get_data('path') + "/User/" + username)
	current_path = f"/home"
	while True:
		command = input(f"[{username}@~{current_path}]> ")
		if command.startswith("cd --home") or command.startswith("cd -h"):
			current_path = "/home"
			os.system("cd " + get_data('path') + "/User/" + username)
		elif command.startswith("cd"):
			if command.endswith(f"/Pynex/User/{username}"):
				current_path = "/home"
			current_path = command.replace("cd ", "")
			os.system(command)
		elif command.startswith("exit"):
			sys.close()
		else:
			os.system(command)

def startup():
	os.system("cd ..")
	os.system("cd System")
	username = get_data('username')
	return listen(username)

startup()