import os
import click

def get_user_path():
	if os.getcwd().endswith("Boot"):
		return os.getcwd().replace("/Boot", "") + "/User"
	elif os.getcwd().endswith("Pynex"):
		return os.getcwd() + "/User"
	else:
		raise RuntimeError("Invalid Directory Launch. Code: E01")


def listen(username):
	os.system("cd " + get_user_path())
	current_path = f"/home"
	while True:
		command = input(f"[{username}@~{current_path}]>")
		if command.startswith("cd --home") or command.startswith("cd -h"):
			current_path = "/home"
			os.system("cd " + get_user_path() + f"/{username}")
		elif command.startswith("cd"):
			if command.endswith(f"/Pynex/User/{username}"):
				current_path = "/home"
			current_path = command.replace("cd ", "")
			os.system(command)
		elif command.startswith("exit"):
			sys.close()
		else:
			os.system(command)

@click.group(invoke_without_command=True, options_metavar='[options]')
@click.pass_context
def main():
	print("Main executed")
	pass

@main.group(short_help='Passes login to startup.', options_metavar='[username]')
def pass_login():
	print("Pass Login executed")
	pass

@pass_login.command(short_help="Startup module that does checks before start.")
def startup(username):
	print("Startup executed")
	path = get_user_path()
	if path.isfile(username):
		return listen(username)
	else:
		os.system(f"mkdir {username}")
		return listen(username)