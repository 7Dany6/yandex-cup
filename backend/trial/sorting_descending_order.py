import requests
url = input()
port = int(input())
a = int(input())
b = int(input())
r = requests.get(f'{url}:{port}?a={a}&b={b}')
answer = [i for i in r.json() if i > 0]
print(*sorted(answer, reverse=True), sep='\n')
