def snake_case(pascal_case):
    snake_list=['_'+char.lower() if char.isupper() else char for char in pascal_case]

    return ''.join(snake_list).strip('_')
def main():
    print(snake_case('MYnameisHArsShit'))