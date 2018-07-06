# -*- coding:UTF-8 -*-

'''
需求:输入batchsize.输出batchsize大小的batch_x(跌倒或日常数据)以及
    对应的label值batch_y.一个label格式[跌倒bool,日常bool].
    例如:一份跌倒数据的label为[1,0].日常数据的label为[0,1]

    Dataset类,构造(数据文件夹路径,分类)
    例如:[0,1,2]代表:'FALL','STD','WAL'
'''

import os
import pandas as pd
import numpy as np

DATA_PATH = '../data/dataset'
TRAIN_DATA = '../data/train.csv'
TEST_DATA = '../data/test.csv'

class DataSet:
    # 定义私有属性
    _train_x = []
    _train_y = []
    _test_x = []
    _test_y = []
    _index_in_epoch = 0
    _epochs_completed = 0
    _num_examples = 0

    # 定义构造方法
    def __init__(self,data_path,class_list,TEST_MODEL=False):
        class_num = len(class_list)

        if TEST_MODEL:
            all_data = pd.read_csv(TEST_DATA,index_col=False)
            for i in range(0,len(all_data.label)):
                label = all_data.iloc[i, 0]
                if label not in class_list:
                    continue
                # 提取传感器数据
                self._test_x.append(all_data.iloc[i, 1:1201])
                # 创建y
                loc = class_list.index(label)
                y = [0 for _ in range(class_num)]
                y[loc] = 1
                self._test_y.append(y)
        else:
            fs = os.listdir(data_path)
            all_data = pd.DataFrame()

            for f in fs:
                file_path = os.path.join(data_path, f)
                # 读取所有csv文件
                if 'csv' in f:
                    data = pd.read_csv(file_path, index_col=False)
                    all_data = all_data.append(data)

            np.random.shuffle(all_data.values)

            train_data = all_data[0:1000 * class_num]
            train_data.to_csv(TRAIN_DATA, index=False)

            test_data = all_data[1000 * class_num:]
            test_data.to_csv(TEST_DATA, index=False)

            self._num_examples = class_num * 1000

            for i in range(0,self._num_examples):
                label = all_data.iloc[i, 0]
                if label not in class_list:
                    continue
                # 提取传感器数据
                self._train_x.append(all_data.iloc[i, 1:1201])
                # 创建y
                loc = class_list.index(label)
                y = [0 for _ in range(class_num)]
                y[loc] = 1
                self._train_y.append(y)

            for i in range(self._num_examples,len(all_data.label)):
                label = all_data.iloc[i, 0]
                if label not in class_list:
                    continue
                # 提取传感器数据
                self._test_x.append(all_data.iloc[i, 1:1201])
                # 创建y
                loc = class_list.index(label)
                y = [0 for i in range(class_num)]
                y[loc] = 1
                self._test_y.append(y)

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
        return np.array(x), np.array(y)

    def get_train_data(self):
        x = self.train_x
        y = self.train_y
        return np.array(x), np.array(y)

    def _normalization(self, data):

        data = data / (256/2.0) - 1
        return data

def main():
    # Test Code
    dataset = DataSet(DATA_PATH,[0,3,6])
    # print(dataset.index_in_epoch)
    # print(dataset.train_x[1999])
    # print(dataset.train_y[150])
    # print(dataset.test_x)
    # print(dataset.test_y)
    #for i in range(0,45):
    x,y=dataset.get_train_data()
    #num = np.array(x)
    print(np.max(x))
    #print(dataset.epochs_completed)




if __name__ == '__main__':
    main()