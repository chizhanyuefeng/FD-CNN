# -*- coding:UTF-8 -*-

'''
用于处理日常行为数据。
根据下载下来的数据文件，日常行为的数据文件解析和提取与跌到数据文件处理存在不同之处。
'''

#import matplotlib.pyplot as plt
#mport pandas as pd

#def adl_line_chart(csv_file):

    #data = pd.read_csv(csv_file)

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
