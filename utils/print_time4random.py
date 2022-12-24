import random
import time


def print_time(f_l: list, args: None,
               n_max: int = None, a_max: int = None,
               n_min: int = 0, a_min: int = 0,
               n_iter: int = 100):
    acc = [[float('inf'), 0, float('-inf')] for _ in f_l]

    for i in range(n_iter):
        n = n_max if i == n_iter - 1 else random.randint(n_min, n_max)

        if args is None:

            if i == n_iter - 1:
                args = (
                    [random.randint(a_min, a_max) for _ in range(n)],
                    #random.randint(n_min, n),
                    random.randint(a_min, a_max)
                    # [random.choices(string.ascii_lowercase, k=k)]
                )
            else:
                args = (
                    list(range(n)),
                    a_max
                    #random.randint(n_min, n),

                    # [random.choices(string.ascii_lowercase, k=k)]
                )

        for j, f in enumerate(f_l):
            t0 = time.perf_counter()
            f(*args)
            t1 = time.perf_counter()

            acc[j][0] = min(acc[j][0], t1 - t0)
            acc[j][1] += (t1 - t0)
            acc[j][-1] = max(acc[j][-1], t1 - t0)

    print(get_time_string(f_l, acc, n_iter))


def get_time_string(f_l: list, acc: list, n_iter: int):
    max_fname = 0

    for f in f_l:
        max_fname = max(len(f.__name__), max_fname)

    time_string = ''.join(('\n', ' ' * (max_fname + 4), 'min', ' ' * 6, 'mean', ' ' * 5, 'max', '\n'))
    len1 = len(time_string) + 2
    time_string = ''.join((time_string, '=' * len1, '\n'))

    for k, f in enumerate(f_l):
        n_spase = max_fname - len(f.__name__) + 1
        f_str = ''.join(
            (f'{f.__name__}', ' ' * n_spase, f'{acc[k][0]: .1e} {acc[k][1] / n_iter: .1e} {acc[k][-1]: .1e}'))
        time_string = ''.join((time_string, f_str, '\n'))
    time_string = ''.join((time_string, '=' * len1, '\n'))

    return time_string
