from multiprocessing import Pool
import time

def f(x):
    return x*x

if __name__ == "__main__":
    N = [10, 1000, 100000]#0を追加
    print("単純実装")
    for n in N:
        start = time.time()
        for x in range(n):
            f(x)
        print("n:{} time:{}".format(n, time.time()-start))

    print("並列処理")
    for n in N:
        start = time.time()
        with Pool(processes=4) as pool:
            pool.map(f, range(n))
        print("n:{} time:{}".format(n, time.time()-start))   
