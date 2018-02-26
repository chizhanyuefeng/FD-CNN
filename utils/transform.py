# -*- coding:UTF-8 -*-

import PIL.Image as Image
import numpy as np

def data2image(data):
    '''
    将跌倒数据转化成图像数据
    :param data: 长度为1200的数组
    :return:
    '''
    # 初始大小为3*400的矩阵。3为RGB通道
    image = np.zeros(shape=[3,400],dtype=float)

    for i in range(400):
        # 传感器数据大小敢为-20~20，需要将其值拓展为0~255的数值
        image[0][i] = (data[3*i] + 20) * 5 # R通道，传感器x值
        image[1][i] = (data[3*i+ 1] + 20) * 5 # G通道，传感器y值
        image[2][i] = (data[3*i+ 2] + 20) * 5 # B通道，传感器z值

    print(image.shape)
    return image


if __name__ == '__main__':
    data = np.arange(1200)
    data2image(data)