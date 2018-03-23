# -*- coding:UTF-8 -*-

'''
用于修正数据样本。根据观测的数据结果来看，有些数据可能由于设备携带问题，
导致出现样本x,y,z轴反转或旋转。
需要修成数据的样本，来保证数据的准确性，和完成性。
'''

import os
import pandas as pd
import numpy as np

# 数据错误类型
X_Y_INVERSION = 0 # 将x,y轴数据对调
X_Y_NEGATION = 1 # 将x,y轴数据分别取反
X_NEGATION = 2 # 将x轴数据进行取反
Y_NEGATION = 3 # 将y轴数据进行取反
Y_Z_NEGATION = 4 # 将y,z进行取反
X_Y_Z_NEGATION = 5 # 将x,y,z进行取反
X_Z_NEGATION = 6 # 将x,z进行取反

# 修改数据所用宏
DATA_PATH = 'E:\Master\FallDetection\\fall_down_detection.git\data\FALL\\fall_data.csv'
ERROR_DATA_PATH = 'E:\Master\FallDetection\\fall_down_detection.git\data\FALL\BSC\error_data.csv'
WRONG_DATA_PATH = 'E:\Master\FallDetection\\fall_down_detection.git\data\FALL\BSC\wrong_data.csv'

# 合并数据所用宏
ROOT_FILE_PATH = 'E:\Master\FallDetection\\fall_down_detection.git\data\FALL'
MERGE_DATA_PATH = 'E:\Master\FallDetection\\fall_down_detection.git\data\MERGE\merge_FALL_data.csv'
HAVE_MERGED_INDEX_PATH = 'E:\Master\FallDetection\\fall_down_detection.git\data\MERGE\indexfile.csv'


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
            temp = wrongdata.iloc[row, i]
            wrongdata.iat[row, i] = wrongdata.iloc[row, i + 1]
            wrongdata.iat[row, i + 1] = temp
        wrongdata.to_csv(data_file,index=False)
        print('修改成功！')

    elif fix_type == 1:
        for i in range(1,len(wrongdata.columns)-1,3):
            wrongdata.iat[row, i] = 0 - wrongdata.iloc[row, i]
            wrongdata.iat[row, i + 1] = 0 - wrongdata.iloc[row, i + 1]
        wrongdata.to_csv(data_file,index=False)
        print('修改成功！')

    elif fix_type == 2:
        for i in range(1,len(wrongdata.columns)-1,3):
            wrongdata.iat[row, i] = 0 - wrongdata.iloc[row, i]
        wrongdata.to_csv(data_file,index=False)
        print('修改成功！')

    elif fix_type == 3:
        for i in range(1,len(wrongdata.columns)-1,3):
            wrongdata.iat[row, i + 1] = 0 - wrongdata.iloc[row, i + 1]
        wrongdata.to_csv(data_file,index=False)
        print('修改成功！')

    elif fix_type == 4:
        for i in range(1,len(wrongdata.columns)-1,3):
            wrongdata.iat[row, i + 1] = 0 - wrongdata.iloc[row, i + 1]
            wrongdata.iat[row, i + 2] = 0 - wrongdata.iloc[row, i + 2]
        wrongdata.to_csv(data_file,index=False)
        print('修改成功！')

    elif fix_type == 5:
        for i in range(1,len(wrongdata.columns)-1,3):
            wrongdata.iat[row, i] = 0 - wrongdata.iloc[row, i]
            wrongdata.iat[row, i + 1] = 0 - wrongdata.iloc[row, i + 1]
            wrongdata.iat[row, i + 2] = 0 - wrongdata.iloc[row, i + 2]
        wrongdata.to_csv(data_file,index=False)
        print('修改成功！')

    elif fix_type == 6:
        for i in range(1,len(wrongdata.columns)-1,3):
            wrongdata.iat[row, i] = 0 - wrongdata.iloc[row, i]
            wrongdata.iat[row, i + 2] = 0 - wrongdata.iloc[row, i + 2]
        wrongdata.to_csv(data_file,index=False)
        print('修改成功！')

    else:
        print('错误类型发生错误！')
        with open(WRONG_DATA_PATH, "a+") as wrong_data:
            wrong_data.seek(0, os.SEEK_SET)
            if wrong_data.read() == "":
                wrong_data.write("ROW,label")
                for i in range(1200):
                    wrong_data.write("," + str(i + 1))
                wrong_data.write("\n")
        check_wrong_data = pd.read_csv(WRONG_DATA_PATH)
        with open(WRONG_DATA_PATH, "a+") as wrong_data:
            wrong_data.seek(0, os.SEEK_END)
            flag = 0
            for data in check_wrong_data.ROW:
                if data == row:
                    flag = 1
            if flag == 0:
                wrong_data.write(str(row))
                for data in wrongdata.iloc[row, :]:
                    line_data = "," + str(data)
                    wrong_data.write(line_data)
                wrong_data.write("\n")
                print("错误数据已保存至文件", WRONG_DATA_PATH)
                for i in range(0,len(wrongdata.iloc[row])):
                    wrongdata.iat[row,i] = None
                wrongdata.to_csv(data_file, index=False)
                print("第" + str(row) + "行置空")
            else:
                print("第" + str(row) + "行错误数据已存在在" + WRONG_DATA_PATH + "文件中！")

