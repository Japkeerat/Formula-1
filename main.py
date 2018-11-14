import time
import os
import file_transfer_shutil as fts
import matplotlib.pyplot as plt

def execute_java(file_name):
    command = "".join(['java file_transfer ', file_name])
    java_time = os.popen(command).read()
    return java_time

    
def execute_python(file_name):
    start_time = time.process_time()
    fts.transfer(file_name)
    end_time = time.process_time()
    return end_time - start_time


def do_work(file_name):
    java_time = execute_java(file_name)
    python_time = execute_python(file_name)
    time_java.append(java_time)
    time_python.append(python_time)
    os.remove(file_name)


file_size = [10, 20, 30, 40, 50, 100, 200, 500, 1024, 2048]
time_java = []
time_python = []

for i in file_size:
    file_name = str(i)
    file_name = "".join([file_name,'MB.txt'])
    with open(file_name, "w") as out:
        out.seek((i * 1024 * 1024) - 1)
        out.write('\0')
    do_work(file_name)
    os.remove("Java.txt")
    os.remove("python.txt")
    
plt.plot(file_size, time_java, label = 'Java', color = 'blue')
plt.plot(file_size, time_python, label = 'Python', color = 'red')
plt.xlabel('File Size(in MB)')
plt.ylabel('Time(in seconds)')
plt.legend()
plt.show()