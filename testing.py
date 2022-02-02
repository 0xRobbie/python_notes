# import re

# def fixname(name):
#     result = re.search(r"^([\w .]*), ([\w .]*)$", name)
#     if result is None:
#         return name
#     return "{} {}".format(result[2], result[1])


####################
##### EXCEPCIONES
####################

# def validar(username, minlen):
#     assert type(username) == str, "username is not string"
#     if minlen < 1:
#         return ValueError("minlen must be at least 1")
#     if len(username) < minlen:
#         return False
#     if not username.isalnum():
#         return False
#     return True

# print(validar("",-1))
# print(validar(" ",1))
# print(validar("user",1))
# print(validar([],1))
# print(validar(["name"],1))
