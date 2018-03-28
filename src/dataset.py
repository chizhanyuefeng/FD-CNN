# -*- coding:UTF-8 -*-

'''
需求:输入batchsize.输出batchsize大小的batch_x(跌倒或日常数据)以及
    对应的label值batch_y.一个label格式[跌倒bool,日常bool].
    例如:一份跌倒数据的label为[1,0].日常数据的label为[0,1]
'''

import os
import pandas as pd
import numpy as np


DATA_PATH = '../data/dataset'
#data = '../data/dataset/data.csv'

class DataSet:
    # 定义私有属性
    _train_x = []
    _train_y = []
    _test_x = []
    _test_y = []
    _index_in_epoch = 0
    _epochs_completed = 0
    _num_examples = 2000

    # 定义构造方法
    def __init__(self,data_path):
        fs = os.listdir(data_path)
        for f in fs:
            file_path = os.path.join(data_path, f)
            if f == 'fall_data.csv':
                fall_data = pd.read_csv(file_path,index_col=False)
            if f == 'adl_data.csv':
                adl_data = pd.read_csv(file_path,index_col=False)
        alldata = fall_data.append(adl_data)
        np.random.shuffle(alldata.values)
        # alldata.to_csv(data, index=False)
        for i in range(0,self._num_examples):
            self._train_x.append(alldata.iloc[i, 1:1201])
            if alldata.iloc[i,0] == 0:
                self._train_y.append([1,0])
            else:
                self._train_y.append([0,1])
        # print(len(alldata.label))
        for i in range(self._num_examples,len(alldata.label)):
            self._test_x.append(alldata.iloc[i,1:1201])
            if alldata.iloc[i,0] == 0:
                self._test_y.append([1,0])
            else:
                self._test_y.append([0,1])

    @property
    def train_x(self):
        return self._train_x

    @property
    def train_y(self):
        return self._train_y

    @property
    def test_x(self):
        return self._test_x

    @property
    def test_y(self):
        return self._test_y

    @property
    def index_in_epoch(self):
        return self._index_in_epoch

    @property
    def epochs_completed(self):
        return self._epochs_completed

    def next_batch(self, batch_size):
        '''
        获取size份数据
        :param size: batchsize
        :return:
        '''
        # TODO: 需要实现从数据中随机获取size份数据,采用抽样不放回策略
        start = self._index_in_epoch
        if start + batch_size > self._num_examples:
            # Finished epoch
            self._epochs_completed += 1
            # Get the rest examples in this epoch
            rest_num_examples = self._num_examples - start
            if rest_num_examples != 0:
                x_rest_part = self.train_x[start:self._num_examples]
                y_rest_part = self.train_y[start:self._num_examples]
                # Start next epoch
                start = 0
                self._index_in_epoch = batch_size - rest_num_examples
                end = self._index_in_epoch
                x_new_part = self.train_x[start:end]
                y_new_part = self.train_y[start:end]
                batch_x,batch_y = np.concatenate(
                    (x_rest_part, x_new_part), axis=0), np.concatenate(
                    (x_rest_part, y_new_part), axis=0)
            else:
                # Start next epoch
                start = 0
                self._index_in_epoch = batch_size - rest_num_examples
                end = self._index_in_epoch
                batch_x = self.train_x[start:end]
                batch_y = self.train_y[start:end]
        else:
            self._index_in_epoch += batch_size
            end = self._index_in_epoch
            batch_x = self.train_x[start:end]
            batch_y = self.train_y[start:end]

        return np.array(batch_x),np.array(batch_y)

    def get_test_data(self):
        x = self.test_x
        y = self.test_y
        return np.array(x),np.array(y)

    def get_train_data(self):
        x = self.train_x
        y = self.train_y
        return np.array(x),np.array(y)

def main():
    # Test Code
    dataset = DataSet(DATA_PATH)
    # print(dataset.index_in_epoch)
    # print(dataset.train_x[1999])
    # print(dataset.train_y[150])
    # print(dataset.test_x)
    # print(dataset.test_y)
    #for i in range(0,45):
    x,y=dataset.get_test_data()
    num = np.array(y)
    print(num.shape)
    #print(dataset.epochs_completed)


if __name__ == '__main__':
    main()