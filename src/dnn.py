# -*- coding:UTF-8 -*-

'''
使用简单的神经网络模型来完成
'''

import tensorflow as tf
import dataset

def wights_variable(shape):
    '''
    权重变量tensor
    :param shape:
    :return:
    '''
    wights = tf.truncated_normal(shape=shape,stddev=0.1)
    return tf.Variable(wights,dtype=tf.float32)

def biases_variable(shape):
    '''
    偏置变量tensor
    :param shape:
    :return:
    '''
    bias = tf.constant(0.1,shape=shape)
    return tf.Variable(bias,dtype=tf.float32)


def nn(nn_name,input_data,input_num,out_num):
    '''
    建立一层网络层
    :param input_data: 网络层输入tensor
    :param input_num: 网络输入神经单元个数
    :param out_num: 网络输出神经单元个数
    :return:
    '''
    with tf.name_scope(nn_name):
        wights = wights_variable([input_num,out_num])
        biases = biases_variable([out_num])
        output = tf.multiply(input_data,wights)+biases

    return tf.nn.relu(output)



def main():

    train_x,train_y,test_x,test_y = dataset.read_data()

    with tf.name_scope('input'):
        x = tf.placeholder(dtype=tf.float32,shape=[None,1200])
        label = tf.placeholder(shape=[None,2])







if __name__=='__main__':
    main()

