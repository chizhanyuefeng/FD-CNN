# -*- coding:UTF-8 -*-


import matplotlib.pyplot as plt
import pandas as pd
import file_io as fio
import numpy as np

def line_chart(csv_file):
    data = pd.read_csv(csv_file)

    num = data.timestamp.size
    x = np.arange(num)
    plt.plot(x, data.ax, label="x")
    plt.plot(x, data.ay, label="y")
    plt.plot(x, data.az, label="z")
    plt.legend()
    plt.xticks([0,100,200,300,400,500,600,700,800])
    plt.show()
    #data.plot()

def main():
    """
    测试代码
    :return:
    """
    csv_name = fio.txt2csv("../data/BSC_acc_1_1.txt")
    csv_name2 = fio.txt2csv("../data/BSC_acc_1_2.txt")
    csv_name3 = fio.txt2csv("../data/BSC_acc_1_3.txt")

    line_chart(csv_name)
    line_chart(csv_name2)
    line_chart(csv_name3)


if __name__ == '__main__':
    main()