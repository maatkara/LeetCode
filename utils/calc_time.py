from datetime import datetime
import time


def get_time1(f, *args):
    """ Моя """
    tic = datetime.now()
    _ = f(*args)
    toc = datetime.now()
    t = (toc - tic).total_seconds()
    return t


def get_time(f, *args, n_iter=100):
    """

    :param f:
    :param args:
    :param n_iter:
    :return:
    """
    acc = float('inf')
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc

