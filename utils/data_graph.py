# -*- coding:UTF-8 -*-

import os
import matplotlib.pyplot as plt
import pandas as pd
import file_io as fio
import numpy as np

def fall_line_chart(csv_file):
    '''
    绘制跌倒数据折线图
    :param csv_file: 跌倒数据csv文件
    :return:
    '''
    if os.path.exists(csv_file) == False:
        print("文件不存在！")
        return csv_file

    data = pd.read_csv(csv_file)
    num = data.timestamp.size

    x = np.arange(num)
    if 'acc' in csv_file:
        plt.plot(x, data.ax, label="x")
        plt.plot(x, data.ay, label="y")
        plt.plot(x, data.az, label="z")
    elif 'gyro' in csv_file:
        plt.plot(x, data.gx, label="x")
        plt.plot(x, data.gy, label="y")
        plt.plot(x, data.gz, label="z")
    # 添加解释图标
    plt.legend()
    plt.xticks([0,100,200,300,400,500,600,700,800])
    plt.show()

def adl_line_chart(csv_file):
    '''
    绘制日常行为运动数据折线图
    :param csv_file: 日常行为运动数据图
    :return:
    '''
    if os.path.exists(csv_file) == False:
        print(csv_file,'文件不存在！')
        return csv_file
    data = pd.read_csv(csv_file)
    num = data.timestamp.size

    x = np.arange(num)
    plt.plot(x, data.acc_x, label='x')
    plt.plot(x, data.acc_y, label='y')
    plt.plot(x, data.acc_z, label='z')

    # 添加解释图标
    plt.legend()
    plt.xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200])
    plt.show()


def main():
    """
    测试代码
    :return:
    """
    # csv_name = fio.txt2csv("../data/BSC_acc_1_1.txt")
    # csv_name2 = fio.txt2csv("../data/BSC_acc_1_2.txt")
    # csv_name3 = fio.txt2csv("../data/BSC_acc_1_3.txt")
    #
    # line_chart(csv_name)
    # line_chart(csv_name2)
    # line_chart(csv_name3)

    adl_line_chart('/home/tony/fall_data/MobiAct_Dataset_v2.0/Annotated Data/CHU/CHU_1_3_annotated.csv')


if __name__ == '__main__':
    main()