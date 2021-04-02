mystring = "/physaria/2021323"


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


# subst = mystring.split("/", 1)
subst = find(mystring, '/')
# print("***>>> " + str(subst))
# print(subst[len(subst)-1])
# print("sub")
print(mystring[0: subst[len(subst)-1]])
