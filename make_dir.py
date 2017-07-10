import os
import yaml

working_folder = '/home/jb/Downloads/test'
folder_dict = dict(
            f2 = os.path.join(d,'f2'),
            f3 = os.path.join(d, 'f3'),
            f4 = os.path.join(d,'f2', 'f21')
            )


def mkdir_using_dict(dict, working_folder):
    """Creates directory structure given in dict in working_folder """
    if not os.path.exists(working_folder):
        os.mkdir(working_folder)
    for a ,b in folder_dict.items():
        try:
            os.mkdir(b)
        except:
            continue


def write_dict_to_yaml(file_path, dict_):
    '''write dict to yaml'''
    with open(file_path, 'w') as f:
      yaml.dump(dict_, f, default_flow_style=False)


def read_yaml_as_dict(yaml_path):
    '''read yaml and returns dict'''
    with open(yaml_path, 'r') as f:
        ym=yaml.safe_load(f)
    return ym
