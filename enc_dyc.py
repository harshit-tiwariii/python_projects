#1st ceaser cipher 
text='Hellow World'
custom_key='python'

def vigenere(message,key,direction):
    key_index=0
    alphabet='abcdefghijklmnopqrstuvwxyz'
    final_message=''

    for char in message.lower():
       if char == ' ': 
           final_message += char
       else :
           key_char=key[key_index % len(key) ]
           key_index+=1
      
           offset=alphabet.index(key_char)
           index=alphabet.find(char)
           new_index=(index+offset*direction)% len(alphabet)
           final_message += alphabet[new_index] 
    return final_message 

encryption= vigenere(text,custom_key,1)
print(encryption)
decryption=vigenere(encryption,custom_key,-1)
print(decryption)

