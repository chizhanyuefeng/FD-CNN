# -*- coding:UTF-8 -*-

'''
将读取的数据直接用于tensorflow
'''
import pandas as pd
import numpy as np

def read_data(data_path):
    '''
    读取跌倒和日常数据
    :param data_path:　跌到数据和日常数据的文件路径
    :return:　
    '''
    # TODO:从csv文件读取数据
    train_x = np.array((2000,400))
    train_y = np.array((2000,1))
    test_x = np.array((50,400))
    test_y = np.array((50,1))

    return train_x,train_y,test_x,test_y

def get_data_batch(size):
    '''
    获取size份数据
    :param size: batchsize
    :return:
    '''
    # TODO: 需要实现从数据中随机获取size份数据,采用抽样不放回策略
    batch_x = np.array([2,3])
    batch_y = np.array([2,3])
    return batch_x,batch_y
