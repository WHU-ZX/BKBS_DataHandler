import numpy as np
import random

#### 测试numpy读取txt文件
# data_path = "original_datas/dataset_ubicomp2013_checkins.txt"
# a = np.loadtxt(data_path,dtype=int)
# user = a[:,0]
# print(a)
# print(a.shape[0])
# w = list(np.where(user==14860)[0])
# print(len(w))
# print(w)
# print(type(w))

#### 测试numpy数组去重
# a = np.array([1,1,3,2,2,5])
# b = np.unique(a)
# print(a)
# print(b)

#### 测试numpy中的维度
# A = np.array([[1,2,3],[4,5,6]])
# b = A[:,0]
# print(b.shape)
# c = np.array([1,2])
# print(c.shape)
# A[:,2] = c
# print(A)

#### 测试list的append功能是否能append list
# list = [1,2,3]
# lap = [7,4,1,7]
# # list.append(lap)
# print(list+lap)


#### 测试写入csv文件
# a = np.array([[1,2,3],[4,5,6],np.zeros(3)],dtype=int)
# print(np.transpose(a))
# print(a)
# np.savetxt('t.csv',a,delimiter=',',fmt='%d')

#### 测试源数据是否重复
path = "E:/py-workspace/BKBS_DataHandler/original_datas/dataset_ubicomp2013_checkins.txt"
A = np.loadtxt(path, dtype=int)
uids = A[:, 0]
vids = A[:, 1]
l = []
print(len(uids))
for i in range(len(uids)):
    if (uids[i],vids[i]) not in l:
        l.append((uids[i],vids[i]))
print(len(l))


