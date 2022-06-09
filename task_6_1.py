with open('nginx_logs.txt') as file:
    for line in file:
        result = tuple([line.split()[0], line.split()[5], line.split()[6]])
        print(result)










