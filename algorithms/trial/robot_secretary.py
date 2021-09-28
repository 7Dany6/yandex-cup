import string

s = input()
result = 0
double_shift = 2
shift = 0

for i in s:
    if i in string.ascii_uppercase:
        if shift + 2 < double_shift:
            double_shift = shift + 2
        shift += 1
    elif i in string.ascii_lowercase:
        if shift > double_shift + 2:
            shift = double_shift + 2
        double_shift += 1
if shift > double_shift:
    result = len(s) + double_shift
else:
    result = len(s) + shift
print(result)