import numpy as np
 
x = np.arange(1,10001)
y = np.arange(10001,20001)
z = np.zeros(10000)

# 주피터 기능 %%time 하면 코드실행측정시간 기록 (1번 2번 비교)

# 1. 리스트의 합
for i in range(10000):
    z[i] = x[i] + y[i] 

# 2. 벡터화 연산 사용 (numpy의 기능) : 훨씬 빠르다
z = x + y
print(x==y)
# print(x/y)

# 벡터화 연산 더 보여줄게
a = np.array([1,2,3,4])
b = np.array([4,2,2,4])
print(a[a>=b])
print(np.all(a==b)) # 모두 true가 아니므로 false
print(np.exp(a))
print(np.log(a))

# 브로드 캐스팅!!
k = np.arange(12).reshape(3,4)
print(100*k) # 스칼라(차원 X)와 벡터(1차원 혹은 2차원)연산
# 차원이 달라도 연산이 가능하다 : 브로드캐스팅!!!!!
# 저차원 배열이 고차원 배열에 맞추어 확장됨
# ex) a + 1 : x + np.array([1,1,1,1])
# ex)   + [0,1,2] : + [[0,1,2],[0,1,2],[0,1,2]] 이렇게 변할수도 있는거지

# 차원축소 연산!!
x = np.array([1,2,3,4])
# np.sum(x) // x.sum() // x.max() // x.min() // x.mean() // x.argmax() (max의 위치 변환)
# 등의 예시가 있다. 고차원 -> 저차원

# 고차원에서의 차원축소 연산
x = np.array([[1,1],[2,2]]) 
print(x.sum())
print(x.sum(axis=0)) # 행방향으로 합친다 (첫번째 차원)
print(x.sum(axis=1)) # 열방향으로 합친다  (두번째 차원)

# 정렬연산
x = np.array([4,3,5,7])
print(np.sort(x))
a = np.array([[4,3,5,7],[1,12,11,9],[2,15,1,14]])
print(np.sort(a,axis=0)) # 행방향으로 정렬한다
print(np.sort(a,axis=1)) # 열방향으로 정렬한다
## 연습문제 끝에 있어요!!! (주피터로 옮겼을수도) 11주!!

# 기술통계
x=np.array([1,2,3,4,5,6,7,8,9,7,6,5,4,4,3,2,34,234,234,234,123,213])
print(len(x))

print(np.sum(x)/len(x)) #평균
print(np.mean(x)) #평균
print(x.mean())

print(np.sum((x-np.mean(x))**2)/len(x)) # 분산
print(np.var(x)) # 분산
print(x.var())

print(np.sqrt(np.var(x))) # 표준편차
print(np.std(x)) # 표준편차
print(x.std())

print(np.max(x)) # 최댓값
print(np.min(x)) # 최솟값
print(np.median(x)) # 중앙값

print(np.percentile(x,0)) # 상위 0퍼센트 : 최솟값
print(np.percentile(x,100)) # 상위 100퍼센트 : 최댓값
print(np.percentile(x,25)) # 상위 25퍼센트 
print(np.percentile(x,50)) # 상위 0퍼센트 : 중앙값

## 난수와 놀자 ##
# 시드설정
np.random.seed(0) # 0번의 시드를 가질것이다. 시드를 다르게 해도되지(세팅값)
print(np.random.rand()) # 난 뭐가나올지 몰랐지만 컴퓨터는 알고있어
print(np.random.rand()) # seed 0으로 세팅되어있는거지
print(np.random.rand())
print(np.random.rand(5)) # 5개의 난수생성!!
# 배열형 난수
print(np.random.rand(3,5))
# 표준정규분포로부터 난수 생성
print(np.random.randn(5)) # 5개 생성
print(np.random.randn(3,5))
# 정수형 난수 생성
print(np.random.randint(10,size=5)) # 0부터 10(9까지)사이 난수 5개 생성
print(np.random.randint(10,20,size=5)) # 10에서 20(19까지)사이 난수 5개 생성
print(np.random.randint(10,20,size=(3,5))) # 10에서 20사이 난수 (3,5) 생성
# numpy 9강 연습문제 풀이 1,2,3
print(np.random.randint(0,2,size=10)) # 굳이 size=10 안하고 그냥 ,10해도 되네
print(np.mean(np.random.randint(1,7,size=100))) 
print((np.random.randn(25)*100)+10000)
## 이게 보니까 실행할때마다 다른값으로 랜덤하게 가려면 seed(0)이 아니라 seed() 해야되네

# | 이게 or & 이게 and
# Nan은 참고할게 없을때 나타나는 오류값!
# ds.notnull은 true인지 false인지 뽑아주는역할
