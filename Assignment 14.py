#สร้างตารางหมากฮอต
"""
แทน
x = สีน้ำตาล
o = สีขาว
"""
number = int(input("ป้อนตัวเลข : "))
for row in range(1,number+1):
	for colamn in range(1,number+1):
		"""
		if (row+colamn)%2 == 0:
			print("x",end=" ")
		else :
			print("o",end=" ")
		
		ยุปให้แอยู่ในบรรทัดเดี่ยงกัน
		"""
		print("x",end=" ") if (row+colamn)%2 == 0 else print("o",end=" ")
		    
	print(" ")
	    
    