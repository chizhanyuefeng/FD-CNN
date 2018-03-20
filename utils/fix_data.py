# -*- coding:UTF-8 -*-

'''
用于修正数据样本。根据观测的数据结果来看，有些数据可能由于设备携带问题，
导致出现样本x,y,z轴反转或旋转。
需要修成数据的样本，来保证数据的准确性，和完成性。
'''


# 数据错误类型
X_Y_INVERSION = 0 # 将x,y轴数据对调
X_Y_NEGATION = 1 # 将x,y轴数据分别取反
X_NEGATION = 2 # 将x轴数据进行取反
Y_NEGATION = 3 # 讲y轴数据进行取反


def fix_data(daya_file,row,fix_type):
    '''
    根据提供的数据和错误类型来修正数据,修改好数据后,将数据更新并保存.
    :param daya_file: 数据文件路径
    :param row: 数据所在文件中的行号(行号从0开始)
    :param fix_type: 错误类型
    :return: 返回修整好的数据a
    '''
