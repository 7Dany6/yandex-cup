import json
with open('input.txt') as file_input:
    lines = [i.replace('\n', '') for i in file_input.readlines()]
    dictionaries = [json.loads(elm) for elm in lines[1::]]
    n, m = map(int, lines[0].split())
result = {'offers': []}
length = len(dictionaries)
for i in range(m):
    if length != 0:
        result['offers'] += dictionaries[i]["offers"]
        length -= 1
    else:
        break
result['offers'] = result['offers'][:m]
with open('output.txt', 'w') as file_output:
    json.dump(result, file_output)
