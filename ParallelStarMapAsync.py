# Parallelizing with Pool.starmap_async()

import multiprocessing as mp
pool = mp.Pool(mp.cpu_count())

results = []

results = pool.starmap_async(howmany_within_range2, [(i, row, 4, 8) for i, row in enumerate(data)]).get()

# With map, use `howmany_within_range_rowonly` instead
# results = pool.map_async(howmany_within_range_rowonly, [row for row in data]).get()

pool.close()
print(results[:10])
#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]
