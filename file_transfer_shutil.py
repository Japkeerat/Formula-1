from shutil import copyfile

def transfer(file_name):
    copyfile(file_name, 'python.txt')