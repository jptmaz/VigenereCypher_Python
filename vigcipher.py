def vigenere_cipher():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = ""
    keyword = ""
    cipher = ""
    
    #ask encryption from user
    message = input("Enter message: ").upper()
    
    #read legnth of input
    message_legnth = len(message)
    
    #ask keyword from user
    keyword = input ("Enter keyword: ").upper()
    
    #expand the encryption key
    expanded_keyword = keyword
    expanded_keyword_legnth = len(expanded_keyword)
    
    while expanded_keyword_legnth < message_legnth:
        expanded_keyword = expanded_keyword + keyword
        expanded_keyword_legnth = len(expanded_keyword)
    
    key_position = 0
    
    #encrypt
    for letter in message:
        if letter in alphabet:
            position = alphabet.find(letter)
            key_character = expanded_keyword[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            new_position = position + key_character_position
            if new_position > 26:
                new_position = new_position - 26
            new_character = alphabet[new_position]
            cipher = cipher + new_character
        else:
            cipher = cipher + letter  
    return (cipher)

#output
print(vigenere_cipher())
