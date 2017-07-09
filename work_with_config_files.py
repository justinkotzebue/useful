import os
import xml.etree.ElementTree as ET


cfg = r"/home/jb/Documents/acolite_linux/acolite_settings.cfg"
replace_string = r"/home/jb/sen2cor/cfg/justindiana"
search_string = 'limit'

o = open(cfg)
print(o.read())
r = o.read()
r.replace()
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
