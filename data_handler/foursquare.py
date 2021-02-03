import numpy as np
import random


class FourSquareHandler:
    def __init__(self, data_path):
        self._path = data_path
        A = np.loadtxt(self._path, dtype=int)
        self._uids = A[:,0]
        self._vids = A[:,1]
        self._count = A.shape[0]
        # 去重
        self._unique()
        self._user_num = 0
        self._index = None

    def discard_low_rate_user(self, lower_bound):
        '''
        去掉数量少于lower_bound的uid，并更新 self._count
        :param lower_bound: 保留的uid的最小数量, int类型
        :return: None
        '''
        unique_uid = np.unique(self._uids)
        retain_list = []
        tc = 0
        for uid in unique_uid: # 找到要保留的list
            res = list(np.where(self._uids==uid)[0])
            if len(res) >= lower_bound:
                retain_list += res
                tc += 1
        self._count = len(retain_list)
        self._uids = self._uids[retain_list]
        self._vids = self._vids[retain_list]
        self._user_num = tc
        print("self._count = ", self._count)
        print("self._user_num = ", self._user_num)
        unique_vid = np.unique(self._vids)
        self._item_num = len(unique_vid)
        print("self._item_num = ", self._item_num)
        self._rearrange_id()

    def _rearrange_id(self):
        '''
        将uid重新排列,按1到self._count排列
        同理，也将vid重新排列
        :return: None
        '''
        # 处理uids
        dic = dict()
        j = 0
        for i in range(1, self._user_num + 1):
            while j < self._count and self._uids[j] in dic.values():
                j += 1
            dic[i] = self._uids[j]
        self._index = list()
        for i in range(1, self._user_num + 1):
            w = list(np.where(self._uids==dic[i])[0])
            self._uids[w] = i
            self._index.append(max(w))

        # 处理vids
        dic = dict()
        j = 0
        for i in range(1, self._item_num + 1):
            while j < self._count and self._vids[j] in dic.values():
                j += 1
            dic[i] = self._vids[j]
        for i in range(1, self._item_num + 1):
            w = list(np.where(self._vids==dic[i])[0])
            self._vids[w] = i
        print("self._uids = \n", self._uids)
        print("self._vids = \n", self._vids)

    def _unique(self):
        '''
        去除重复
        :return: None
        '''
        l = []
        for i in range(self._count):
            if (self._uids[i], self._vids[i]) not in l:
                l.append((self._uids[i], self._vids[i]))
        self._count = len(l)
        nuids = []
        nvids = []
        for i in range(self._count):
            nuids.append(l[i][0])
            nvids.append(l[i][1])
        self._uids = np.array(nuids, dtype=int)
        self._vids = np.array(nvids, dtype=int)

    def get_handled_datasets(self, train_number):
        '''
        随机选择产生训练集和测试集
        :param train_number: 对每个uid, 选择进入训练集的vid的数量
        :return: 训练集, 测试集    均为元组类型,元组的元素为list
        '''
        end = 0
        train_users = []
        train_items = []
        test_users = []
        test_items = []
        for i in range(self._user_num):
            start = end
            end = self._index[i] + 1
            user_data = self._uids[start:end]
            item_data = self._vids[start:end]
            length = end-start
            l = list(range(length))
            random.shuffle(l)
            rl = list(set(range(length)) - set(l[0:train_number]))
            train_user_data = list(np.array(user_data)[l[0:train_number]])
            train_item_data = list(np.array(item_data)[l[0:train_number]])
            test_user_data = list(np.array(user_data)[rl])
            test_item_data = list(np.array(item_data)[rl])
            train_users += train_user_data
            train_items += train_item_data
            test_users += test_user_data
            test_items += test_item_data
        return (train_users, train_items), (test_users, test_items)
