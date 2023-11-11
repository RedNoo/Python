try:
    with open('/home/kayayan/Desktop/bulk_upload_statuses.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
