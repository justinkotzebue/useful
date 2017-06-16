
#count uniqe values in array
import np

def print_number_of_unique_pixels(data_arary):
    uv = np.unique(data_arary)
    if len(uv) > 50:
        print("Counted too many unique pixels! \n {uv}".format(uv))
    else:
        for u in uv:
            max_area = data_arary.shape[0] * data_arary.shape[1]
            n = np.count_nonzero(data_arary == u)
            perc = float(n)/max_area
            print('Value: {} * {} : {}%'.format(u, n, int(perc*100)))
