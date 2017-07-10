import os
import re
import xml.etree.ElementTree as ET


replace_string = r"/home/jb/sen2cor/cfg/justindiana"

print(o.read())


r.replace(search_string, 'bla')
print(r)


import re
cfg = r"/home/jb/Documents/acolite_linux/acolite_settings.cfg"
def read_file_change_string(infile, search_string, replace_string, outfile[]):
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
    replace_string : str
        string which will be used to replace original
    outfile : str
        output path, if empty infile will be updated
    """
    o = open(cfg)
    p = re.compile('limit=(.*)')
    s = o.read()
    to_repl = p.findall(s)
    text_changed = s.replace(to_repl[0], 'tessst')


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
