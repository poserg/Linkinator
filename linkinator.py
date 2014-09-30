#!/usr/bin/env python3

from os import symlink, path, listdir, makedirs

from sys import argv

def mklink(src, dst):
    # print (src + " <==> " + dst)
    if not path.exists(dst) and not path.lexists(dst):
        symlink(src, dst, target_is_directory=True)
    

def run(src_dir, dst_dir):
    file_names = listdir(src_dir)
    if not path.exists(dst_dir):
        makedirs(dst_dir)
    for file in file_names:
        src_dir = path.abspath(src_dir)
        mklink(path.join(src_dir, file), path.join(dst_dir, file))

p = argv[1:]
run(p[0], p[1])
