import os
import sys

def get_clear_command():
	clear_command = {
		"win32": "cls",
		"linux": "clear"
	}
	return clear_command[sys.platform]

def clear():
	os.system(get_clear_command())
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
		return os.system("python login.py")

	else:
		done_count = 0
		file = open("./pypi.txt", "r")
		line_count = 0
		for line in file:
			if line != "\n":
				line_count += 1

		for content in file.readlines():
			os.spawnl(os.P_DETACH, f'pip install {content}')
			done_count = done_count + 1
			os.system(get_clear_command())
			print(f"""
    ____                       
   / __ \__  ______  ___  _  __
  / /_/ / / / / __ \/ _ \| |/_/
 / ____/ /_/ / / / /  __/>  <  
/_/    \__, /_/ /_/\___/_/|_|  
      /____/                   
\n\n
          {done_count}/{line_count} Done!
{'#'* done_count + ('_' * line_count - done_count)}""")
		with open('.installed', 'w') as f:
			f.write('Pynex installed pypi packages.')

clear()
boot()