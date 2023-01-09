import numpy as np
import pandas as pd

a=np.array([[0,1,2,3,4],[5,6,7,8,9]])
b=np.array([[[0,1,2],[3,4,5]],[[4,5,6],[7,8,9]]])
c=np.array([[0,1,2],[3,4,5],[4,5,6],[7,8,9]])
# print(len(a))
# print(b.ndim)
# print(b.shape)
# print(len(c))
# print(b[1][0])

# x=np.array([0,1,2,3,4])
# x = np.array([1,2,3,4,5,6,7,8,9,10])
# y = np.array([1,2,3,4,5,6,7,8,9,10])
# y1 = y[y%3==0]
# y2 = y[y%2==0]
# print(np.intersect1d(y1,y2,assume_unique=True))
# x = np.array([1,2,3])
# y = np.array([1.0, 2.0, 3.0])
# print(x.dtype) #
x = np.array([1,3,True,False])
## numpy에서는 모두 통일된 값으로 처리해야하기문에 True : 1, False : 0로 계산
# print(x)
# print(np.arange(3,9,2))
# print(np.zeros((4,2,1)).ndim)
# x=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# y=x.reshpae(2,-1)
# print(y)
s=pd.Series([1,2,3],index=['s','b,','c'])
s2=pd.Series([1,2,3],index=['s','b,','k'])
print(s-s2)