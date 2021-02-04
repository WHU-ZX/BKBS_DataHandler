import json
import numpy as np
from data_handler.foursquare import FourSquareHandler

'''
    程序功能，根据Foursquare的原始数据集产生sql-rank需要的训练集和测试集
'''

if __name__=='__main__':
    with open('./config.json', 'r') as load_f:
        config_dict = json.load(load_f)
    IN_PATH = config_dict['IN_PATH']
    TRAIN_OUT_PATH = config_dict['TRAIN_OUT_PATH']
    TEST_OUT_PATH = config_dict['TEST_OUT_PATH']
    handler = FourSquareHandler(IN_PATH)
    handler.discard_low_rate_user(20)
    train, test = handler.get_handled_datasets(10)
    train_len = len(train[0])
    test_len = len(test[0])
    train_mat_T = np.array([train[0], train[1], np.ones(train_len)], dtype=int)
    test_mat_T = np.array([test[0], test[1], np.ones(test_len)], dtype=int)
    train_mat = np.transpose(train_mat_T)
    test_mat = np.transpose(test_mat_T)
    np.savetxt(TRAIN_OUT_PATH, train_mat, delimiter=',', fmt='%d')
    np.savetxt(TEST_OUT_PATH, test_mat, delimiter=',', fmt='%d')