# -*- coding:UTF-8 -*-

'''
使用神经网络模型来完成
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
        output = tf.matmul(input_data,wights)+biases

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


    with tf.name_scope('input'):
        x = tf.placeholder(tf.float32,[None,1200])
        label = tf.placeholder(tf.float32,[None,2])

    y_ = dnn(x)

    with tf.name_scope("loss"):
        cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=label,logits=y_)
        loss = tf.reduce_mean(cross_entropy)

    with tf.name_scope('gradient'):
        train = tf.train.GradientDescentOptimizer(0.001).minimize(loss)

    with tf.name_scope('accuracy'):
        correct_prediction = tf.equal(tf.argmax(y_, 1), tf.argmax(label, 1))
        correct_prediction = tf.cast(correct_prediction, tf.float32)
        accuracy = tf.reduce_mean(correct_prediction)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for step in range(2000):
            # TODO:獲取batch函數尚未完成
            batch_x ,batch_label = next_batch(50)
            if step%100==0:
                current_accuracy = sess.run(accuracy,feed_dict={x:batch_x,label:batch_label})
                print('第',step,'步,准确率为',current_accuracy)
            sess.run(train,feed_dict={x:batch_x,label:batch_label})



if __name__=='__main__':
    main()

