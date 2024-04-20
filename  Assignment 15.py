#สร้างขอบตาราง
last = int(input("ป้อนขนาดที่ต้องการ :"))
for row in range(last) :
	for number in range(last):
		if  row == 0 or row == last-1 or number == 0 or number == last-1:
			print("x",end="")
		else :
			print(" ",end="")
	print(" ")

print(20000((1+0.01)**2))