# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:27:20 2021

@author: Shao
"""

import time
import multiprocessing as mp

def task(v,num):
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        print(v.value)

def multicore():
    v=mp.Value('i',0)
    P1=mp.Process(target=task,args=(v,1))
    P2=mp.Process(target=task,args=(v,5))
    P1.start()
    P2.start()
    P1.join()
    P2.join()

if __name__=='__main__':
    mp.freeze_support()
    multicore()