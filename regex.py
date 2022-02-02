# https://regex101.com/
# 
# 
# import re
# log = "Jule 31 07:05:51 my computer bad_process[12345]: ERROR Performing package upgrade"
# regex = r"\[(\d+)]"
# result = re.search(regex,log)
# print(result[1])

# Comandos de linux
#grep -i python <ruta>
#grep l.rts <ruta>
#grep ^fruit <ruta>
#grep cat$ <ruta>

import re
result = re.search(r"aza", "plaza")
print(result)
# result = re.search(r"aza", "maze")
# print(result)
# result = re.search(r"p.ng", "Pangea", re.IGNORECASE)
# print(result)
# result = re.search(r"[Pp]ython", "Python")
# print(result)
# result = re.search(r"[a-z]way", "The end of the highway")
# print(result)
# result = re.search(r"cloud[a-zA-Z0-9]", "cloudy")
# print(result)
# result = re.search(r"[^a-zA-Z]", "This is a sentence with spaces.")
# print(result)
# result = re.search(r"[^a-zA-Z ]", "This is a sentence with spaces.")
# print(result)
# result = re.search(r"cat|dog", "I like dogs")
# print(result)
# result = re.findall(r"cat|dog", "I like cats and dogs")
# print(result)
# result = re.search(r"Py.*n", "Pygmalion")
# print(result)
# result = re.search(r"Py.*n", "Python programming")
# print(result)
# result = re.search(r"Py[a-z]*n", "Python programming")
# print(result)
# result = re.search(r"o+l+", "goldfish")
# print(result)
# result = re.search(r"o+l+", "wolly")
# print(result)
# result = re.search(r"o+l+", "boil")
# print(result)
# result = re.search(r"p?each", "To each their own")
# print(result)
# result = re.search(r"\.com", "welcome.com")
# print(result)
# result = re.search(r"\w*", "welcome home")
# print(result)
# result = re.search(r"\w*", "welcome_home")
# print(result)
# result = re.search(r"^A.*a$", "Argentina")
# print(result)
# result = re.search(r"^A.*a$", "Azerbaijan")
# print(result)

# pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
# print(re.search(pattern, "_This_is_valid"))
# print(re.search(pattern, "This is not"))

#################################
##### ADVANCE REGULAR EXPRESSION
#################################

# import re
# result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
# print(result)
# print(result.groups())
# print(result[0])
# print(result[1])
# print(result[2])

# def fix_name(name):
#     result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
#     if result == None:
#         return name
#     return "{} {}".format(result[2], result[1])

# print(fix_name("Kennedy, John F."))

# import re
# print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))
# print(re.findall(r"\w{5,10}", "I really like strawberries"))
# print(re.findall(r"\w{5,}", "I really like strawberries"))
# print(re.search(r"s\w{,20}", "I really like strawberries"))

# import re
# log = "Jule 31 07:05:51 my computer bad_process[12345]: ERROR Performing package upgrade"
# regex = r"\[(\d+)]"
# result = re.search(regex,log)
# print(result[1])

# import re
# result = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
# print(result)
# result = re.split(r"([.?!])", "One sentence. Another one? And the last one!")
# print(result)

# import re
# result = re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for yup@example.com")
# print(result)
# result = re.sub(r"^(\w*), (\w*)$", r"\2 \1", "Lovelace, Ada")
# print(result)

# result = re.split(r"the|a", "One sentence. Another one? And the last one!")
# print(result)

# import re
# input = "abcdefghi"
# result = re.sub('abc(def)(ghi)', r'\2', input)
# print(result)

#################
##### THIRD LAB
#################

# Full Name, Email Address
# Blossom Gill, blossom@abc.edu
# Hayes Delgado, nonummy@utnisia.com
# Petra Jones, ac@abc.edu
# Oleg Noel, noel@liberomauris.ca
# Ahmed Miller, ahmed.miller@nequenonquam.co.uk
# Macaulay Douglas, mdouglas@abc.edu
# Aurora Grant, enim.non@abc.edu
# Madison Mcintosh, mcintosh@nisiaenean.net
# Montana Powell, montanap@semmagna.org
# Rogan Robinson, rr.robinson@abc.edu
# Simon Rivera, sri@abc.edu
# Benedict Pacheco, bpacheco@abc.edu
# Maisie Hendrix, mai.hendrix@abc.edu
# Xaviera Gould, xlg@utnisia.net
# Oren Rollins, oren@semmagna.com
# Flavia Santiago, flavia@utnisia.net
# Jackson Owens, jackowens@abc.edu
# Britanni Humphrey, britanni@ut.net
# Kirk Nixon, kirknixon@abc.edu
# Bree Campbell, breee@utnisia.net

#!/usr/bin/env python3

# import csv
# import re

# def contains_domain(address, domain):
#   """Returns True if the email address contains the given domain,
#     in the domain position, false if not."""
#   domain_pattern = r'[\w\.-]+@'+domain+'$'
#   if re.match(domain_pattern, address):
#     return True
#   return False

# def replace_domain(address, old_domain, new_domain):
#   """Replaces the old domain with the new domain in
#     the received address."""
#   old_domain_pattern = r'' + old_domain + '$'
#   address = re.sub(old_domain_pattern, new_domain, address)
#   return address

# def main():
#   """Processes the list of emails, replacing any instances of the
#     old domain with the new domain."""
#   old_domain, new_domain = 'abc.edu', 'xyz.edu'
#   csv_file_location = '/home/student-00-7f0d7a4592b8/data/user_emails.csv'
#   report_file =  '/home/student-00-7f0d7a4592b8/data' + '/updated_user_emails.c$
#   user_email_list = []
#   old_domain_email_list = []
#   new_domain_email_list = []
#   with open(csv_file_location, 'r') as f:
#     user_data_list = list(csv.reader(f))
#     user_email_list = [data[1].strip() for data in user_data_list[1:]]
#     for email_address in user_email_list:
#       if contains_domain(email_address, old_domain):
#         old_domain_email_list.append(email_address)
#         replaced_email = replace_domain(email_address, old_domain, new_domain)
#         new_domain_email_list.append(replaced_email)
#     email_key = ' ' + 'Email Address'
#     email_index = user_data_list[0].index(email_key)
#     for user in user_data_list[1:]:
#       for old_domain, new_domain in zip(old_domain_email_list, new_domain_email$
#         if user[email_index] == ' ' + old_domain:
#           user[email_index] = ' ' + new_domain
#     f.close()
#   with open(report_file, 'w+') as output_file:
#     writer = csv.writer(output_file)
#     writer.writerows(user_data_list)
#     output_file.close()

# main()
