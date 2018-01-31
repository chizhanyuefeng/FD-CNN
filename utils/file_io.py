# -*- coding:UTF-8 -*-
import pandas as pd
import numpy as np

def txt2csv(txt_file):
    """
    将txt文件复制并转化成csv文件
    :param txt_file: txt格式文件
    :return: 返回转化后的csv文件
    """
    with open(txt_file,"r") as file_r:
        # 读取文件中所有行内容
        lines = file_r.readlines()
    # 将txt文件转化为csv文件格式名
    csv_name = txt_file.replace("txt","csv")
    # 新建csv文件
    with open(csv_name,"w+") as file_w:
        for line in lines:
            if("#" in line):
                continue
            if("@DATA" in line):
                if("acc" in csv_name):
                    file_w.write("timestamp,ax,ay,az\n")
                elif("gyro" in csv_name):
                    file_w.write("timestamp,gx,gy,gz\n")
                elif("ori" in csv_name):
                    file_w.write("timestamp,ox,oy,oz\n")
                else:
                    break
                continue

            if(line.isspace()):
                continue
            file_w.write(line)

    return csv_name

def extract_data(file,begin,end,sensor=0,label=0,new_data_file="/home/tony/fall_data/fall_data.txt"):
    """
    提取数据，根据参数，截取定长数据来存储到new_data_file中.
    截取的数据长度=end+1-begin
    :param file: 需要提取的数据文件
    :param begin: 数据的起始段
    :param end: 数据的终止段
    :param sensor: 传感器标识符，0代表加速度传感器，1代表陀螺仪传感器
    :param label: 数据分类类型
    :param new_data_file: 攫取的数据存储文件
    :return: 返回存储好的文件
    """
    data_file = pd.read_csv(file)
    extract_data = data_file.iloc[begin:end+1,1:4].values

    with open(new_data_file,"a+") as data_file:
        if sensor == 0:
            #在数据每一行中，第一位代表数据标签。0代表跌倒数据,非0代表日常活动数据
            data_file.write(str(label)+",")
        for data in extract_data:
            line_data = str(data[0])+","+str(data[1])+","+str(data[2])+","
            data_file.write(line_data)
        if sensor !=0:
            #传感器有加速度和陀螺仪，所以提取完陀螺仪后自动完成换行，方便提取新的一行数据
            data_file.write("\n")

    return new_data_file

extract_data("../data/BSC_acc_1_1.csv",200,300)
