################
###### EXAMPLES
################

# import shutil
# du = shutil.disk_usage('/')
# print(du)

# import psutil
# print(psutil.cpu_percent(0.5))
# print(psutil.cpu_percent(0.5))
# print(psutil.cpu_percent(0.5))
# print(psutil.cpu_percent(0.5))

# def check_disk_usage(disk):
#     du = shutil.disk_usage(disk)
#     free = du.free / du.total * 100
#     return free > 20

# def check_cpu_usage():
#     usage = psutil.cpu_percent(1)
#     return usage < 75

# if not check_disk_usage("/") or not check_cpu_usage():
#     print("ERROR")
# else:
#     print("All OK")


#######################
###### Work with files
#######################

# file = open("doc.txt")
# print(file.read())
# file.close()

# with open("doc.txt") as file:
#     print(file.readline())

# with open("doc.txt") as file:
#     for line in file:
#         # print(line.strip().upper())

# with open("write.txt", "w") as file:
#     file.write("It was stormy")

#####################
# "r" read only
# "w" write only
# "x" exclusive creation
# "a" append 
# "t" text mode (default) 
# "r+" read-write
#####################

# import os
# os.remove("write.txt")
# os.rename("new.txt", "doc.txt")
# os.rename("doc.txt", "new.txt")
# print( os.path.exists("doc.txt") )
# print( os.path.getsize("new.txt") )
# print( os.path.getmtime("new.txt") )

# import datetime
# timestamp = os.path.getmtime("new.txt")
# print( datetime.datetime.fromtimestamp(timestamp) )

############################
# python documentation
# class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
############################

# import os
# file= "file.dat"
# if  os.path.isfile(file):
#     print(os.path.isfile(file))
#     print(os.path.getsize(file))
# else:
#     print(os.path.isfile(file))
#     print("File not found")

# import os
# print( os.path.abspath("new.txt") )

# import os
# print(os.getcwd())
# os.mkdir("newDir")
# os.chdir("newDir")
# os.rmdir("newDir")
# os.listdir("newDir")

# import os
# dir = 'directory'
# for name in os.listdir(dir):
#     fullname = os.path.join(dir, name)
#     if os.path.isdir(fullname):
#         print("{} is a directory".format(fullname))
#     else:
#         print("{} is a file".format(fullname))



# import os
# def create_python_script(filename):
#   comments = "# Start of a new Python program"
#   with open(filename):
#     filesize = os.path.getsize(filename)
#   return(filesize)

# print(create_python_script("program.py"))

###########
###### CSV
###########

# import csv
# f = open("csv_file.txt")
# csv_f = csv.reader(f)
# for row in csv_f:
#     name, phone, role = row
#     print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
# f.close()

# import csv
# hosts = [["work.local", "192.168.1.1"], ["home.cloud", "10.2.5.256"]]
# with open('hosts.csv', 'w') as hosts_csv:
#     writer = csv.writer(hosts_csv)
#     writer.writerows(hosts)

# import csv
# with open('csv_file.txt') as people:
#     reader = csv.DictReader(people)
#     for row in reader:
#         print(("{} phone is {}").format(row["name"], row["phone"]))

# import csv
# users = [
#     {"name": "Robbie", "username": "Robb", "department": "IT"},
#     {"name": "Tommys", "username": "Tomm", "department": "RH"},
#     {"name": "Frodns", "username": "Frop", "department": "SA"}
# ]
# keys = ["name", "username", "department"]
# with open ('by_department.csv', 'w') as by_department:
#     writer = csv.DictWriter(by_department, fieldnames=keys)
#     writer.writeheader()
#     writer.writerows(users)


##################
###### SECOND LAB
##################

##!/usr/bin/env python3
# import csv
# def read_employees(csv_file_location):
#     csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
#     employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
#     employee_list = []
#     for data in employee_file:
#         employee_list.append(data)
#     return employee_list

# employee_list = read_employees('/home/student-00-7f0d7a4592b8/data/employees.csv')
# print(employee_list)

# def process_data(employee_list):
#     department_list = []
#     for employee_data in employee_list:
#         department_list.append(employee_data['Department'])
#     department_data = {}
#     for department_name in set(department_list):
#         department_data[department_name] = department_list.count(department_name)
#     return department_data
# dictionary = process_data(employee_list)
# print(dictionary)

# def write_report(dictionary, report_file):
#     with open(report_file, "w+") as f:
#         for k in sorted(dictionary):
#             f.write(str(k)+':'+str(dictionary[k])+'\n')
#     f.close()
# write_report(dictionary, '/home/student-00-7f0d7a4592b8/test_report.txt')

##################
###### FIRST LAB
##################

# #!/usr/bin/env python3
# import requests
# import socket

# def check_localhost():
#     localhost = socket.gethostbyname('localhost')
#     if localhost == '127.0.0.1':
#         return True
#     else:
#         return False

# def check_connectivity():
#     request = requests.get("https://www.google.com")
#     if request.status_code == 200:
#         return True
#     else:
#         return False


# #!/usr/bin/env python3
# from network import *
# import shutil
# import psutil
# def check_disk_usage(disk):
#     """Verifies that there's enough free space on disk"""
#     du = shutil.disk_usage(disk)
#     free = du.free / du.total * 100
#     return free > 20
# def check_cpu_usage():
#     """Verifies that there's enough unused CPU"""
#     usage = psutil.cpu_percent(1)
#     return usage < 75
# # If there's not enough disk, or not enough CPU, print an error
# if not check_disk_usage('/') or not check_cpu_usage():
#     print("ERROR!")
# elif check_localhost() and check_connectivity():
#     print("Everything ok")
# else:
#     print("Network checks failed")



























