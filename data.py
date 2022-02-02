# data = input("This is STDIN:")
# print("Now we write STDOUT: " + data)
# print("Now we write STDERR: " + int(data) + 1)

# import os
# print("HOME: " + os.environ.get("HOME", ""))
# print("SHELL: " + os.environ.get("SHELL", ""))
# print("FRUIT: " + os.environ.get("FRUIT", ""))

# import sys
# print(sys.argv)

###############################
##### ON LINUX
###############################

# wc <pythonfile.py>
# echo $?

###############################


# import os
# import sys

# filename = sys.argv[1]
# if not os.path.exists(filename):
#     with open(filename, "w") as f:
#         f.write("New file created \n")
# else:
#     print("Error, the file {} already exists!".format(filename))
#     sys.exit(1)


# import subprocess
# subprocess.run(["date"])

# import subprocess
# result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
# print(result.returncode)
# print(result.stout)
# print(result.stout.decode().split())

# import os
# import subprocess

# my_env = os.environ.copy()
# my_env["PATH"] = os.pathsep.join(["/opt/myapp",my_env["PATH"]])
# result = subprocess.run(["myapp"], env=my_env)

# import sys
# logfile = sys.argv[1]
# with open(logfile) as f:
#     for line in f:
#         print(line.strip())


# import re
# import sys

# logfile = sys.argv[1]
# usernames = {}
# with open(logfile) as f:
#     for line in f:
#         if "CRON" not in line:
#             continue
#         pattern = r"USER \((\w)\)$"
#         result = re.search(pattern, line)
#         if result is None:
#             continue
#         name = result[1]
#         usernames[name] = usernames.get(name, 0) + 1
# print(usernames)

##################
##### FOURTH LAB
##################

#!/usr/bin/env python3
# import sys
# import os
# import re
# def error_search(log_file):
#   error = input("What is the error? ")
#   returned_errors = []
#   with open(log_file, mode='r',encoding='UTF-8') as file:
#     for log in  file.readlines():
#       error_patterns = ["error"]
#       for i in range(len(error.split(' '))):
#         error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
#       if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
#         returned_errors.append(log)
#     file.close()
#   return returned_errors
  
# def file_output(returned_errors):
#   with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
#     for error in returned_errors:
#       file.write(error)
#     file.close()
# if __name__ == "__main__":
#   log_file = sys.argv[1]
#   returned_errors = error_search(log_file)
#   file_output(returned_errors)
#   sys.exit(0)