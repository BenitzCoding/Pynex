import os

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
		file = open("pypi.txt", "r")
		line_count = 0
		for line in file:
			if line != "\n":
				line_count += 1

		for content in file.readlines():
			os.spawnl(os.P_DETACH, f'pip install {content}')
			done_count = done_count + 1
			os.system("clear")
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

boot()