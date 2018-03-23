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


def net(nn_name,input_data,input_num,out_num):
    '''
    建立一层网络层
    :param input_data: 网络层输入tensor
    :param input_num: 网络输入神经单元个数
    :param out_num: 网络输出神经单元个数
    :return: 返回测试结果
    '''
    with tf.name_scope(nn_name):
        wights = wights_variable([input_num,out_num])
        biases = biases_variable([out_num])
        output = tf.multiply(input_data,wights)+biases

    return tf.nn.relu(output)

def dnn(x):
    '''
    神经网络
    :param x: 输入值
    :return: 网络输出层
    '''

    net1 = net('frist_net',x,1200,512)
    net2 = net('second_net',net1,512,64)
    net3 = net('third_net',net2,64,2)

    return net3

def main():

    train_x,train_y,test_x,test_y = dataset.read_data()

    with tf.name_scope('input'):
        x = tf.placeholder(tf.float32,[None,1200])
        label = tf.placeholder(tf.float32,[None,2])

    y_ = dnn(x)

    with tf.name_scope("loss"):
        loss = tf.nn.softmax_cross_entropy_with_logits(labels=label,logits=y_)










if __name__=='__main__':
    main()

