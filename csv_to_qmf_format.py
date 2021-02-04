import numpy as np

'''
    程序功能:将.csv文件转化为qmf中要求的文件格式
'''

if __name__=='__main__':
    train_in_path = 'foursquare_train.csv'
    test_in_path = 'foursquare_test.csv'

    train_out_path = 'foursquare_train.txt'
    test_out_path = 'foursquare_test.txt'

    train_mat = np.loadtxt(train_in_path, delimiter = ",", dtype=int)
    test_mat = np.loadtxt(test_in_path, delimiter = ",", dtype=int)

    np.savetxt(train_out_path, train_mat, delimiter=' ', fmt='%d')
    np.savetxt(test_out_path, test_mat, delimiter=' ', fmt='%d')