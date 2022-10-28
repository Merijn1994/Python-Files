__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
from zipfile import ZipFile

parent_dir = os.path.dirname(__file__)
directory = "cache"
path = os.path.join(parent_dir, directory)

def clean_cache():
  if os.path.exists(path):
    shutil.rmtree(path)
  os.mkdir(path)

def cache_zip(zip_file, cache_dir_path):
  with ZipFile(zip_file, 'r') as zip:
    zip.extractall(cache_dir_path)

def cached_files():
  file_list = os.listdir(path)
  file_path_list = []
  for file in file_list:
    file_path_list.append(os.path.join(path, file))
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

if __name__ == "__main__":
  clean_cache()
  cache_zip(zip_file = os.path.join(parent_dir, "data.zip"), cache_dir_path=path)
  print(find_password(cached_files()))



