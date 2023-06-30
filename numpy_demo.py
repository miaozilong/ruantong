import random
import time

from loguru import logger as log
import numpy as np

log.add('file_{time:YYYY-MM-DD}.log', format="{name} {level} {message}", level="TRACE", rotation='5 MB',
        encoding='utf-8')

if __name__ == "__main__":
    np_array = np.array([[1, 2, 3], [4, 5, 6]])
    log.debug(np_array)
    # 常见的属性  shape ndim size
    log.debug(np_array.shape)
    log.debug(np_array.ndim)
    log.debug(np_array.size)
    log.debug(np_array.dtype)
    log.debug("==============")
    demo_array = np.array([[1, 2, 3], [4, 5, 6]])
    dot = demo_array.dot(demo_array.transpose())
    log.debug(dot.shape)
    log.debug("-------------------")
    reshape = np.arange(1, 151).reshape(3, 50)
    log.debug(reshape)
