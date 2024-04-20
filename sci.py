max,min = 0,99999999
for i in range(1,3):
	number = int(input("ป้อนตัววเลขที่คุณต้องการ :"))
	if number>max :
		max = number
	if  number<min :
		min = number
	print("รอบที่ =",i)

print("ค่า max =",max)
print("ค่า min =",min)    