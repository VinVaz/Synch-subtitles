#! python3
# check.py - Check for formatation errors in a subtitle folder.

import logging, re, os

logging.basicConfig(level=logging.DEBUG, format='''%(asctime)s 
                    - %(levelname)s - %(message)s''')
    
def file_name(filename):
    name, ext = os.path.splitext(filename)
    extensions = ['.txt', '.srt']
    logging.warning('File name: {}, file  extension: {}'.format(name, ext))
    if ext not in extensions:
        raise Exception('''File "{}" is not in an 
                        acceptable format'''.format(filename))
    if name == '':
        raise Exception('Files must have a name')
                
def file_content(text):
    timeRegex = re.compile(r'\d{2}:\d{2}:\d{2},\d{3}')
    time_list = timeRegex.findall(text)
    if not time_list:
        raise Exception('''File must contain time 
                        representation in the format: "00:00:00,000"''')
