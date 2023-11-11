text = "this text has been overwritten"
with open('test.txt',"a") as file:
    file.write(text)