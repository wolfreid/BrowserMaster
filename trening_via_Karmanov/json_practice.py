import json
import requests

#create request to API JSONPlaceholder

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)#deserialize json code of response.text
# with open("text.txt","w") as file:
#     for line in todos:
#         file.write(json.dumps(line)+'\n')
#print(todos == response.json()) # True
#словарь все пользователей
todos_by_user = {}

# for todo in todos:
#     if todo["completed"]:
#         try:
#             # Увеличение количества существующих пользователей.
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             # Новый пользователь, ставим кол-во 1.
#             todos_by_user[todo["userId"]] = 1

for todo in todos:
    if todo["completed"]:
        #смотрим только на выполненный задачи
        #print(todo["completed"])#key checking 
        try:
            #каккак действие
            todos_by_user[todo["userId"]] += 1 
            #всего десять пользователей, которые выполнили хотя бы одну задачу
            #print("work",todos_by_user)
            print(todo["id"])
        except KeyError:#если userId не найден - первый пользователь
            todos_by_user[todo["userId"]] = 1
            #print("not work",todos_by_user)
            #print(todo["id"]) - вывел все выполненный задачи задачи

top_users = sorted(todos_by_user.items(), 
                   key=lambda x: x[1], reverse=True)

max_complete = top_users[0][1]

users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))
 
max_users = " and ".join(users)

print(max_users)

s = "s" if len(users) > 1 else ""

print(f"user{s} {max_users} completed {max_complete} TODOs")

