import numpy as np
 
a=np.array([0,1,2,3,4,5,6,7,8,9])
print(a*2)
print()

# 2행 3열짜리 matrix를 만든것이여
b=np.array([[0,1,2],[3,4,5]])
print(b)
print()

# 2차원이 여러개있는 이게 3차원이여
c=np.array([[[0,1,2],[3,4,5]],[[4,5,6],[7,8,9]]])
print(c)

# 기모땅 
print(b.ndim) # 차원 : 2
print(c.shape) # 형태 : 2 by 3 매트릭스가 2개가 있다! 

x = np.array([[0,1,2,3],[4,5,6,7]])
print(x[1][2])
print(x[1,2])
print(x[0, :])
print(x[1,1:3])

idx = np.array([True, False, False, True, True])
a = np.array([1,2,3,4,5])
print(a[idx])

# 팬시 인덱싱
print(a>2)
print(a[a>2])
print(a%2 == 0)
print(a[a%2==0])

# 연습문제
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(x[x%3==0])
print(x[x%4==1])

#  ????
x1 = x[x%4==1]
y1 = x[x%3==0]
print(np.intersect1d(x1, y1, assume_unique=True))

#################################
x = np.array([1,2,3.0])
y = np.array([1,2,3])
y2 = np.array([1,2,3],dtype='f') # 데이터형식지정
print(x)
print(y)
print(y2)

x = np.array([1,3,True,False])
## numpy에서는 모두 통일된 값으로 처리해야하기문에 True : 1, False : 0로 계산
print(x)

# inf 는 무한대 nan 은 수학적으로 말이 안되는경우
x = np.array([0,1,-1,0])
y = np.array([1,0,0,0])
print(x/y)

a1 = np.zeros(5) #zeros든 ones든 튜플형식으로 입력!! 튜플은 리스트와 달리 변경불가능!
a2 = np.ones((4,2,3)) # 3차원 매트릭스
print(a2)

print(np.arange(10))
print(np.arange(3,21,2))

x = np.arange(12)
print(x)
y = x.reshape(1,12)
print(y)
t = x.reshape(3,-1) # 행의 갯수는 3개로 고정시킬테니 알아서 계산해라!
print(t)
q = x.reshape(-1,6) # 열의 갯수는 6개로 고정시킬테니 알아서 계산해라!
print(q)

# 3차원 배열로 reshape
x = np.arange(24)
t2 = x.reshape(4,2,3)
print(t2)
t2 = x.reshape(2,2,-1) # 알아서 맡기는거지 이것도
print(t2)

# 붙이기
# 행의 개수가 같아야 가로로 붙일수있지 hstack
# 열의 개수가 같아야 세로로 붙일수있지 vstack
a1 = np.ones((2,3))
a2 = np.zeros((2,2))
print(np.hstack((a1,a2))) # hstack은 여러개의 배열로 이루어진 tuple을 입력값으로 한다. 근데 [a1,a2], (a1,a2)는 노상관
# hstack 함수 괄호 안에어 shift + tab을(주피터!) 눌러서 함수의 사용 방법을 호출하였다.
a1 = np.ones((2,3))
a2 = np.zeros((5,3))
print(np.vstack((a1,a2))) 

# stack의 작동 (같은 차원들끼리의 결합)
x = np.array([0,1,2,3])
y = np.array([4,5,6,7])
print(np.stack((x,y),axis=0)) 
# 차원을 추가하는데 행을 1로 만든다 
# x:4 -> x(1,4) y:4 -> y(1,4) 합해서 ==> (2,4)
print(np.stack((x,y),axis=1)) 
# 차원을 추가하는데 열이 추가된다 
# x:4 -> x(4,1) y:4 -> y(4,1) 합해서 ==> (4,2)
### 다차원의 stack
c1 = np.ones((3,4))
c2 = np.zeros((3,4))
np.stack([c1,c2],axis=0) # 3,4 ==> (2,3,4)
np.stack([c1,c2],axis=1) # 3,4 ==> (3,2,4)
np.stack([c1,c2],axis=2) # 3,4 ==> (3,4,2)
