#! python3
# synchSubtitles.py - Change subtitle's time to synchronize it with a given audio.

import re, os, shutil
from lib.timeMethods import Synchronize

def save_synched_sub(text, filename):
    """Store the syncronized subtitle in the folder "./output_files"."""  
    file_object = open(os.path.join('.\output_files', filename), 'w')
    file_object.write(text)
    file_object.close()
    
def get_synched_text(sub_text, delta_time):
    # Create a regex for the time format contained in the text.
    timeRegex = re.compile(r'\d{2}:\d{2}:\d{2},\d{3}')
    time_list = timeRegex.findall(sub_text)
    for old_time in time_list:
        new_time = Synchronize(old_time).add(delta_time)
        oldTimeRegex = re.compile(old_time)
        sub_text = oldTimeRegex.sub(new_time, sub_text)
    return sub_text
    
def clean_old_subs():
    subs_dir = "./output_files"
    if os.path.exists(subs_dir):
        shutil.rmtree(subs_dir)
    os.makedirs(subs_dir, exist_ok=True)

    
import lib.check as check

def start(delta='00:00:00,000'):
    clean_old_subs()
    for folderName, subfolders, filenames in os.walk('./input_files'):
        for filename in filenames:
            check.file_name(filename)
            
            file_object = open(os.path.join('./input_files', filename), 'r')
            subtitle_text = file_object.read()
            file_object.close()
            
            check.file_content(subtitle_text)
            new_sub_text = get_synched_text(subtitle_text, delta)
            save_synched_sub(new_sub_text, filename)
            
delta = '- 00:00:07,000'
start(delta)