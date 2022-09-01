__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
from zipfile import ZipFile 

def clean_cache():
  directory = "cache"
  parent_dir = "C:\\Users\\Merijn\\Desktop\\Winc_Academy\\Backend Development\\files"
  path = os.path.join(parent_dir, directory)
  if os.path.exists(path):
    shutil.rmtree(path)
    os.makedirs(path)
  else: 
    os.mkdir(path)
  return path

clean_cache()

def cache_zip(zip_file_path, cache_dir_path):
  with ZipFile(zip_file_path, 'r') as zip:
    zip.extractall(cache_dir_path)

cache_zip(zip_file_path="C:\\Users\\Merijn\\Desktop\\Winc_Academy\\Backend Development\\files\data.zip", cache_dir_path=clean_cache())

def cached_files():
  path = "C:\\Users\\Merijn\\Desktop\\Winc_Academy\\Backend Development\\files\\cache"
  file_list = os.listdir(path)
  file_path_list = []
  for file in file_list:
    file_path_list.append(path + '\\' + file)
  return file_path_list

def find_password(file_list):
  for file_path in file_list:
    word = 'password'
    with open(file_path, 'r') as fp:
      lines = fp.readlines()
      for line in lines:
        if line.find(word) != -1:
          password_line = line
  return password_line[password_line.find(' ') + 1:].replace('\n', '')


