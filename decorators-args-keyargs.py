def security_check(func):

	def wrapper(*args, **kwargs):
		print("Performing Security Check....")
		func(*args, **kwargs)

	return wrapper


@security_check

def deploy(app_name, version):

	print("Deploying:", app_name, "Version:", version)

deploy("College Management", "1.0")