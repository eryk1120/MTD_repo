import itertools
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import cpu_count
from data.example_data import data_generator
from src.timer_decorator import timeIt
# from tqdm import tqdm
import time

import  sys


@timeIt
def brute(ds):
    def _calcTotaDistance(permutation):
        totDist = 0
        for i in range(len(permutation) - 1):
            totDist += ds[permutation[i]][permutation[i + 1]]
        return totDist

    noCheckpoints = len(ds[0])
    permutations = itertools.permutations([i for i in range(noCheckpoints)], noCheckpoints)


    lowest = sum(ds[0])
    bestPermutation = list()

    for p in permutations:
        d = _calcTotaDistance(p)
        if lowest > d:
            lowest = d
            bestPermutation = p
    return bestPermutation, lowest

    # with ThreadPoolExecutor(max_workers=cpu_count()) as ex:
    #     futures = [(ex.submit(_calcTotaDistance(i)),i) for i in permutations]
    #     for d,road in as_completed(futures):
    #         if lowest > d:
    #             lowest =d
