#
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
    dimension = data_array.shape
    if not len(dimension) == 2:
        raise ValueError('Shape must be two dimensions not {}'.format(dimension))

    print(data_array.dtype)
    if only_int and not data_array.dtype == 'uint8' and not data_array.dtype == 'uint16':
        uv = [num for num in uv if num.is_integer()]
    max_area = data_array.shape[0] * data_array.shape[1]
    print(max_area)

    if max_area == len(uv):
        print('No values were repeated!')
        return

    nr = []  # number
    val = []  # value
    p = []  # percent
    for i, unique in enumerate(uv):
        # print(i)
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


# u = print_number_of_unique_pixels(data[0,:,:],100,only_int=True)
# d = data.shape
# len(d)
# data_array = type(data[0,:,:])
# dtpye = data.dtype
# dtpye == 'uint8'
