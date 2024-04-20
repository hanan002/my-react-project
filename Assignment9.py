#แม่สูตรคูณ

#แสดงแม่สูตรคูณ 2,3,4....,12
start = int(input("เริ่มต้น :"))
stop = int(input("สุดท้าย"))+1
for i in range(start,stop) :
	print("แม่ที่", i)
	for j in range(1,13):
		print(i,"x",j," = ",i*j)