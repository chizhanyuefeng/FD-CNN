# -*- coding:UTF-8 -*-

'''
用于处理日常行为数据。
根据下载下来的数据文件，日常行为的数据文件解析和提取与跌到数据文件处理存在不同之处。

需要实现的功能：
1.通过调用data_graph里面的adl_line_chart方法查看需要截取的数据范围，
获取需要截取的数据。
2.日常行为数据传感器采集频率为200hz，而跌倒数据采集频率为100hz，
所以需要进步提取数据，并将提取的数据保存至新的csv文件中。

'''
import os
import pandas as pd
import data_graph as dp
# import matplotlib.pyplot as plt

ADL_DATA_SAVE_FILE = "E:\Master\FallDetection\fall_down_detection.git\data\adl_data.csv"
Label = {'STD':1,'WAL':2,'JOG':3,'JUM':4,'STU':5,'STN':6,'SCH':7,'SIT':8,'CHU':9,'CSI':10,'CSO':11,'LYI':12,'FOL':0,'FKL':0,'BSC':0,'SDL':0}

def extract_data(annotated_file,begin,end,label,save_data_file=ADL_DATA_SAVE_FILE):
    """
    提取数据，根据参数，截取定长数据来存储到new_data_file中.
    截取的数据长度=end+1-begin
    :param annotated_file: 需要提取的csv数据文件
    :param begin: 数据的起始段
    :param end: 数据的终止段
    :param label: 数据分类类型
    :param save_data_file: 攫取的数据存储文件
    :return: 返回存储好的文件
    """
    if (end-begin)!=400:
        print('数据截取长度不为400份')
        return 'error'
    try:
        annotated_data = pd.read_csv(annotated_file)
    except IOError:
        print(annotated_file,"文件无法打开或不存在！")
        return annotated_file
    else:
        print(annotated_file,"成功读取")

    acc_extract_data = annotated_data.iloc[begin:end:2, 2:5].values
    gyro_extract_data = annotated_data.iloc[begin:end:2, 5:8].values

    with open(save_data_file, "a+") as data_file:
        data_file.seek(0,os.SEEK_SET)
        if data_file.read()=="":
            data_file.write("label")
            for i in range(1200):
                data_file.write(","+str(i+1))
            data_file.write("\n")

        data_file.seek(0, os.SEEK_END)
        #在数据每一行中，第一位代表数据标签。0代表跌倒数据,非0代表日常活动数据
        data_file.write(str(Label[label]))

        for data in acc_extract_data:
            line_data = ","+str(data[0])+","+str(data[1])+","+str(data[2])
            data_file.write(line_data)

        for data in gyro_extract_data:
            line_data = ","+str(data[0])+","+str(data[1])+","+str(data[2])
            data_file.write(line_data)

        #传感器有加速度和陀螺仪，所以提取完陀螺仪后自动完成换行，方便提取新的一行数据
        data_file.write("\n")

    print("从",annotated_file,"文件中提取",str((end-begin)/2),"份数据。\n已保存至",save_data_file)

    return save_data_file

def main():
    path = 'E:\Master\FallDetection\MobiAct_Dataset_v2.0\Annotated Data\BSC'

    for i in os.listdir(path):
        file = path + '\\' + i
        if os.path.isfile(file):
            if ('annotated' in i) and ('csv' in i):
                print('开始截取',i,'文件')
                #dp.adl_line_chart(file)
                dp.fall_line_chart(file)
                begin = input('起始：')
                pdFile = pd.read_csv(file)
                lableName = pdFile.iat[begin,11]
                label = Label["BSC"]
                extract_data(file, int(begin), int(begin) + 400,label)

    print("截取完成！")

    #测试程序
    f = pd.read_csv(ADL_DATA_SAVE_FILE)
    print(f.head())
    print(f.shape)

if __name__ == "__main__":
    main()