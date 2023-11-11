import os
import shutil

path = 'cop_2.txt'

try:
    os.remove(path)
    # os.rmdir(path) delete folder
    # shutil.rmtree(path) delete folder not empty
except FileNotFoundError:
    print(path + 'ile not found')
except PermissionError:
    print("perrmission error")
except OSError:
    print("you cannot delete that using with this function")
else:
    print(path + " deleted")
