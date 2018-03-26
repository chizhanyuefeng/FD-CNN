# -*- coding:UTF-8 -*-

'''
CNN模型
'''

import tensorflow as tf

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

def conv2d(x,kernel):
    '''
    网络卷积层
    :param x: 输入x
    :param kernel: 卷积核
    :return: 返回卷积后的结果
    '''

    return tf.nn.conv2d(x,kernel,strides=[1,1,1,1],padding='SAME')

def max_pooling_2x2(x):
    '''
    最大赤化层
    :param x: 输入x
    :return: 返回池化后数据
    '''
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

def lrn(x):
    '''
    local response normalization
    局部响应归一化,可以提高准确率
    :param x: 输入x
    :return:
    '''

    return tf.nn.lrn(x,4,1.0,0.0001,0.75)


def fall_net(x):
    '''
    跌到检测网络
    :param x: 输入tensor,shape=[None,]
    :return:
    '''

    with tf.name_scope('reshape'):
        tf.reshape(x,[-1,20,20,3])

    with tf.name_scope('conv1'):
        # value shape:[-1,18,18,32]
        conv1_kernel = wights_variable([5,5,3,32])
        conv1_bias = biases_variable([32])
        conv1_conv = conv2d(x,conv1_kernel)+conv1_bias
        conv1_value = tf.nn.relu(conv1_conv)

    with tf.name_scope('max_pooling_1'):
        # value shape:[-1,10,10,32]
        mp1 = max_pooling_2x2(conv1_value)

    with tf.name_scope('conv2'):
        # value shape:[-1,8,8,64]
        conv2_kernel = wights_variable([5,5,32,64])
        conv2_bias = biases_variable([64])
        conv2_conv = conv2d(mp1,conv2_kernel)+conv2_bias
        conv2_value = tf.nn.relu(conv2_conv)

    with tf.name_scope('max_pooling_2'):
        # value shape:[-1,5,5,64]
        mp2 = max_pooling_2x2(conv2_value)

    with tf.name_scope('fc1'):
        fc1_wights = wights_variable([5*5*64,512])
        fc1_biases = biases_variable([512])

        fc1_input = tf.reshape(mp2,[-1,5*5*64])
        fc1_output = tf.nn.relu(tf.matmul(fc1_input,fc1_wights)+fc1_biases)

    with tf.name_scope('drop_out'):
        keep_prob = tf.placeholder(dtype=tf.float32)
        drop_out = tf.nn.dropout(fc1_output,keep_prob)

    with tf.name_scope('fc2'):
        fc2_wights = wights_variable([512,2])
        fc2_biases = biases_variable([2])
        fc2_output = tf.matmul(drop_out,fc2_wights)+fc2_biases

    return fc2_output,keep_prob


def train_model():
    '''
    训练模型,并将训练的模型参数进行保存
    :return: 返回训练好模型参数
    '''
    pass

def test_model():
    '''
    使用训练好的模型进行测试
    :return: 测试结果
    '''
    pass


if __name__=='__main__':

    train_model()
    test_model()