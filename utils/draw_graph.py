# -*- coding:UTF-8 -*-

import os
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import pandas as pd
import numpy as np
from abc import ABCMeta,abstractmethod

class Data_graph(object):
    '''
    绘制图片接口类
    '''
    def on_mouse_press(self,event):
        pass

    def on_ok_button(self,event):
        pass

    def on_backout_button(self,event):
        pass

    def update_graph(self,event):
        pass

    def draw_button(self,name, point, func):
        point = plt.axes(point)
        button = Button(point, name)
        button.on_clicked(func)
        return button


class ADL_data_graph(Data_graph):
    '''
    绘制日常数据折线图
    '''

    def __init__(self,csv_file,extract_data_num):

        if os.path.exists(csv_file) == False:
            print(csv_file, '文件不存在！')
            return
        self.data = pd.read_csv(csv_file)
        num = data.timestamp.size

        # 获取标签和其最终的位置
        label_dict = {}
        for i in range(num):
            label_dict[data.label[i]] = i

        x = np.arange(num)

        self.data_num = extract_data_num
        self.figure = plt.figure(1,figsize=(15,7))
        self.subplot1 = self.figure.add_subplot(2,1,1)
        self.subplot2 = self.figure.add_subplot(2,1,2)
        self.__graph_ui()

        # 鼠标点击事件
        fig.canvas.mpl_connect('button_press_event', self.on_mouse_press)
        global backout_button, ok_button
        backout_button = self.draw_button('backout', [0.93, 0.8, 0.05, 0.03], self.on_backout_button)
        ok_button = self.draw_button('ok', [0.93, 0.85, 0.05, 0.03], self.on_ok_button)


    def __graph_ui(self):
        num = self.data.timestamp.size

        # 获取标签和其最终的位置
        label_dict = {}
        for i in range(num):
            label_dict[self.data.label[i]] = i

        x = np.arange(num)
        # 子表1绘制加速度传感器数据
        self.subplot1.title('acc')
        self.subplot1.plot(x, self.data.acc_x, label='x')
        self.subplot1.plot(x, self.data.acc_y, label='y')
        self.subplot1.plot(x, self.data.acc_z, label='z')

        acc_max = max(self.data.acc_x.max(), self.data.acc_y.max(), self.data.acc_z.max())
        acc_min = min(self.data.acc_x.min(), self.data.acc_y.min(), self.data.acc_z.min())

        for key in label_dict:
            self.subplot1.vlines(label_dict[key], acc_min, acc_max)
            self.subplot1.annotate(key, xy=(label_dict[key] - 200, acc_max))

        # 添加解释图标
        self.subplot1.legend()
        self.subplot1.xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200])

        # 子表2绘制陀螺仪传感器数据
        self.subplot2.title('gyro')
        self.subplot2.plot(x, self.data.gyro_x, label='x')
        self.subplot2.plot(x, self.data.gyro_y, label='y')
        self.subplot2.plot(x, self.data.gyro_z, label='z')

        gyro_max = max(self.data.gyro_x.max(), self.data.gyro_y.max(), self.data.gyro_z.max())
        gyro_min = min(self.data.gyro_x.min(), self.data.gyro_y.min(), self.data.gyro_z.min())

        for key in label_dict:
            self.subplot2.vlines(label_dict[key], gyro_min, gyro_max)
            self.subplot2.annotate(key, xy=(label_dict[key] - 200, gyro_max))
        # 添加解释图标
        self.subplot2.legend()
        self.subplot2.xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200])

    def on_mouse_press(self,event):
        pass

    def on_ok_button(self,event):
        pass

    def on_backout_button(self,event):
        pass

    def update_graph(self,event):
        pass



