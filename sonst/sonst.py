

def filter_list_by_time_window(list, start_time=None, end_time=None):
    """Filters list by start and end date, which must be part of the list

    Parameters
    ----------
    list : list
        list to be filtered by date
    start_time : int
        e.g. 20170808
    end_date : int
        e.g. 20170809
    Returns
    -------
    filtered list

    """

    if start_time > end_time:
        raise ValueError('sart time must be before end time!')
    if start_time:
        listscenes = [x for x in listscenes if int(re.search(8*'\d', os.path.basename(x)).group(0)) >= start_time]
    if end_time:
        listscenes = [x for x in listscenes if int(re.search(8*'\d', os.path.basename(x)).group(0)) <= end_time]

    return listscenes
