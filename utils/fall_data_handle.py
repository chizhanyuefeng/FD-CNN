# -*- coding:UTF-8 -*-

import os
import pandas as pd
import data_graph as dp

FALL_DATA_SAVE_FILE = "E:\Master\FallDetection\\fall_down_detection.git\data\\newfall_data.csv"

def txt2csv(txt_file):
    """
    将txt文件复制并转化成csv文件
    :param txt_file: txt格式文件路径
    :return: 返回转化后的csv文件
    """
    try:
        file = open(txt_file, "r")
        file.close()
    except IOError:
        print(txt_file, "文件不存在或无法读取！")
        return txt_file

    with open(txt_file, "r") as f:
        # 读取文件中所有行内容
        lines = f.readlines()

    # 将txt文件转化为csv文件格式名
    csv_name = txt_file.replace("txt", "csv")
    # 新建csv文件
    # 下面的代码是为moblieFall进行的转化
    '''with open(csv_name, "w+") as file_w:
        for line in lines:
            if "#" in line:
                continue
            if "@DATA" in line:
                if "acc" in csv_name:
                    file_w.write("timestamp,ax,ay,az\n")
                elif "gyro" in csv_name:
                    file_w.write("timestamp,gx,gy,gz\n")
                elif "ori" in csv_name:
                    file_w.write("timestamp,ox,oy,oz\n")
                else:
                    break
                continue

            if line.isspace():
                continue
            file_w.write(line)
    '''
    # 下面的代码是为sisfall进行的转化
    with open(csv_name, "w+") as file_w:
        #file_w.seek(0, os.SEEK_SET)
        file_w.write('a1x,a1y,a1z,gyro_x,gyro_y,gyro_z,acc_x,acc_y,acc_z\n')
        flag = 0
        for line in lines:
            flag = flag+1
            if flag%2==0:
                if ';' in line:
                    line = line.replace(';', '')
                file_w.write(line)


    print("将",txt_file,"转化成",csv_name)
    return csv_name

def extract_data(acc_csv_file,begin,end,label=0,save_data_file=FALL_DATA_SAVE_FILE):
    """
    提取数据，根据参数，截取定长数据来存储到new_data_file中.
    截取的数据长度=end+1-begin
    :param acc_csv_file: 需要提取的csv数据文件
    :param begin: 数据的起始段
    :param end: 数据的终止段
    :param label: 数据分类类型
    :param save_data_file: 攫取的数据存储文件
    :return: 返回存储好的文件
    """

    if (end-begin)!=200:
        print('数据截取长度不为200份')
        return 'error'

    try:
        acc_data = pd.read_csv(acc_csv_file)
    except IOError:
        print(acc_csv_file,"文件无法打开或不存在！")
        return acc_csv_file
    else:
        print(acc_csv_file,"成功读取")

    if "acc" in acc_csv_file:
        gyro_csv_file = acc_csv_file.replace("acc","gyro")
    else:
        print(acc_csv_file,"此文件不是加速度传感器csv文件,无法提取数据！")
        return acc_csv_file

    try:
        gyro_data = pd.read_csv(gyro_csv_file)
    except IOError:
        print(gyro_csv_file,"文件无法打开或不存在！")
        return gyro_csv_file
    else:
        print(gyro_csv_file, "成功读取")

    if not os.path.exists(save_data_file):
        print('文件存储路径有问题:',save_data_file)
        return None

    acc_extract_data = acc_data.iloc[begin:end, 1:4].values
    gyro_extract_data = gyro_data.iloc[begin:end, 1:4].values

    #print(gyro_data.shape)
    #print(os.path.exists(save_data_file))

    with open(save_data_file,"a+") as data_file:
        data_file.seek(0,os.SEEK_SET)
        if data_file.read()=="":
            data_file.write("label")
            for i in range(1200):
                data_file.write(","+str(i+1))
            data_file.write("\n")

        data_file.seek(0, os.SEEK_END)
        #在数据每一行中，第一位代表数据标签。0代表跌倒数据,非0代表日常活动数据
        data_file.write(str(label))

        for data in acc_extract_data:

            line_data = ","+str(data[0])+","+str(data[1])+","+str(data[2])
            data_file.write(line_data)

        for data in gyro_extract_data:
            print(data.shape)
            line_data = ","+str(data[0])+","+str(data[1])+","+str(data[2])
            data_file.write(line_data)

        #传感器有加速度和陀螺仪，所以提取完陀螺仪后自动完成换行，方便提取新的一行数据
        data_file.write("\n")
    print("从",acc_csv_file,"和",gyro_csv_file,"中各提取",str(end-begin),
          "份数据。并保存至",save_data_file)
    return save_data_file

def find_txt_data_file(path):
    """
    查找所有txt数据文件，并转化成csv文件
    :param path: 文件绝对路径
    :return: 无
    """
    if not os.path.exists(path):
        print('路径存在问题：',path)
        return None

    for i in os.listdir(path):
        if os.path.isfile(path+"/"+i):
            #if ("txt" in i) and (("acc" in i) or ("gyro" in i)):
            if ('txt' in i) and ('_' in i):
                txt2csv(path+"/"+i)
        else:
            find_txt_data_file(path+"/"+i)


def main():

    path = 'E:\Master\FallDetection\MobiFall_Dataset_v2.0\sub31\FALLS\SDL'

    #find_txt_data_file('E:\Master\FallDetection\MobiFall_Dataset_v2.0')

    for i in os.listdir(path):
        file = path + '\\' + i
        if os.path.isfile(file):
            if ('acc' in i) and ('csv' in i):
                print('开始截取',i,'文件')
                dp.fall_line_chart(file)
                begin = input('起始：')
                #end = input('终止：')
                extract_data(file, int(begin), int(begin) + 200)

    print("截取完成")

    # f = pd.read_csv(FALL_DATA_SAVE_FILE)
    # print(f.head())
    # print(f.shape)
    # 测试代码
    #txt2csv("../data/BSC_acc_1_1.txt")
    #extract_data("../data/BSC_acc_1_1.csv",200,300)

    # file = pd.read_csv(FALL_DATA_SAVE_FILE)
    # print(file.shape)
    #
    # print(file.tail())

    #find_txt_data_file("/home/tony/fall_data/MobiFall_Dataset_v2.0")


if __name__=="__main__":
    # main()
    #txt2csv('test.txt')
    find_txt_data_file('/home/tony/fall_research/fall_data/SisFall_dataset/SisFall_dataset')