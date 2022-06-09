import sys
nums = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as file:
    result = file.readlines()
    if len(nums) == 0:
        print("".join(result))
    elif len(nums) == 1:
        start_line = int(nums[0])
        if start_line == 0:
            exit()
        else:
            out = result[start_line - 1:]
            print("".join(out))
    elif len(nums) == 2:
        start_line = int(nums[0])
        end_line = int(nums[1])
        out = result[start_line - 1:end_line]
        print("".join(out))
    else:
        exit()