def deleteEmpty(data_file):

    '''
    将修正后的数据中空行剔除.
    :param daya_file: 数据文件路径
    :return: 返回剔除空行的文件
    '''
    try:
        Empty_data = pd.read_csv(data_file)
    except IOError:
        print(data_file, "文件无法打开或不存在！")
        return data_file
    print(data_file, '读取成功！')

    print(len(Empty_data.label))
    for i in range(len(Empty_data.label)-1,-1,-1):
        row_data = Empty_data.iloc[i, 1]
        if np.isnan(row_data).any():
            Empty_data.drop(i,axis=0, inplace=True)
    Empty_data.to_csv(data_file, index=False)
    print(len(Empty_data.label))
    print("文件剔除空行成功！")

def mergedata(root_dir,save_data_file):
    fs = os.listdir(root_dir)
    for f in fs:
        root_path = os.path.join(root_dir, f)
        if not os.path.isdir(root_path):
            # print(f)
            if f != 'error_data.csv' and f != 'indexfile.csv' and f != 'wrong_data.csv':
                flag = 0
                with open(HAVE_MERGED_INDEX_PATH, "a+") as index_file:
                    index_file.seek(0, os.SEEK_SET)
                    if index_file.read() == "":
                        index_file.write("Name")
                        index_file.write("\n")
                index_data = pd.read_csv(HAVE_MERGED_INDEX_PATH)
                for file_name in index_data.iloc[:,0]:
                    if f == file_name:
                        flag = 1
                if flag == 0:
                    with open(save_data_file, "a+") as data_file:
                        data_file.seek(0, os.SEEK_SET)
                        if data_file.read() == "":
                            data_file.write("label")
                            for i in range(1200):
                                data_file.write("," + str(i + 1))
                            data_file.write("\n")
                        data_file.seek(0, os.SEEK_END)
                        source_data = pd.read_csv(root_path)
                        for i in range(0,len(source_data.label)):
                            for data in source_data.iloc[i,:]:
                                line_data = str(data) + ','
                                data_file.write(line_data)
                            data_file.write("\n")
                    with open(HAVE_MERGED_INDEX_PATH, "a+") as index_file:
                        index_file.seek(0, os.SEEK_END)
                        index_file.write(f)
                        index_file.write("\n")
                    print("已将文件" + f + "添加进" + save_data_file + "文件中" )
                else:
                    print(f + "文件已经合成完毕！")

        else:
            # print(root_path)
            mergedata(root_path,save_data_file)

def main():

    # 修正数据
    # error_data = pd.read_csv(ERROR_DATA_PATH)
    # for i in range(len(error_data.row)):
    #     Row = error_data.iloc[i, 0]
    #     Type = error_data.iloc[i, 1]
    #     fix_data(DATA_PATH,Row,Type)

    # 剔除空行
    # deleteEmpty(DATA_PATH)

    # 合并数据
    mergedata(ROOT_FILE_PATH,MERGE_DATA_PATH)



if __name__ == '__main__':
    main()