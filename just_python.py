import file_transfer_shutil as fts
import file_transfer_custom as ftc
import time
import os
import matplotlib.pyplot as plt

file_size = [10, 20, 30, 40, 50, 100, 200, 500, 1024, 2048]
shutil_time = []
custom_time = []

def with_shutil(file_name):
    start_time = time.process_time()
    fts.transfer(file_name)
    end_time = time.process_time()
    return end_time - start_time


def with_custom(file_name):
    start_time = time.process_time()
    ftc.transfer(file_name)
    end_time = time.process_time()
    return end_time - start_time
    

def do_work(file_name):
    time_shutil = with_shutil(file_name)
    time_custom = with_custom(file_name)
    shutil_time.append(time_shutil)
    custom_time.append(time_custom)
    os.remove(file_name)
    

for i in file_size:
    file_name = str(i)
    file_name = "".join([file_name,'MB.txt'])
    with open(file_name, "w") as out:
        out.seek((i * 1024 * 1024) - 1)
        out.write('\0')
    do_work(file_name)
    os.remove("python.txt")
    os.remove("Python1.txt")
    
plt.plot(file_size, shutil_time, color = 'blue', label = 'Shutil')
plt.plot(file_size, custom_time, color = 'red', label = 'Simple File Handling')
plt.xlabel("File size(in MB)")
plt.ylabel("Execution time(in sec)")
plt.legend()
plt.show()