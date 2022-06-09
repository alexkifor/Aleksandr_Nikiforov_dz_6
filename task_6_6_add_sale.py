import sys
argv = sys.argv[1]
with open('bakery.csv', 'a', encoding='utf-8') as file:
    file.write(f'{argv}\n')
