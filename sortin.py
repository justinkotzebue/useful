import os
import re
import glob
import time

input_folder = r"\\ncr103\c$\Users\gras-user\Downloads\gpt_testing\zip"
pattern = os.path.join(input_folder, "*")
try:
    files = glob.glob(pattern)
except ValueError:
    print('cant find input files: \n {}'.format(pattern))


def sort_list_by_date(input_list, research_pattern='r\d{8}', date_format="%Y%m%d"):
    """
    Returns sorted list

    Parameters:
    -----------
    input_list : str
        list containing some kind of date format
    research_pattern : str
        search pattern used which returns the date (see library 're')
        defaults to 'r\d{8}' which corrsponds to %Y%m%d, Note that 'r' has to be added
    date_format : str
        needs to correspond to the format found with specified research_pattern
    Returns:
    --------
    Sorted list
    """
    sorted_list = sorted(input_list, key = lambda x:time.strptime(re.search(research_pattern, x).group(0), date_format))
    return sorted_list


print('dakdfjdkjfdkj'+
        'dfjdkjdfkj')
        
