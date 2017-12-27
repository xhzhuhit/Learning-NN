# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:44:32 2017

@author: 晓辉
"""

from perception import Perception

def f(x):
    return 1 if x > 0 else 0
        
def get_training_dataset():
    input_vecs = [[1,1], [0,0], [1,0], [0,1]]
    labels = [1, 0, 1, 1]
    return input_vecs, labels
        
def train_and_perception():
    p = Perception(2, f)
    input_vecs, labels = get_training_dataset()
    p.train(input_vecs, labels, 10, 0.1)
    return p
    
if __name__ == '__main__':
    and_perception = train_and_perception()
    print and_perception
    print '1 and 1 = %d' % and_perception.predict([1, 1])
    print '0 and 0 = %d' % and_perception.predict([0, 0])
    print '1 and 0 = %d' % and_perception.predict([1, 0])
    print '0 and 1 = %d' % and_perception.predict([0, 1])