from random import randint
from random import seed as random_seed
import time
from dask import delayed
L = []


def gen_data(seed):
    # Notice: random is seeded by system time, so when 100 of these are run on the cluster simultaneously,
    # they all use the same random numbers. To prevent this, seed from the job id.
    random_seed(seed)
    return randint(1,60)


def my_sleep(n):
    time.sleep(n)
    return n


def summarize(result):
    return result


for i in range(1,100):
    data = delayed(gen_data)(i)  # pass i to gen_data, to be used as random seed, so all jobs will seed differently
    L.append(delayed(my_sleep)(data))

#for fn in filenames:                  # Use for loops to build up computation
#    data = delayed(load)(fn)          # Delay execution of function
#    L.append(delayed(process)(data))  # Build connections between variables

result = delayed(summarize)(L)
result_L = result.compute()  # type: list

print(result_L)

