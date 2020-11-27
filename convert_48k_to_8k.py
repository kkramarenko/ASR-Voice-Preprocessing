#!/usr/bin/python3
import os
import sys

argc = len(sys.argv)

if (argc < 3):
    print("Not enough parameters!")
    print("Usage: ./convert_48k_to_8k.py name_48k.{pcm|wav} name_8k.{pcm|wav}")
    sys.exit(1)

name_48k_file = sys.argv[1]
name_8k_file  = sys.argv[2]

command = 'ffmpeg -f s16le -ar 48k -ac 1 -i ' + name_48k_file + ' -f s16le -ar 8k -ac 1 ' + name_8k_file  
ret = os.system(command)
