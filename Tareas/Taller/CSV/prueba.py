import os

def file_exists(filename,organization_data = os.getcwd()):
	"""
	Check if the specified file exists at the specified directory
	"""
	files = os.listdir(organization_data)
	return filename in files