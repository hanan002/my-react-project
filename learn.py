number = int(input("จำนวนเงินที่ต้องกานถ้อน :"))

if number >= 1000 :
	print("แบงค์พัน",number//1000,"ใบ") 
	number %= 1000

if number >= 500 :
	print("แบงค์ห้าร้อย",number//500,"ใบ")
	number %= 500
 
if number >= 100 :
	print("แบงค์ร้อย",number//100,"ใบ")
	number %= 100

if number >= 50 :
	print("แบงค์ห้าสิบ",number//50,"ใบ")
	number %= 50

if number >= 20 :
	print("แบงค์ยี้สิบ",number//20,"ใบ")
	number %= 20

if number >= 10 :
	print("เหรียญสิบ",number//10,"coin")
	number %= 10

print("end the programe")