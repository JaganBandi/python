class InsufficientBalenceError(Exception):

	pass

balence = 500
withdraw = 1000

if withdraw > balence:
	raise InsufficientBalenceError("Insufficient Balence")

print("Withdraw Successfully")