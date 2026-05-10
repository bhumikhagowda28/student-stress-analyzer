sleep=int(input("enter sleep hours: "))
screen=int(input("enter screen hours: "))
study=int(input("enter study hours: "))

if sleep<5 and screen>8:
	print("High stress level detected")
 print(" take proper rest and reduce screen   time")
elif sleep<=7:
	print(" medium stress detected")
 print(" try balancing the same routines")
else:
	print("low stress detected")
	print(" keep maintaining healthy habits")