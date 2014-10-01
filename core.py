from os import symlink, path, listdir, makedirs
from random import random

video_ext = [".3gp", 
             ".avi", 
             ".mpg", 
             ".mov", 
             ".swf", 
             ".asf", 
             ".mp4", 
             ".wmv", 
             ".mts", 
             ".mkv", 
             ".flv",
             ".m2ts"]

def mklink(src, dst):
    # print (src + " <==> " + dst)
    if path.exists(dst) or path.lexists(dst):
        dst = generate_name(src, dst)
    symlink(src, dst)

def generate_name(src, dst):
    k = path.splitext(dst)
    return k[0] + str(random()) + k[1]
    
    

def run(src_dir, dst_dir):
    file_names = []
    try:
        file_names = listdir(src_dir)
    except PermissionError:
        print ("Permission denied: '" + src_dir + "'")
    if not path.exists(dst_dir):
        makedirs(dst_dir)
    for file in file_names:
        src_dir = path.abspath(src_dir)
        src = path.join(src_dir, file)
        if path.isdir(src):
            run(src, dst_dir)
        elif path.splitext(src)[1].lower() in  video_ext:
            mklink(src, path.join(dst_dir, file))
