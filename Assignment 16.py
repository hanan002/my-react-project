#เกมทายเลขลูกเต๋า
import random
myrandom = random.randrange(1,7)
correct = False
print("คุณมีโอกาศตอบคำถาม 3 ครัง")
i = 1
while True :
	number = int(input("ป้อนตัวเลขของคุณ :"))
	correct = (number==myrandom)
	if not correct :
		if number < myrandom :
			print("มากกว่านี้")
		if number > myrandom :
			print("น้อยกว่านี้")
	if correct :
		print("ยินดีด้วยคุณชนะ")
		break
	if number<0 or number>6 or i == 3 :
		print("game over")
		break
	i+= 1

	