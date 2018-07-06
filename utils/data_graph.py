# -*- coding:UTF-8 -*-

import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

coord_x = []

def on_button_press(event):
    '''
    鼠标点击响应事件
    :param event:
    :return:
    '''
    global coord_x
    coord_x.append(int(event.xdata))

    length = len(coord_x)
    plt.subplot(2,1,1)
    plt.hlines(event.ydata,coord_x[length-1],coord_x[length-1]+200)
    plt.subplot(2, 1, 2)
    plt.hlines(event.ydata, coord_x[length-1], coord_x[length-1] + 200)

    plt.draw()


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

def adl_line_chart(csv_file,data_num=1):
    '''
    绘制日常行为运动数据折线图
    :param csv_file: 日常行为运动数据图
    :param data_num: 截取数据量
    :return: 截取的数据和截取的数据量
    '''

    if os.path.exists(csv_file) == False:
        print(csv_file,'文件不存在！')
        return None
    data = pd.read_csv(csv_file)
    num = data.acc_x.size

    global coord_x
    coord_x.clear()

    # 获取标签和其最终的位置
    # label_dict = {}
    # for i in range(num):
    #     label_dict[data.label[i]] = i

    x = np.arange(num)
    fig = plt.figure(1,figsize=(100,60))
    # 子表1绘制加速度传感器数据
    plt.subplot(2,1,1)
    plt.title('acc')
    plt.plot(x, data.acc_x, label='x', color='red')
    plt.plot(x, data.acc_y, label='y', color='green')
    plt.plot(x, data.acc_z, label='z', color='blue')

    acc_max = max(data.acc_x.max(),data.acc_y.max(),data.acc_z.max())
    acc_min = min(data.acc_x.min(),data.acc_y.min(),data.acc_z.min())

    # for key in label_dict:
    #     plt.vlines(label_dict[key],acc_min,acc_max)
    #     plt.annotate(key,xy=(label_dict[key]-200,acc_max))

    # 添加解释图标
    plt.legend()
    x_flag = np.arange(0,num,num/10)
    plt.xticks(x_flag)

    # 子表2绘制陀螺仪传感器数据
    plt.subplot(2,1,2)
    plt.title('gyro')
    plt.plot(x, data.gyro_x, label='x', color='red')
    plt.plot(x, data.gyro_y, label='y', color='green')
    plt.plot(x, data.gyro_z, label='z', color='blue')

    gyro_max = max(data.gyro_x.max(),data.gyro_y.max(),data.gyro_z.max())
    gyro_min = min(data.gyro_x.min(),data.gyro_y.min(),data.gyro_z.min())

    # for key in label_dict:
    #     plt.vlines(label_dict[key], gyro_min,gyro_max)
    #     plt.annotate(key, xy=(label_dict[key]-200, gyro_max))
    # 添加解释图标
    plt.legend()
    plt.xticks(x_flag)

    # 鼠标点击事件
    fig.canvas.mpl_connect('button_press_event', on_button_press)

    plt.show()

    return coord_x,data_num


def main():
    """
    测试代码
    :return:
    """

    x = adl_line_chart('/home/tony/fall_research/fall_data/MobiAct_Dataset_v2.0/Annotated Data/JOG/JOG_1_1_annotated.csv',6)
    print('pos:', x)

if __name__ == '__main__':
    main()