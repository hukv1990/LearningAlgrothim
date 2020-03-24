# coding=utf-8

import time


def calc_runing_time(func):
    def warp(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        print(func.__name__, f'running time = {end_time - start_time:.2f}s')
        return ret
    return warp