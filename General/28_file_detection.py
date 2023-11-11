import os

path = "/home/kayayan/Desktop/bulk_upload_statuses.txt"

if os.path.exists(path):
    print("That location exist")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("that is a directory")

else:
    print("location doesnt exist")
