def backup_required(func):

	def wrapper():
		print("Taking Backup...")
		func()

	return wrapper

@backup_required

def deploy():
	print("Deploying College Management Application...")

deploy()
