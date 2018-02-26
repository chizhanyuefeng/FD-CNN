# -*- coding:UTF-8 -*-

import PIL.Image as Image
import numpy as np
import matplotlib.pyplot as plt

def normalize_sensor_data(data):
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

def data2image(data):
    '''
    将规范化后的传感器数据转化为图像数据
    :param data: 规范后的数据
    :return: 生成好的图像数据
    '''
    if data.shape != [3,400]:
        print('需要转化的数据类型不匹配，错误shape=',data.shape)
        return None

    r = Image.fromarray(data[0]).convert('L')
    g = Image.fromarray(data[1]).convert('L')
    b = Image.fromarray(data[2]).convert('L')

    image = Image.merge('RGB',(r,g,b))

    plt.imshow(image)

    return image



if __name__ == '__main__':
    data = np.arange(1200)
    data2image(data)