import itertools
import json
users = []
hobbys = []
with open('users.csv', encoding='utf-8') as u_file:
    u_file_text = u_file.readlines()
    for user in u_file_text:
        users.append(user.strip())
with open('hobby.csv', encoding='utf-8') as h_file:
    h_file_text = h_file.readlines()
    for hobby in h_file_text:
        hobbys.append(hobby.strip())
if len(users) >= len(hobbys):
    out_dict = dict(itertools.zip_longest(users, hobbys, fillvalue=None))
else:
    exit(1)
with open('result_task_3.json', 'w') as r_file:
    json.dump(out_dict, r_file)
with open('result_task_3.json', encoding='utf-8') as file:
    data = json.load(file)
print(data)









