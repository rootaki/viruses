
# !usr/bin/Python3
# Made by Aki

import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")

i = 1

for i in range(60):
    
    new_folder = "Hacked " + str(i)
    folder_path = os.path.join(desktop, new_folder)
    
    os.mkdir(folder_path)
    i = i + 1
