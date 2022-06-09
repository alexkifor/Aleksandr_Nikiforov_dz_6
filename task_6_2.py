remote_addr = []
with open('nginx_logs.txt') as file:
    for line in file:
        remote_addr.append(line.split()[0])
remote_count = []
set_remote_addr = set(remote_addr)
for elem in set_remote_addr:
    num_count = remote_addr.count(elem)
    remote_count.append(num_count)
spam_count = max(remote_count)
spammer = [elem for elem in set_remote_addr if remote_addr.count(elem) == spam_count]
print(f'спамер c IP {spammer[0]} отправил {spam_count} запросов')
