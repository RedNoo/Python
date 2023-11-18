from multiprocessing import Process, cpu_count

import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print(cpu_count())
    start_time = time.perf_counter()
    a = Process(target=counter, args=(50000000,))
    a.start()
    b = Process(target=counter, args=(50000000,))
    b.start()
    a.join()
    b.join()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("finished in : ", elapsed_time, "seconds")


if __name__ == '__main__':
    main()
