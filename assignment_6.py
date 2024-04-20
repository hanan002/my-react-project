x = int(input("น้ำหนัก :"))
y = int(input("ส่วนสูง :"))/100

bmi = x/(y**2)

if bmi < 18 :
	olo = "ต่ำกว่าเกณฑ์"

elif bmi >= 18.5 and bmi <= 22.9 :
	olo = "สมส่วน"

elif bmi >= 23.0 and bmi <= 24.9 :
	olo = "น้ำหนักเกิน"

elif bmi >= 25.0 and bmi <= 29.9 :
	olo = "โรคอ้วน ระดับ 1"

elif bmi > 30 :
	olo = "น้ำหนักเกิน"
	print("โรคอ้วยอันตราย")

else :
	olo = "error"

print(olo)
print("ค่า bmi ของคุณ =",bmi)
print("end the programe")