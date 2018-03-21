# -*- coding:UTF-8 -*-

'''
用于修正数据样本。根据观测的数据结果来看，有些数据可能由于设备携带问题，
导致出现样本x,y,z轴反转或旋转。
需要修成数据的样本，来保证数据的准确性，和完成性。
'''

import os
import pandas as pd

# 数据错误类型
X_Y_INVERSION = 0 # 将x,y轴数据对调
X_Y_NEGATION = 1 # 将x,y轴数据分别取反
X_NEGATION = 2 # 将x轴数据进行取反
Y_NEGATION = 3 # 将y轴数据进行取反
Y_Z_NEGATION = 4 # 将y,z进行取反
X_Y_Z_NEGATION = 5 # 将x,y,z进行取反
X_Z_NEGATION = 6 # 将x,z进行取反

#test
# TEST_DATA_PATH = 'E:\Master\FallDetection\\test_dataall.csv'
# TEST_ROW = 5

def fix_data(data_file,row,fix_type):
    '''
    根据提供的数据和错误类型来修正数据,修改好数据后,将数据更新并保存.
    :param daya_file: 数据文件路径
    :param row: 数据所在文件中的行号(行号从0开始)
    :param fix_type: 错误类型
    :return: 返回修整好的数据a
    '''
    try:
        wrongdata = pd.read_csv(data_file)
    except IOError:
        print(data_file,"文件无法打开或不存在！")
        return data_file
    if row > len(wrongdata.label):
        print('错误行数超出范围！')
        return 'error'
    else:
        print(data_file,'读取成功！')

    if fix_type == 0:
        for i in range(1,len(wrongdata.columns)-1,3):
            temp = wrongdata.iloc[row,i]
            wrongdata.iat[row,i] = wrongdata.iloc[row,i+1]
            wrongdata.iat[row,i+1] = temp
        wrongdata.to_csv(data_file,index=False)

    elif fix_type == 1:
        for i in range(1,len(wrongdata.columns)-1,3):
            wrongdata.iat[row,i] = 0-wrongdata.iloc[row,i]
            wrongdata.iat[row,i+1] = 0-wrongdata.iloc[row,i+1]
        wrongdata.to_csv(data_file,index=False)

    elif fix_type == 2:
        for i in range(1,len(wrongdata.columns)-1,3):
            wrongdata.iat[row,i] = 0-wrongdata.iloc[row,i]
        wrongdata.to_csv(data_file,index=False)

    elif fix_type == 3:
        for i in range(1,len(wrongdata.columns)-1,3):
            wrongdata.iat[row,i+1] = 0-wrongdata.iloc[row,i+1]
        wrongdata.to_csv(data_file,index=False)

    else:
        print('错误类型发生错误！')
        return 'error'

    return data_file

def main():
    """
    测试代码
    :return:
    """
    # fix_data(TEST_DATA_PATH,TEST_ROW,Y_NEGATION)

if __name__ == '__main__':
    main()