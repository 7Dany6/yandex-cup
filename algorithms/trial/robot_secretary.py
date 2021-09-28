import string

s = input()
result = 0
double_shift = 2
shift = 0

for i in s:
    if i in string.ascii_uppercase:
        shift += 1
    elif i in string.ascii_lowercase:
        double_shift += 1
if shift > double_shift:
    result = len(s) + double_shift
else:
    result = len(s) + shift
print(result)