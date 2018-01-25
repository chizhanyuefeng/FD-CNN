# -*- coding:UTF-8 -*-

def txt2csv(txt_file):
    """
    将txt文件复制并转化成csv文件
    :param txt_file: txt格式文件
    :return: 返回转化后的csv文件
    """
    with open(txt_file,"r") as file_r:
        lines = file_r.readlines()

    csv_name = txt_file.replace("txt","csv")

    with open(csv_name,"w+") as file_w:
        for line in lines:
            if("#" in line):
                continue
            if("@DATA" in line):
                file_w.write("timestamp,x,y,z\r\n")
                continue
            if(line.isspace()):
                continue
            file_w.write(line)

    return csv_name


#txt2csv("../data/BSC_acc_1_1.txt")



