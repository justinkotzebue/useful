import os
import re
import xml.etree.ElementTree as ET


replace_string = r"/home/jb/sen2cor/cfg/justindiana"

print(o.read())


r.replace(search_string, 'bla')
print(r)


import re
# infile = r"C:\Users\juko\Downloads\temp\acolite - Copy.cfg"
# outfile = r"C:\Users\juko\Downloads\temp\acolite_out.cfg"
# replace_string = ['CHL_OC2','CHL_OC3']

def change_config_file(infile, search_string, replace_string, outfile=infile):
    """
    Reads file seaches for Node and changes its values
    Parameters
    ----------
    infile : str
        input file path e.g. .txt, .cfg...
    search_string : str
        string to search what returns the string to be replaced
        e.g. 'limit=(.*)' searches for the node 'limit=' and returns what will
        be replaced
    replace_string : list or string
        New settings which will be used to replace original settings
    outfile : str
        output path including file ending [...,txt, cfg], default infile will be updated
    """
    if isinstance(replace_string, list):
        replace_string = ','.join(replace_string)
    to_change, original_text = get_config_settings(infile, search_string)
    print('Replacing "{}" with "{}"'.format(to_change, replace_string))
    text_changed = original_text.replace(to_change, replace_string)
    if outfile is not None:
        infile = outfile
    with open(infile, 'w') as dst:
        dst.write(text_changed)


def get_config_settings(infile, search_string):
    """Returns settings for search_string and original text of infile"""
    with open(infile, 'r') as f:
        compiler_pattern = search_string + '(.*)'
        compiling = re.compile(compiler_pattern)
        original_text = f.read()

        settings = compiling.findall(original_text)
        if not settings:
            raise ValueError('Cant find {} in {}'.format(compiler_pa, infile))
    return settings, original_text


def xml_change_field(xml_in, search_string, replace_string, xml_out=[]):
    '''
    Search for 'node' and repace text in field & updates/writes new file

    Parameters
    ----------
    xml_in : str
        path to xml file to be updated
    search_string : str
        string of the node from which tex/value should be changed
    replace_string : str
    "<node>value</node>" --> node
        string which will be used for updating node to e.g. value_test
        "<node>value_test</node>"
    xml_out : str
        if given, new file will be written
        defaults to [] --> updating xml_in
    '''
    xml_out_defualt = 'empty: default'

    try:
        tree = ET.parse(xml_in)
        root = tree.getroot()
        for path in root.iter(search_string):
            print(path.text)
            if not path.text:
                print(path.text)
                print('search_string did not lead to results')
            path.text = replace_string
        if not xml_out:
            tree.write(xml_in)
        else:
            tree.write(xml_out)
    except :
        print('Error: sen2cor config xml could not be updated/written' +
              '\nxml_in: {}\nxml_out: {}\nsearch_string: {}\nreplace_string: {}'.format(
              xml_in, xml_out_defualt, search_string, replace_string))
