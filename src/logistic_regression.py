# -*- coding:UTF-8 -*-

'''
从简单的逻辑回归做起预测数据
'''

import tensorflow as tf
import numpy as np
import pandas as pd

INPUT_NUM = 400
OUTPUT_NUM = 2

def read_data(data_path):
    '''
    读取跌倒和日常数据
    :param data_path:　跌到数据和日常数据的文件路径
    :return:　
    '''
    # TODO:从csv文件读取数据
    train_x = np.array((2000,400))
    train_y = np.array((2000,1))
    test_x = np.array((50,400))
    test_y = np.array((50,1))

    return train_x,train_y,test_x,test_y

def wight_variable(shape):
    '''
    权重tensor
    :param shape: 权重shape
    :return:
    '''
    # stddev为正态分布的标准差,采用正态分布初始化数值
    wights = tf.truncated_normal(shape=shape,stddev=0.1)
    return tf.Variable(wights,dtype=tf.float32)

def bias_varibale(shape):
    '''
    偏置tensor
    :param shape: 偏置tensor
    :return:
    '''
    # 初始化bias数值
    bias = tf.constant(0.1,shape=shape)
    return tf.Variable(bias,dtype=tf.float32)


def logistic_regression(x):
    '''
    逻辑回归方法
    :param x:　输入层
    :return:　输出层
    '''
    with tf.name_scope('logistic'):
        wights = wight_variable([400,1])
        biases = bias_varibale([1])
        y = tf.nn.sigmoid(tf.multiply(x,wights)+biases)
    return y

def get_data_batch(size):
    '''
    获取size份数据
    :param size: batchsize
    :return:
    '''
    # TODO: 需要实现从数据中随机获取size份数据,采用抽样不放回策略
    batch_x = np.array([2,3])
    batch_y = np.array([2,3])
    return batch_x,batch_y

def main():

    x,y,test_x,test_y = read_data('')

    with tf.name_scope('input_label_init'):
        train_x = tf.placeholder(tf.int16,[None,400])
        label_y = tf.placeholder(tf.int16,[None,1])

    y_ = logistic_regression(train_x)

    with tf.name_scope('loss'):
        loss = tf.reduce_mean(tf.square(y_-label_y))

    with tf.name_scope('gradient'):
        train = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

    with tf.name_scope('accuracy'):
        predict = y_ >= 0.5
        label = y
        correct = tf.equal(predict,label)
        accuracy = tf.reduce_mean(correct)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for step in range(10000):
            batch_x,batch_y = get_data_batch(50)
            sess.run(train,feed_dict={train_x:batch_x,label_y:batch_y})

            if step%100 ==0:
                print(sess.run(accuracy,feed_dict={train_x:batch_x,label_y:batch_y}))


if __name__=='__main__':
    main()


