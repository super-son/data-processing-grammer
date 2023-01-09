##########################################

# x1=[4,3,2,3,4]
# x2=[3,3,1,2,2]
# sum=0
# sum_div=0

# for idx, (a1,a2) in enumerate(zip(x1,x2)):
# 	sum += a1 * a2
# 	sum_div += a2 
# 	if idx + 1 == len(x1):
# 		print(sum/sum_div)

##########################################

def Var(*args): # 미친 핵꿀팁.. 이렇게 하면 자유롭게 받을 수 있구나.
	sum = 0
	x=args
	for i in x:
		sum += i
	avg = sum/len(x)

	sum1 = 0
	for i in x:
		sum1 += (i-avg)**2

	var = sum1/len(x)
	print(var)

Var(1,2,3,4,5)

###########################################

class Character():
	def __init__(self,x,y):
		self.h = x
		self.p = y
		self.life = 1000
	def attacked(self):
		self.life = self.life - 100
		print("공격 받았습니다. 현재 체력 :",self.life)
	
class Warrior(Character):
	def __init__(self,x,y):
		super(Warrior,self).__init__(x,y)
		self.power = 100
	def attack(self):
		print("상대방에게 100의 데미지를 입힙니다")

me = Character(1,2)
for i in range(3):
	me.attacked()
re = Warrior(2,3)
re.attack()

#####################################

# 사각형 클래스만들기
class Character():
    
    def __init__(self):
        self.life = 1000

    def attacked(self):
        self.life = self.life - 10
        print("공격받음! 생명력 = ",self.life)

class Warrior(Character):
    def __init__(self):
        super(Warrior,self).__init__() # 캐릭터(부모클래스)의 생성자로 접근하여 생명력과 attack 행동을 상속받았다.
        # 사실 Character.__init__()으로 해도되.. 괄호안에는 받고싶은 멤버만 적을수있고
        self.strength = 15
        self.intelligence = 5

    def attack(self):
        print("육탄공격")

class Wizard(Character):
	def __init__(self):
		super(Wizard,self).__init__()
		self.strength = 10
		self.intelligence = 20

	def long_attack(self):
		print("원거리공격")	

me = Warrior() # 인자를 넣을 공간이 없음. 그대로 상속
you = Wizard()
print(me.strength, you.strength)

###########################################################
x = 7

if x > 10 :
	print("1등급")
elif x > 7 :
	print("2등급")
elif x > 4 :
	print("3등급")
else :
	print("4등급")
########################################
y = 1800

if y%400==0:
	print("윤년")
else:
	if y%4 in [0,1,2,3,4,5]:
		if y%100 == 0:
			print("평년")
		else:
			print("윤년")
	else:
		print("평년")		
##########################################
for i in range(9):
	if i <=4 :
		print("*"*(i+1))
	else :
		print("*"*(9-i))
##########################################
stock = 2400

for i in range(-1,2,2):
    for j in range(-1,2,2):
        for k in range(-1,2,2):
            print(stock * (2**(i+j+k)))
##########################################
성적 = [3.5,4,4,4.5,4.5]
이수학점 = [2,2,3,2,3]
z1 = 0
z2 = 0
for x,y in zip(성적, 이수학점):
	z1 += x*y
	z2 += y
print(z1/z2)
##########################################
my_list = [1,4,7]
def var(x):
	sum1 = 0
	sum2 = 0
	z = len(x)

	for i in x:
		sum1 += i
	avg = sum1/z
	
	for i in x:
		sum2 += (i-avg)**2

	return sum2/z

print(var(my_list))
##########################################
data ={
	"민수" : 100,
	"휘준" : 90,
	"준희" : 80,
	"윤호" : 50
}
s = 0
for i,k in enumerate(data):
	print(k, ":", data[k])
	s += data[k]
	if i == len(data)-1:
		print("평균 :",s/len(data))

#############################################

class Character():
	def __init__(self):
		self.life = 1000
		print("탄생")

	def attacked(self):
		self.life -= 10
		print("i am attacked life is", self.life)
		

class Wizard():
	def __init__(self):
		super(Wizard,self).__init__()
		self.strength = 100

	def attack(self):
		print("toyou 100 damage")

class Warrior():
	def __init__(self):
		super(Warrior,self).__init__()
		self.intelligence=300

	def long_attack(self):
		print("toyou 100/300 damage")

a = Character()
for i in range(3):
	a.attacked()

b = Warrior()
b.long_attack()

c= Wizard()
c.attack()



