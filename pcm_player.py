#!/usr/bin/python3
import pyaudio
import os
import fnmatch
import shutil
import sys

def play_pcm(filename):
    p = pyaudio.PyAudio()
    stream = p.open(format = pyaudio.paInt16,
                channels = 2,
                rate = 24000,
                output = True)

    with open(filename, 'rb') as pcm_file:
        pcm_data = pcm_file.read()
        stream.write(pcm_data)
    stream.stop_stream()

    stream.close()
    p.terminate()

def menu_show():
    print('MENU:')
    print('1 - Play pcm file')
    print('2 - View decoded string')
    print('3 - Edit decoded string')
    print('4 - Add pcm file to test dataset')
    print('5 - Next pcm file')
    print('6 - Quit')

def process_file(path, copy_path, pcm_file, ds_file):
    flag = True
    decoded_string = ''
    while(flag):
        print('File in process:' + pcm_file)
        menu_show()
        value = input('Choose item:')
        menu_item = int(value)
        if (menu_item == 1):
            play_pcm(path + pcm_file)

        elif (menu_item == 2):
            with open(path + ds_file, 'r') as fd:
                decoded_string = fd.read()
            print(decoded_string)

        elif (menu_item == 3):
            decoded_string = input('Enter string for pcm file:')

        elif (menu_item == 4):
            shutil.copy(path + pcm_file, copy_path + pcm_file)
            file_name = ds_file.split('.')[0]
            with open(copy_path + file_name + '.ds', 'w') as fd:
                print(decoded_string)
                fd.write(decoded_string)
            fd.close()

        elif (menu_item == 5):
            flag = False

        elif (menu_item == 6):
            os._exit(0)

def main(pcm_path, copy_path, start_index):
    dir_name = pcm_path

    pcm_list = []
    decoded_string_list = []
    for file_name in os.listdir(dir_name):

        if fnmatch.fnmatch(file_name, '*.pcm'):
            pcm_file = file_name
            data_file = file_name.split('.')[0]
            bad_file = data_file + '.bad'
            good_file = data_file + '.good'
            if os.path.isfile(dir_name + bad_file):
                pcm_list.append(pcm_file)
                decoded_string_list.append(bad_file)
            if os.path.isfile(dir_name + good_file):
                pcm_list.append(pcm_file)
                decoded_string_list.append(good_file)

    print('pcm list len - ' + str(len(pcm_list)))
    print('ds list len - ' + str(len(decoded_string_list)))
    for index in range(start_index,len(pcm_list)):
        print('index - ', index)
        print(pcm_list[index])
        print(decoded_string_list[index])
        process_file(dir_name, copy_path, pcm_list[index], 
                decoded_string_list[index])

if __name__ == '__main__':
    abs_path_name = os.path.abspath(os.getcwd()) + '/'
    if (len(sys.argv) != 4):
        print('\nUsage: ' + sys.argv[0] + ' dir_with_pcm_files dir_to_copy start_index\n')
        os._exit(-1)
    path1 = abs_path_name + sys.argv[1] + '/'
    path2 = abs_path_name + sys.argv[2] + '/'
    start_index = int(sys.argv[3])
    main(path1, path2, start_index)
