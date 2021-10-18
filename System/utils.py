import json

def get_data(variable):
	with open("info.json", "r") as jsonFile:
		data = json.load(jsonFile)
	return data[variable]

def register_value(variable, value):
	try:
		with open("info.json", "r") as jsonFile:
			data = json.load(jsonFile)
	
		data[variable] = value
	
		with open("info.json", "w") as jsonFile:
			json.dump(data, jsonFile)
	
	except:
		data = {}
		data[variable] = value
	
		with open("info.json", "w") as jsonFile:
			json.dump(data, jsonFile)