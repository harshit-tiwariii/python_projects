def verify_card_number(card_number):
    sum_of_odd_numbers=0
    reversed_card_number=card_number[::-1]
    odd_digits=reversed_card_number[::2]

    for digit in odd_digits:
        sum_of_odd_numbers += int(digit)

    sum_of_even_numbers=0
    even_digits=reversed_card_number[1::2]
    
    for digit in even_digits:
        number= int(digit)*2
        if number >= 10:
            number= number//10+number%10
        sum_of_even_numbers+=number
        total=sum_of_even_numbers+sum_of_odd_numbers
    return total %10 == 0

def main():
    card_number = '4111-1111-4555-1142'
    translated_card= str.maketrans({'-': '',' ':''})
    translated_number=card_number.translate(translated_card)

    if verify_card_number(translated_number):
        print('VALID')
    else:
        print('INVALID')

main()