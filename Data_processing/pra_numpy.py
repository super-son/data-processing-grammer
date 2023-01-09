import numpy as np
import pandas as pd

a=np.array([0,1,2,3,4,5,6,7,8,9]) # array에는 ([]) 형식유지! 
print(a)
print(a.ndim)
print(a.shape)

# shape가 (2,2,3)이라면 : 분류의 관점
# 대단위에서 2개, 중단위에서 2개 소단위에서 3개

x = np.array([[0,1,2,3],[4,5,6,7]])
print(x[:,0])

n = np.array([[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]])
print(n[1:,2])

y = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
y1 = y[y%3==0]
y2 = y[y%4==1]
print(np.intersect1d(y1,y2,assume_unique=True))

x = np.array([0,1,-1,0])
y = np.array([1,0,0,0])
print(x/y)

x=np.arange(0,12,1)
t = x.reshape(-1,3,2)
print(t.flatten())

a1 = np.ones((2,3))
a2 = np.zeros((5,3))
print(np.vstack([a1,a2]))

c1 = np.ones((3,4))
c2 = np.zeros((3,4))
print(np.stack([c1,c2],axis=0)) # 3,4 ==> (2,3,4)
print(np.stack([c1,c2],axis=1)) # 3,4 ==> (3,2,4)
print(np.stack([c1,c2],axis=2)) # 3,4 ==> (3,4,2)

x = np.array([[1,1],[2,2]]) 
print(x.sum())
print(x.sum(axis=0)) # 행방향으로 합친다 (첫번째 차원)
print(x.sum(axis=1)) # 열방향으로 합친다  (두번째 차원)

np.random.seed()
x = np.random.randn(25)
y = 10000 + 100*x
print(y)

################################################################33

# loc 정확한 인덱스 값으로 데이터 추리기
# iloc : 배열과 같이 몇번째인지를 이용하여 데이터 추리기
# df[df['국어']>50][['국어','영어']]

s1 = pd.Series({'국어':80,'영어':90,'수학':90})
s2 = pd.Series({'국어':90,'영어':70,'수학':60})
s3 = pd.Series({'국어':70,'영어':60,'수학':80})
s4 = pd.Series({'국어':30,'영어':40,'수학':70})
df=pd.DataFrame([s1,s2,s3,s4],index=['춘향','몽룡','향단','방자'])

# print(df['수학'])
# print(df[['국어','영어']])
df['평균'] = (df['국어']+df['영어']+df['수학'])/3
print(df.loc['방자'])
