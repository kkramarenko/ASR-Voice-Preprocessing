#!/usr/bin/python3
import os
import fnmatch
import shutil

dir_good_once    = 'good_once/'
dir_not_recog    = 'not_recognized/'
dir_not_found_pb = 'not_found_in_phonebook/' 
dir_name         = '../pcm_files/'

bad_file_size_edge = 15

try:
    os.mkdir(dir_good_once)
except FileExistsError:
    print('Directory "' + dir_good_once + '" existed!')

try:
    os.mkdir(dir_not_recog)
except FileExistsError:
    print('Directory "' + dir_not_recog + '" existed!')

try:
    os.mkdir(dir_not_found_pb)
except FileExistsError:
    print('Directory "' + dir_not_found_pb + '" existed!')

for pcm_file in os.listdir(dir_name):
    if fnmatch.fnmatch(pcm_file, '*.pcm'):
        #print(file_name)
        file_name = pcm_file.split('.')[0]
        #print(file_name)
        bad_file = file_name + '.bad'
        good_file = file_name + '.good'
        if os.path.isfile(dir_name + bad_file):
            try:
                file_size = os.path.getsize(dir_name + bad_file)
                if file_size < bad_file_size_edge:
                    shutil.copy2(dir_name + bad_file, dir_not_recog + bad_file)
                    shutil.copy2(dir_name + pcm_file, dir_not_recog + pcm_file)           
                else:    
                    shutil.copy2(dir_name + bad_file, dir_not_found_pb + bad_file)
                    shutil.copy2(dir_name + pcm_file, dir_not_found_pb + pcm_file)
            except OSError:
                print('Permission denied for file:' + bad_file)
        if os.path.isfile(dir_name + good_file):
            shutil.copy2(dir_name + good_file, dir_good_once + good_file)
            shutil.copy2(dir_name + pcm_file, dir_good_once + pcm_file)

