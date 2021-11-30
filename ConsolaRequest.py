import requests
import json

url = "http://jsonplaceholder.typicode.com/posts/"
print(url)
r = requests.get(url)
lineas = r.text
datos = json.loads(lineas)
for registro in datos:
    userId = registro['userId']
    id = registro['id']
    title = registro['title']
    body = registro['body']
    print(f"El userId es: {userId}, el id es: {id}, el titulo es {title} y el body contiene {body}")