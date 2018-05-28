
# -*- coding:UTF-8 -*-

import progressbar as pb
import PIL.Image as Image
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

SAVEFIG_PATH = '../data/raw_data/ADL/STU/figure/'
SAVEIMG_PATH = '../data/raw_data/ADL/STU/image/'
SOURCE_DATA_PATH = '../data/raw_data/ADL/STU/STU_data.csv'

#DATASET_FALL_PATH = '../data/dataset/fall_data.csv'
DATASET_ADL_PATH = '../data/dataset/fall_data.csv'

value_max = 0
value_min = 0

def transform_sensor_data(sensor_data,num,data_move=20,data_scale=6,MAKE_FIGURE = False):
    '''
    将跌倒数据规范化
    :param sensor_data: 长度为1200的数组
    :return:
    '''
    # 初始大小为3*400的矩阵。3为RGB通道
    transform_data = np.zeros(shape=[3,400],dtype=np.int)
    re = np.zeros(shape=[3,400],dtype=np.float)

    for i in range(400):
        # 传感器数据大小敢为-20~20，需要将其值拓展为0~255的数值
        if i>=200:
            # 陀螺仪数据
            scale = 250/(value_max-value_min)
            transform_data[0][i] = int((sensor_data[3 * i] - value_min) * scale)  # R通道，传感器x值
            transform_data[1][i] = int((sensor_data[3 * i + 1] - value_min) * scale)  # G通道，传感器y值
            transform_data[2][i] = int((sensor_data[3 * i + 2] - value_min) * scale)  # B通道，传感器z值
        else:
            # 加速度数据
            transform_data[0][i] = (sensor_data[3*i] + data_move) * data_scale # R通道，传感器x值
            transform_data[1][i] = (sensor_data[3*i+ 1] + data_move) * data_scale # G通道，传感器y值
            transform_data[2][i] = (sensor_data[3*i+ 2] + data_move) * data_scale # B通道，传感器z值

        if MAKE_FIGURE:
            re[0][i] = (sensor_data[3 * i] )  # R通道，传感器x值
            re[1][i] = (sensor_data[3 * i + 1])   # G通道，传感器y值
            re[2][i] = (sensor_data[3 * i + 2])   # B通道，传感器z值

    if MAKE_FIGURE:
        x = np.arange(400)
        plt.figure(1)

        plt.subplot(211)
        plt.title('processed data')
        plt.plot(x, transform_data[0], label='x', color='red')
        plt.plot(x, transform_data[1], label='y', color='green')
        plt.plot(x, transform_data[2], label='z', color='blue')
        plt.legend()

        plt.subplot(212)
        plt.title('raw data')
        plt.plot(x, re[0], label='x', color='red')
        plt.plot(x, re[1], label='y', color='green')
        plt.plot(x, re[2], label='z', color='blue')
        plt.legend()

        #plt.show()
        plt.savefig(SAVEFIG_PATH + str(num) + '.png')

        plt.close()

    transform_data = transform_data.reshape([3,20,20])

    return transform_data

def data2image(transform_data,num):
    '''
    将规范化后的传感器数据转化为图像数据
    :param transform_data: 规范后的数据
    :param num: 图像编号
    :return: 生成好的图像数据
    '''
    if transform_data.shape != (3,20,20):
        print('需要转化的数据类型不匹配，错误shape=',transform_data.shape)
        return None

    r = Image.fromarray(transform_data[0],'L')#.convert('L')
    g = Image.fromarray(transform_data[1],'L')#.convert('L')
    b = Image.fromarray(transform_data[2],'L')#.convert('L')

    image = Image.merge('RGB',(r,g,b))
    image.save(SAVEIMG_PATH + str(num) + '.png','png')
    return image

def make_figure():
    '''
    将未处理数据进行可视化，生成figure和对应的image
    :return:
    '''
    fall_data = pd.read_csv(SOURCE_DATA_PATH,index_col=False)

    num = fall_data.label.size

    pbar = pb.ProgressBar(maxval=num, widgets=['处理进度',pb.Bar('=', '[', ']'), '',pb.Percentage()])

    for i in range(num):
        pbar.update(i + 1)
        sensor_data = fall_data.iloc[i:i+1, 1:1201].values.reshape([1200, 1])
        global value_max
        global value_min
        value_max = max(fall_data.iloc[i:i+1, 601:1201].values.reshape([600,]))
        value_min = min(fall_data.iloc[i:i+1, 601:1201].values.reshape([600,]))
        if not np.isnan(sensor_data).any():
            transform_data = transform_sensor_data(sensor_data,i,MAKE_FIGURE=True)
            data2image(transform_data, i)
    pbar.finish()

def make_dataset():
    '''
    生成规范数据集
    :return:
    '''
    # 将未处理数据（即范围-20-20的数据）转化为0-250，并将数据转为rgb存储
    data = pd.read_csv(SOURCE_DATA_PATH,index_col=False)

    num = data.label.size

    pbar = pb.ProgressBar(maxval=num, widgets=['处理进度', pb.Bar('=', '[', ']'), '', pb.Percentage()])

    for i in range(num):
        pbar.update(i + 1)
        sensor_data = data.iloc[i:i+1, 1:1201].values.reshape([1200, ])
        global value_max
        global value_min
        value_max = max(data.iloc[i:i + 1, 601:1201].values.reshape([600, ]))
        value_min = min(data.iloc[i:i + 1, 601:1201].values.reshape([600, ]))
        transform_data = transform_sensor_data(sensor_data,i,MAKE_FIGURE=True).reshape([1200,])
        for j in range(1200):
            data.iat[i,j+1] = transform_data[j]

    data.to_csv(DATASET_ADL_PATH,index=False)
    pbar.finish()

if __name__=='__main__':

    make_figure()

    #make_dataset()
    pass