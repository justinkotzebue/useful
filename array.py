
#count uniqe values in array
import numpy as np
import pandas as pd
import operator

def print_number_of_unique_pixels(data_array, maximum_len_table=100,only_int=True):
    """
    return pandas table of unique values their count and percentage of total
    number of values

    data_array : array
        list or 2d array
    maximum_len_table : int
        maximul length of table containing highest counts
    only_int : bool
        only consider integer in unique values, if False processing time can
        increase drastically

    """
    uv = np.unique(data_array)
    if only_int:
        uv = [num for num in uv if num.is_integer()]
    try:
        max_area = data_array.shape[0] * data_array.shape[1]
    except:
        print("Exception")
        max_area = len(data_array)
    if max_area == len(uv):
        print('No values were repeated!')
        return

    nr = []  # number
    val = []  # value
    p = []  # percent
    for i, unique in enumerate(uv):
        print(i)
        number = np.count_nonzero(data_array == unique)
        perc = float(number)/max_area
        nr.append(number)
        val.append(unique)
        p.append(int(perc*100))
    d = {'Unique Value' : pd.Series(val),
        'Count' : pd.Series(nr),
        'Percent': pd.Series(p)}
    data = pd.DataFrame(d, dtype=float)
    sort = data.sort_values(by='Count', ascending=False)
    return sort[:maximum_len_table]
        #print('Value:{}: {} * {} : {}%'.format(i,u, n, int(perc*100)))

data_array = np.random.random((100,100))

data_array[1,4] = 2
data_array[1,67] = 4
data_array[1,3] = 4
data_array[1:55,88:9999] = 2
u = print_number_of_unique_pixels(data_array,100,only_int=False)
