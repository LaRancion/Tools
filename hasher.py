import sys
import os
import subprocess
import shlex

system_os = sys.argv[1]
option = sys.argv[2]


def hashing():

    if system_os == 'windows':
        md5 = 'md5sum.exe "{}"'.format(file)
        sha256 = 'sha256.exe "{}"'.format(file)

    if system_os == 'unix':
        sha256 = 'sha256sum "{}"'.format(file) 
        md5 = 'md5sum "{}"'.format(file)

    md5_hash = subprocess.check_output(shlex.split(md5)).decode().split()[0]
    sha256_hash = subprocess.check_output(shlex.split(sha256)).decode().split()[0]
    
    return md5_hash, sha256_hash
    
if option == 'folder':
    files = []
    folder_path = input('folder path: ')
    for root, dirs, target_files in os.walk(folder_path):
        for file in target_files:
            files.append(os.path.join(root, file))

if option == 'files':
    files = input('files (separated by spaces): ').split()

with open('hashed.txt', 'w') as f:
    for file in files:
        md5_hash, sha256_hash = hashing()
        if md5_hash and sha256_hash:
            f.write(f'{file}\nMD5: {md5_hash}\nSHA256: {sha256_hash}\n\n')
        else:
            print("missing an output hash")

