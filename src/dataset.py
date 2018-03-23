# -*- coding:UTF-8 -*-

'''
需求:输入batchsize.输出batchsize大小的batch_x(跌倒或日常数据)以及
    对应的label值batch_y.一个label格式[跌倒bool,日常bool].
    例如:一份跌倒数据的label为[1,0].日常数据的label为[0,1]
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
