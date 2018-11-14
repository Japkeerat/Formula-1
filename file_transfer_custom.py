
def transfer(file_name):
    file_write = open("Python1.txt", 'w')
    with open(file_name, 'r') as file_read:
        data = file_read.readline()
        file_write.write(data)
    file_write.close()