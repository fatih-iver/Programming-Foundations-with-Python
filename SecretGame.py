import os
from string import digits

file_list = os.listdir(r"C:\Users\fatih\Downloads\prank")

os.chdir(r"C:\Users\fatih\Downloads\prank")

for file_name in file_list:
    os.rename(file_name, file_name.translate(str.maketrans('', '', digits)))