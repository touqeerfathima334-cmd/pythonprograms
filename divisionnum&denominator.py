try:
	numerator=int(input("enter numerator:"))
	denominator=int(input("enter denominator:"))
	result=numerator/denominator
	print(f"result:{result}")
except zerodivisionerror:
	print("Error:cannot divide by zero")
except valueError:
	print("plz enter valid integers")
	